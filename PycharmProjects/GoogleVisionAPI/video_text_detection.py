import io
import os
import cv2
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
#from google.cloud.vision import types  #pip install google-cloud-vision == 1.0.0

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'[KEY.json]'
# Instantiates a client
client = vision.ImageAnnotatorClient()

file_name = 'logos.png'
image_folder = './resources/'
image_path = os.path.join(image_folder, file_name)

def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    #image = types.Image(content=content) #pip install google-cloud-vision == 1.0.0
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    file = 'live.png'
    cv2.imwrite( file,frame)

    # print OCR text
    print(detect_text(file))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
