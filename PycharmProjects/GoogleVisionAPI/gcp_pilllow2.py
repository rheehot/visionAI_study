from google.cloud import vision
import io,os
from PIL import Image, ImageDraw

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'[KEY.json]'

client = vision.ImageAnnotatorClient()

# image_path = 'image_4.jpg'
image_path = 'resources/twice_1.jpg'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# image = vision.types.Image(content=content)  #pip install google-cloud-vision == 1.0.0
image = vision.Image(content=content)

print(type(image))
response = client.face_detection(image=image)
faces = response.face_annotations

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')
print('Faces:')

im = Image.open(image_path)
imgWidth, imgHeight = im.size

draw = ImageDraw.Draw(im)

# calculate and display bounding boxes for each detected face
for face in faces:
    points = []
    for vertex in face.bounding_poly.vertices:
        points.append((vertex.x, vertex.y))
    points.append(points[0])
    vertices = tuple(points)
    draw.line(vertices, fill='#00d400', width=6)

im.show()
