import os
import cv2

input_folder = "C:\\Users\\satya\\OneDrive\\Desktop\\keerthana\\DL_APSAC\\ds\\DATASET"       # Folder where your original 504 images are
output_folder = "resized_images"  # Folder to save resized versions
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, file)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to read {file}")
            continue
        resized = cv2.resize(img, (2048, 1536))  # You can change this size if needed
        save_path = os.path.join(output_folder, file)
        cv2.imwrite(save_path, resized)

print("✅ All images resized and saved to 'resized_images' folder.")
