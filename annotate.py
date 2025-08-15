import os
import csv

#  CONFIGURATION
class_map = {
    "Chickpea": 0,
    "Corn": 1,
    "Mustard": 2,
    "Pearl Millet": 3,
    "Rice": 4,
    "Wheat": 5,
    "Wheat": 6,
    "Wheat": 7,
    "Chickpea (Gram)": 8,
    "Soybean": 9,
    "Soybean": 10,
    "Soybean": 11,
    "Corn (Maize)": 12,
    "Soybean": 13,
    "Cotton": 14,
    "Corn (Maize)": 15
    "Corn (Maize)": 16
    "Rice": 17,
    "Rice": 18,
    "Cotton": 19,
    "Soybean": 20,
    "Pigeon Pea (Arhar)": 21,
    "Cowpea (Lobia)": 22,
    "Corn (Maize)": 23
}

# Default bounding box (centered, large area)
default_bbox = [0.5, 0.5, 0.8, 0.8]

# Input CSV-like data (can be replaced with file read)
raw_data = """
import os
import csv


# Default bounding box (centered, large area)
default_bbox = [0.5, 0.5, 0.8, 0.8]

# Input CSV-like data (can be replaced with file read)
raw_data =
"""
| 1 | Chickpea (Gram) | Pod development | Healthy | Green pods are visible and appear well-formed. |
| 2 | Corn (Maize) | Vegetative stage | Healthy | Plants are young, with good stand establishment and green foliage. |
| 3 | Mustard | Flowering | Healthy | Plants are in full bloom with yellow flowers, Chickpea (Gram) good growth. |
| 4 | Pearl Millet | Reproductive/Grain filling | Healthy | Ear heads are developing and appear healthy, with seeds filling out. |
| 5 | Rice | Tillering/Panicle initiation | Healthy | Plants are green and have a good number of tillers. Some panicles might be initiating. |
| 6 | Wheat | Late vegetative/Early reproductive | Diseased | Symptoms of leaf spot or rust are evident, with yellowing and browning lesions on leaves. |
| 7 | Wheat | Reproductive (ear formation) | Healthy | Plants are well-developed with clear ear heads emerging. |
| 8 | Wheat | Reproductive (with disease) | Diseased | Severe infestation of rust (likely stripe or stem rust) is visible, characterized by orange-yellow pustules on stems and leaves. |
| 9 | Chickpea (Gram) | Pod development | Healthy | Plants appear to be at the pod development stage, with good canopy cover. |
| 10 | Soybean | Vegetative | Healthy | Young soybean plants are established in rows with good green foliage. |
| 11 | Soybean | Vegetative | Healthy | Dense canopy of healthy soybean plants. |
| 12 | Soybean | Early vegetative | Stressed | Plants are small and appear to be struggling, with some wilting or dieback. Potentially due to poor establishment or environmental stress. |
| 13 | Corn (Maize) | Vegetative stage | Healthy | Young corn plants with good growth and green color. |
| 14 | Soybean | Vegetative | Healthy | Dense, uniform stand of healthy soybean plants. |
| 15 | Cotton | Vegetative/Flowering initiation | Healthy | Cotton plants show good vegetative growth and early flower buds are visible. |
| 16 | Corn (Maize) | Vegetative stage | Damaged | Leaf damage is evident, possibly due to insect feeding or mechanical injury. |
| 17 | Corn (Maize) | Vegetative stage | Healthy | Young corn plants are growing well in rows. |
| 18 | Rice | Seedling/Early vegetative | Healthy | Rice seedlings are established in a flooded paddy with a green algae bloom present. |
| 19 | Rice | Vegetative/Panicle initiation | Healthy | Rice plants are robust and green, with signs of early panicle development. |
| 20 | Cotton | Flowering | Healthy | A cotton flower is shown, indicating progression to the reproductive stage. The surrounding foliage is healthy. |
| 21 | Soybean | Vegetative | Healthy | A field of healthy, well-established soybean plants. |
| 22 | Pigeon Pea (Arhar) | Flowering/Pod development | Healthy | The plants are tall and bushy, with flowers and developing pods visible. |
| 23 | Cowpea (Lobia) | Vegetative | Healthy | Young cowpea plants are establishing well in rows. |
| 24 | Corn (Maize) | Early vegetative | Healthy | Young corn plants with good stand and growth. |
"""

# 🧼 Parse and clean data
def parse_data(raw_text):
    lines = raw_text.strip().split('\n')
    parsed = []
    for line in lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 2:
            crop_name = parts[1].split('(')[0].strip()  # Remove bracketed synonyms
            parsed.append((parts[0], crop_name))
    return parsed

# 📝 Generate YOLO annotation files
def generate_annotations(parsed_data, output_dir="labels/train"):
    os.makedirs(output_dir, exist_ok=True)
    for idx, crop_name in parsed_data:
        class_id = class_map.get(crop_name)
        if class_id is None:
            print(f"⚠️ Unknown crop: {crop_name}")
            continue
        filename = f"{crop_name.lower().replace(' ', '_')}_{idx}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(f"{class_id} {' '.join(map(str, default_bbox))}\n")
        print(f"✅ Created: {filepath}")

# 🚀 Run the pipeline
if __name__ == "__main__":
    parsed = parse_data(raw_data)
    generate_annotations(parsed)"""

# 🧼 Parse and clean data
def parse_data(raw_text):
    lines = raw_text.strip().split('\n')
    parsed = []
    for line in lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 2:
            crop_name = parts[1].split('(')[0].strip()  # Remove bracketed synonyms
            parsed.append((parts[0], crop_name))
    return parsed

# 📝 Generate YOLO annotation files
def generate_annotations(parsed_data, output_dir="labels/train"):
    os.makedirs(output_dir, exist_ok=True)
    for idx, crop_name in parsed_data:
        class_id = class_map.get(crop_name)
        if class_id is None:
            print(f"⚠️ Unknown crop: {crop_name}")
            continue
        filename = f"{crop_name.lower().replace(' ', '_')}_{idx}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(f"{class_id} {' '.join(map(str, default_bbox))}\n")
        print(f"✅ Created: {filepath}")

# 🚀 Run the pipeline
if __name__ == "__main__":
    parsed = parse_data(raw_data)
    generate_annotations(parsed)