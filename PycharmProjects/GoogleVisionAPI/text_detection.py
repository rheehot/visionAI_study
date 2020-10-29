import io
import os
from google.cloud import vision
# from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'[KEY.json]'

# Instantiates a client
client = vision.ImageAnnotatorClient()

file_name = os.path.join(os.path.dirname(__file__), 'resources/GNC_big_1_9.jpg')
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.text_detection(image=image)
textAnnotations = response.text_annotations

print('Faces:')
for textAnnotations in textAnnotations:
    print(textAnnotations)
