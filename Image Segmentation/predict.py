from ultralytics import YOLO
import cv2

model_path = 'C:/Users/Harsh/runs/segment/train3/weights/last.pt'
image_path = 'C:/Users/Harsh/OneDrive/Documents/Desktop/Image Segmentation Yolov8/data/images/train/duck_07.jpg'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

# Check if results contain masks
if results[0].masks is not None:
    for result in results:
        for j, mask in enumerate(result.masks.data):
            mask = mask.numpy() * 255
            mask = cv2.resize(mask, (W, H))
            cv2.imwrite('./output.png', mask)
else:
    print("No masks found in the results.")
