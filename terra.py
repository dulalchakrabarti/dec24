from owslib.wms import WebMapService
from PIL import Image
# Connect to GIBS WMS Service
wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

# Configure request for MODIS_Terra_CorrectedReflectance_TrueColor
img = wms.getmap(layers=['MODIS_Terra_CorrectedReflectance_TrueColor'],  # Layers
                 srs='epsg:4326',  # Map projection
                 bbox=(40,0,110,40),  # Bounds
                 size=(7200, 6000),  # Image size
                 time='2024-12-07',  # Time of data
                 format='image/tiff',  # Image format
                 transparent=True)  # Nodata transparency

# Save output tif to a file
out = open('terra.tif', 'wb')
out.write(img.read())
# View image
out.close()
print('Downloaded terra.tif....'
