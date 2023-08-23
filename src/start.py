import numpy as np

from ultralytics import YOLO
from PIL import Image
from ultralytics import settings

settings.update({"runs_dir": "."})

model = YOLO("yolov8n-seg.pt")


def get_names(source):
    results = model.predict(source, save=True)
    result = results[0]
    output = []
    c = 0
    for box in result.boxes:
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
            result.names[class_id], prob, c
        ])
        c += 1
    return output


def delete_bg(source, name_id):
    results = model.predict(source)
    result = results[0]
    masks = result.masks
    mask1 = masks[name_id]
    mask = mask1.data[0].numpy()
    original_image = Image.open(source)
    original_image_resized = original_image.resize(
        mask.shape[::-1], Image.NEAREST
    )
    mask_bool = mask > 0
    object_image_np = np.array(original_image_resized)
    object_image_np[~mask_bool] = 0

    alpha_channel = np.full(object_image_np.shape[:2], 255, dtype=np.uint8)
    alpha_channel[~mask_bool] = 0

    object_image_rgba = np.dstack((object_image_np, alpha_channel))

    object_image = Image.fromarray(object_image_rgba, "RGBA")
    object_image.save("./images/seg_image.png")

