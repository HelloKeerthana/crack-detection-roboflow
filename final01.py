import cv2
import numpy as np
import requests

# ---- Configuration ----
image_path = "image.png"
tile_size = 640
overlap = 0.2
api_key = "***************"
model_id = "*********************"
confidence_threshold = 0.3
nms_iou_threshold = 0.4

# ---- Load Image ----
image = cv2.imread(image_path)
height, width, _ = image.shape

# ---- Tile the image ----
stride = int(tile_size * (1 - overlap))
tiles = []

for y in range(0, height, stride):
    for x in range(0, width, stride):
        x_end = min(x + tile_size, width)
        y_end = min(y + tile_size, height)
        tile = image[y:y_end, x:x_end]
        tiles.append(((x, y), tile))

# ---- Inference Function ----
def infer_tile(tile_img):
    _, img_encoded = cv2.imencode(".jpg", tile_img)
    try:
        response = requests.post(
            f"https://detect.roboflow.com/{model_id}?api_key={api_key}&confidence={confidence_threshold}",
            files={"file": img_encoded.tobytes()}
        )
        if response.status_code != 200:
            print("Error:", response.text)
            return []
        return response.json().get("predictions", [])
    except Exception as e:
        print("Request failed:", e)
        return []

# ---- Run Inference on Tiles ----
all_boxes = []

for (x_offset, y_offset), tile_img in tiles:
    preds = infer_tile(tile_img)
    for pred in preds:
        x1 = int(pred['x'] - pred['width'] / 2) + x_offset
        y1 = int(pred['y'] - pred['height'] / 2) + y_offset
        x2 = int(pred['x'] + pred['width'] / 2) + x_offset
        y2 = int(pred['y'] + pred['height'] / 2) + y_offset
        conf = pred['confidence']
        all_boxes.append([x1, y1, x2, y2, conf])

# ---- Apply NMS ----
if len(all_boxes) == 0:
    print("No detections found.")
    exit()

boxes_np = np.array(all_boxes)
boxes = boxes_np[:, :4].astype(int)
scores = boxes_np[:, 4].astype(float)
indices = cv2.dnn.NMSBoxes(
    bboxes=boxes.tolist(),
    scores=scores.tolist(),
    score_threshold=confidence_threshold,
    nms_threshold=nms_iou_threshold
)

# ---- Draw Final Boxes ----
final_image = image.copy()
final_boxes = []

print("\nFinal Detections (after NMS):")
for i in indices:
    i = i[0] if isinstance(i, (list, np.ndarray)) else i
    x1, y1, x2, y2 = boxes[i]
    final_boxes.append((x1, y1, x2, y2))
    print(f"Box: ({x1}, {y1}), ({x2}, {y2})")

    # Draw thick, dark (black) bounding boxes
    cv2.rectangle(final_image, (x1, y1), (x2, y2), (0, 0, 0), thickness=10)

# ---- Save Output ----
output_path = "imageop.png"
cv2.imwrite(output_path, final_image)   
print(f" Saved result to: {output_path}")   
