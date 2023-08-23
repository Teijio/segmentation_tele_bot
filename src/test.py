import numpy as np
from ultralytics import YOLO
from PIL import Image
from rembg import remove
from ultralytics import settings

# Update a setting
settings.update({"runs_dir": "."})

# Update multiple settings
# settings.update({'runs_dir': '/path/to/runs', 'tensorboard': False})

# Reset settings to default values
# settings.reset()

model = YOLO("yolov8n-seg.pt")

# model = YOLO("best.pt")

src = "./images/image.jpg"
results = model.predict(src, name="", save=True)
for result in results:

    detection_count = result.boxes.shape[0]

for i in range(detection_count):
    cls = int(result.boxes.cls[i].item())
    name = result.names[cls]
    confidence = float(result.boxes.conf[i].item())
    bounding_box = result.boxes.xyxy[i].cpu().numpy()
    print(name, confidence, bounding_box)

# result = results[0]
# output = []
# for box in result.boxes:
#     x1, y1, x2, y2 = [round(x) for x in box.xyxy[0].tolist()]
#     class_id = box.cls[0].item()
#     prob = round(box.conf[0].item(), 2)
#     output.append([result.names[class_id], prob])
# print(output)


# names = result.boxes.cls
# res = []
# for i in range(len(names)):
#     name1 = names[i]
#     name_class = model.names[int(name1)]
#     res.append((name_class, i))
# print(res)


