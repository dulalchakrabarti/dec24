import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import numpy as np

# ================= CONFIGURATION =================
BG_IMAGE = 'yb_2025_.png' 
ICON_IMAGE = 'cyclone_icon.png'
OUTPUT_NAME = 'sequential_cyclones.gif'

TOTAL_FRAMES = 300 # Increased to give enough room for sequential movement
FPS = 20          
ICON_SIZE_PX = 100 

# SEQUENTIAL TIMELINE SETTINGS
# 'start': frame number when it appears
# 'duration': how many frames it takes to finish its track
storm_settings = {
    'red':    {'name': 'SCS Shakhti',   'start': 0,   'duration': 100},
    'blue':   {'name': 'CS Ditwah', 'start': 50,  'duration': 100},
    'green':  {'name': 'SCS Montha',   'start': 120, 'duration': 100},
    'violet': {'name': 'CS Senyar',  'start': 180, 'duration': 100}
}

raw_tracks = {
    'red': [(475, 1592), (514, 1566), (547, 1562), (584, 1507), (628, 1475), (646, 1435),(668,1402),(547,1373),(670,1400),(549,1376),(676,1306),(772,1266),(800,1241),(802,1251),(987,1304),(982,1274),(1067,1205),(1120,1192),(1205,1273)],
    'blue': [(1544, 2119), (1640, 2129), (1708, 2014), (1656, 1948), (1661, 1728), (1544, 2119)],
    'green': [(2222, 1848), (2115, 1861), (1869, 1751), (1762, 1630), (1690, 1565), (1631, 1535)],
    'violet': [(3371, 1901), (3272, 1956), (3051, 2170), (2931, 2176), (2803, 2227), (2604, 2221)]
}
# =================================================

# Pre-calculate smooth paths for each storm based on their specific duration
smooth_tracks = {}
for color, pts in raw_tracks.items():
    duration = storm_settings[color]['duration']
    points = np.array(pts)
    t = np.linspace(0, 1, len(points))
    t_new = np.linspace(0, 1, duration)
    x_new = np.interp(t_new, t, points[:, 0])
    y_new = np.interp(t_new, t, points[:, 1])
    smooth_tracks[color] = list(zip(x_new, y_new))

bg = Image.open(BG_IMAGE)
w, h = bg.size
icon_raw = Image.open(ICON_IMAGE).convert("RGBA").resize((ICON_SIZE_PX, ICON_SIZE_PX))

fig, ax = plt.subplots(figsize=(15, 10))
ax.imshow(bg, extent=[0, w, h, 0], zorder=1)
ax.set_xlim(0, w)
ax.set_ylim(h, 0)
ax.axis('off')

# Containers
cyclone_images = {}
cyclone_labels = {}
cyclone_trails = {}

# Initialize all but keep them hidden (alpha=0 or visible=False)
for color in smooth_tracks:
    trail_line, = ax.plot([], [], color=color, linewidth=3, alpha=0.8, zorder=2)
    cyclone_trails[color] = trail_line
    
    # We initialize the icon off-screen or invisible
    cyclone_images[color] = ax.imshow(np.array(icon_raw), extent=[-200,-100,-200,-100], zorder=3)
    cyclone_images[color].set_visible(False)
    
    name = storm_settings[color]['name']
    cyclone_labels[color] = ax.text(0, 0, name, color='white', fontweight='bold', 
                                    visible=False, zorder=4,
                                    bbox=dict(facecolor='black', alpha=0.6, edgecolor='none'))

def update(frame):
    angle = (frame * -20) % 360
    rotated_icon = np.array(icon_raw.rotate(angle))
    updated_artists = []
    
    half = ICON_SIZE_PX / 2

    for color, path in smooth_tracks.items():
        start = storm_settings[color]['start']
        end = start + storm_settings[color]['duration']
        
        # LOGIC: If current frame is within this storm's window
        if start <= frame < end:
            idx = frame - start
            new_x, new_y = path[idx]
            
            # Make visible
            cyclone_images[color].set_visible(True)
            cyclone_labels[color].set_visible(True)
            
            # Update Position
            cyclone_images[color].set_extent([new_x - half, new_x + half, new_y + half, new_y - half])
            cyclone_images[color].set_data(rotated_icon)
            cyclone_labels[color].set_position((new_x, new_y - 70))
            
            # Update Trail
            history = np.array(path[:idx+1])
            cyclone_trails[color].set_data(history[:, 0], history[:, 1])
            
        # If the storm has finished its track, let's keep the trail but hide the icon
        elif frame >= end:
            cyclone_images[color].set_visible(False)
            cyclone_labels[color].set_visible(False)
            # The trail remains as a permanent record on the map
            
        updated_artists.extend([cyclone_trails[color], cyclone_images[color], cyclone_labels[color]])

    return updated_artists

print(f"Generating sequential animation ({TOTAL_FRAMES} frames)...")
ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000//FPS, blit=False)
ani.save(OUTPUT_NAME, writer='pillow', fps=FPS)
print(f"Success! Sequential GIF saved as {OUTPUT_NAME}")
