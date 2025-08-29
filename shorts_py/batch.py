import os
import shutil

# Source paths
IMAGE_DIR = "G:\\My Drive\\DRONE_Images_dataset\\tiled_dataset\\images"

LABEL_DIR = "G:\\My Drive\\DRONE_Images_dataset\\tiled_dataset\\labels"

# Destination root
DEST_ROOT = "G:\\My Drive\\DRONE_Images_dataset\\tiled_batches"
os.makedirs(DEST_ROOT, exist_ok=True)

# List all image files
all_images = sorted([f for f in os.listdir(IMAGE_DIR) if f.endswith(".jpg")])
batch_size = 2500  # number of image-label pairs per batch

for i in range(0, len(all_images), batch_size):
    batch_num = i // batch_size + 1
    batch_folder = os.path.join(DEST_ROOT, f"batch{batch_num}")
    img_out = os.path.join(batch_folder, "images")
    lbl_out = os.path.join(batch_folder, "labels")
    os.makedirs(img_out, exist_ok=True)
    os.makedirs(lbl_out, exist_ok=True)

    for fname in all_images[i:i+batch_size]:
        # Copy image
        shutil.copy(os.path.join(IMAGE_DIR, fname), os.path.join(img_out, fname))
        # Copy matching label
        label_name = fname.replace(".jpg", ".txt")
        label_path = os.path.join(LABEL_DIR, label_name)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(lbl_out, label_name))

    print(f"created batch{batch_num} with {len(all_images[i:i+batch_size])} files")

