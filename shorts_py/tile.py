import os
import cv2

INPUT_DIR = r"C:\Users\satya\OneDrive\Desktop\keerthana\DL_APSAC\ds\DATASET"
OUTPUT_DIR = r"C:\Users\satya\OneDrive\Desktop\keerthana\DL_APSAC\ds\tiled_dataset"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Tiling parameters
TILE_SIZE = 640
OVERLAP = 0
STEP = TILE_SIZE - OVERLAP

# Tile each image
for fname in os.listdir(INPUT_DIR):
    if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(INPUT_DIR, fname)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Couldn't read {fname}")
            continue

        h, w = img.shape[:2]
        base = os.path.splitext(fname)[0]

        count = 0
        for y in range(0, h - TILE_SIZE + 1, STEP):
            for x in range(0, w - TILE_SIZE + 1, STEP):
                tile = img[y:y + TILE_SIZE, x:x + TILE_SIZE]
                tile_name = f"{base}_tile_{count}.jpg"
                tile_path = os.path.join(OUTPUT_DIR, tile_name)
                cv2.imwrite(tile_path, tile)
                count += 1

        print(f"Tiled {fname} into {count} patches.")

