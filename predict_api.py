from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from PIL import Image

app = FastAPI()

@app.get("/")
async def test_connection():
    return {"Hello": "Hello"}


@app.post("/get_prediction")
async def predict_sentiment(file: UploadFile = File(...)): 
    img = Image.open(file.file)
    img.save('temp.png')

    if os.path.exists('yolov5/runs/detect/exp'):
        os.system('rm -rf yolov5/runs/detect/exp')

    os.system('python yolov5/detect.py --weights yolo5mweights1.pt --source temp.png --save-txt')
    
    with open('yolov5/runs/detect/exp/labels/temp.txt') as f:
        lines = f.readlines()
    labels = list(map(lambda x: x[0], lines))
    labels_count = {'count': str(labels.count('0')) +',' + str(labels.count('1')) + ',' + str(labels.count('2'))
                }
    print(labels_count)
    # labels_count = {'test':'test'}

    return FileResponse("yolov5/runs/detect/exp/temp.png", headers = labels_count, media_type="image/png")

