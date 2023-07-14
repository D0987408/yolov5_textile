import torch

model = torch.hub.load("ultralytics/yolov5","yolov5s")

img="scissor.jpg"

results=model(img)

results.print()

results.show()
