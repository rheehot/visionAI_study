import os, io
from google.cloud import vision
from matplotlib import pyplot as plt
from matplotlib import patches as pch

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'[KEY.json]'

client = vision.ImageAnnotatorClient()

# file_name = 'len_std.jpg'
# image_path = f'./resources/len_std.jpg'

f = 'resources/twice_1.jpg'
with io.open(f, 'rb') as image:
    content = image.read()

# with io.open(image_path, 'rb') as image_file:
#     content = image_file.read()

image = vision.Image(content=content)
response = client.face_detection(image=image)
faceAnnotations = response.face_annotations

print('faceAnnotations:')
# for face in faceAnnotations:
#     print(faceAnnotations);

possibility = ('Unknown', 'Very Unlikely', 'Unlikely', 'Possibly', 'Likely', 'Very Likely')

a = plt.imread(f)
fig, ax = plt.subplots(1)
ax.imshow(a)

for face in faceAnnotations:
    print('Possibility of anger: {}'.format(possibility[face.anger_likelihood]))
    print('Possibility of joy: {}'.format(possibility[face.joy_likelihood]))
    print('Possibility of surprise: {}'.format(possibility[face.surprise_likelihood]))
    print('Possibility of sorrow: {}'.format(possibility[face.sorrow_likelihood]))

    vertices = ([(vertex.x, vertex.y)
                 for vertex in face.bounding_poly.vertices])

    print('Vertices covering face: {}\n\n'.format(vertices))

    rect = pch.Rectangle(vertices[0], (vertices[1][0] - vertices[0][0]),
                         (vertices[2][1] - vertices[0][1]), linewidth=1,
                         edgecolor='r', facecolor='none')
    ax.add_patch(rect)

print('Confidence in Detection: {}%'.format(
    face.detection_confidence * 100))

plt.show()
