from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


import io
import torchvision.transforms as transforms 
from PIL import Image

def transfrom_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225]
        )])
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return my_transforms(image).unsqueeze(0)

with open('./_static/img/sample.png', 'rb') as f:
    image_bytes = f.read()
    tensor = transfrom_image(image_bytes=image_bytes)
    print(tensor)