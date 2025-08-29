import os
import pandas as pd

base_dir = r"C:\Users\satya\OneDrive\Desktop\keerthana\DL_APSAC\Crack Detection.v1i.yolov8"

splits = ['train', 'valid', 'test']
rows = []

for split in splits:
    labels_dir = os.path.join(base_dir, split, "labels")

    if not os.path.exists(labels_dir):
        print(f" :( not found: {labels_dir}")
        continue

    for file in os.listdir(labels_dir):
        if file.endswith(".txt"):
            label_path = os.path.join(labels_dir, file)
            image_name = file.replace(".txt", ".jpg")

            with open(label_path, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        cls, x_center, y_center, width, height = parts
                        rows.append({
                            'split': split,
                            'image': image_name,
                            'class': int(cls),
                            'x_center': float(x_center),
                            'y_center': float(y_center),
                            'width': float(width),
                            'height': float(height)
                        })

# Convert to DataFrame and save
df = pd.DataFrame(rows)
df.to_csv("combined_labels.csv", index=False)
print("combined_labels.csv created with", len(df), "annotations.")

