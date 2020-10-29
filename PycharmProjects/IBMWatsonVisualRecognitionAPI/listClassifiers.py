import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('[IAMAuthenticator_key]')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url('[server_url]')


classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
print(json.dumps(classifiers, indent=2))