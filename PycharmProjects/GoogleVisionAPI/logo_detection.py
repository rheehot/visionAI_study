import os, io
from google.cloud import vision
from draw_vertice import drawVertices

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'[KEY.json]'
client = vision.ImageAnnotatorClient()

file_name = 'logos.png'
image_folder = './resources/'
image_path = os.path.join(image_folder, file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    print('Logo Description:', logo.description)
    print('Confidence Score:', logo.score)
    print('-' * 50)
    vertices = logo.bounding_poly.vertices
    print('Vertices Values {0}'.format(vertices))
    drawVertices(content, vertices, logo.description)
