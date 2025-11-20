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

## Requirements

Install all dependencies:

```
pip install -r requirements.txt
```

<pre>
opencv-python
numpy
requests
tqdm
Pillow
</pre>

## File Structure

<pre>
.
├── crack_detection.py        # Main script: tiling, inference, NMS
├── utils.py                  # Helper functions (tiling, stitching, NMS)
├── requirements.txt          # Dependency list
├── assets/
│   ├── input.jpg             # Input image for detection
│   └── samples/              # Additional test images
├── outputs/
│   └── result.jpg            # Output with drawn detections
└── README.md                 # Documentation
</pre>
