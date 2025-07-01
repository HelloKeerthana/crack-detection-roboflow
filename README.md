# 🧠 Crack Detection using Tiling, Roboflow API, and NMS

This project implements **automated crack detection** in high-resolution drone or structural 
images using **image tiling**, **Roboflow model inference**, and **Non-Maximum Suppression (NMS)** to accurately localize and visualize cracks.

---

## 📌 Features

- ✅ Image **tiling** to handle large-resolution inputs
- ✅ Inference using **Roboflow-hosted YOLO model**
- ✅ Smart **Non-Maximum Suppression (NMS)** to merge overlapping boxes
- ✅ OpenCV-based **visualization** with bounding boxes and coordinates
- ✅ Saves final output with annotations and optionally prints box coordinates

---

## 🧰 Requirements

Install dependencies using `pip install -r requirements.txt`

opencv-python
numpy
requests
📂 File Structure
.
├── crack_detection.py        # Main script: tiling, inference, NMS
├── utils.py                  # (Optional) helper functions (tiling, NMS)
├── image.jpg                 # Your input image
└── output.jpg                # Saved result after detection
⚙️ Configuration
Edit these inside crack_detection.py:

api_key = "YOUR_ROBOFLOW_API_KEY"
project_url = "https://infer.roboflow.com/YOUR_PROJECT"
image_path = "path/to/your/image.jpg"
tile_size = 640  # Adjust based on model input
overlap = 0.2    # For tile overlap
🚀 How It Works
Tile the Image
Large image is split into overlapping tile_size × tile_size chunks.

Run Inference
Each tile is passed to Roboflow model API for detection.

Merge Predictions
All tile predictions are re-scaled and stitched back.

Apply NMS
Suppresses overlapping boxes to keep only the best ones.

Visualize & Save
Final image is saved with bounding boxes and labels.

🖼️ Example Output

🧪 Sample Command

python crack_detection.py
📈 Next Improvements (TODO)
 Add GUI for image upload and preview

 Batch process folder of images

 Add support for local model inference (YOLOv5)

🤝 Acknowledgments
Roboflow for model hosting

YOLO architecture for detection

OpenCV and NumPy for processing

📬 Contact
For queries or improvements, reach out to Keerthana ✨

Let me know if you want a version that supports webcam feed or video too — or want to add CLI arguments
