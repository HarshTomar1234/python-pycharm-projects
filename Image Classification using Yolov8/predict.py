from ultralytics import YOLO

import numpy as np


model = YOLO('C:/Users/Harsh/runs/classify/train3/weights/last.pt')  # load a custom model

results = model('C:/Users/Harsh/Downloads/dawid-zawila--G3rw6Y02D0-unsplash.jpg')  # predict on an image



names_dict = results[0].names

probs = results[0].probs.data.tolist()

print(names_dict)
print(probs)

print(names_dict[np.argmax(probs)])