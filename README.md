# Crack Detection using Tiling, Roboflow API, and NMS

This project implements **automated crack detection** in high-resolution drone or structural 
images using **image tiling**, **Roboflow model inference**, and **Non-Maximum Suppression (NMS)** to accurately localize and visualize cracks.

---

## Features

-  Image **tiling** to handle large-resolution inputs
-  Inference using **Roboflow-hosted YOLO model**
-  Smart **Non-Maximum Suppression (NMS)** to merge overlapping boxes
-  OpenCV-based **visualization** with bounding boxes and coordinates
-  Saves final output with annotations and optionally prints box coordinates

---
<h2>Requirements</h2> <p>Install dependencies using <code>pip install -r requirements.txt</code></p> <pre><code>opencv-python numpy requests </code></pre> <h2>File Structure</h2> <pre><code>. ├── crack_detection.py # Main script: tiling, inference, NMS ├── utils.py # (Optional) helper functions (tiling, NMS) ├── image.jpg # Your input image └── output.jpg # Saved result after detection </code></pre> <h2>Configuration</h2> <p>Edit these inside <code>crack_detection.py</code>:</p> <pre><code>api_key = "YOUR_ROBOFLOW_API_KEY" project_url = "https://infer.roboflow.com/YOUR_PROJECT" image_path = "path/to/your/image.jpg" tile_size = 640 # Adjust based on model input overlap = 0.2 # For tile overlap </code></pre> <h2>How It Works</h2> <ol> <li> <strong>Tile the Image</strong> <p>Large image is split into overlapping <code>tile_size × tile_size</code> chunks.</p> </li> <li> <strong>Run Inference</strong> <p>Each tile is passed to Roboflow model API for detection.</p> </li> <li> <strong>Merge Predictions</strong> <p>All tile predictions are re-scaled and stitched back.</p> </li> <li> <strong>Apply NMS</strong> <p>Suppresses overlapping boxes to keep only the best ones.</p> </li> <li> <strong>Visualize &amp; Save</strong> <p>Final image is saved with bounding boxes and labels.</p> </li> </ol> <hr> <h2>Acknowledgments</h2> <ul> <li>Roboflow for model hosting</li> <li>YOLO architecture for detection</li> <li>OpenCV and NumPy for processing</li> </ul>

CHANGE THIS AND GIVE IN SAME HTML TAGS BUT DIFFERENT TEXTS
