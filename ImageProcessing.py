import app
import base64


def convert_to_image(image, received_data):
    with open(image, "wb") as fh:
        fh.write(base64.decodebytes(received_data['image'].encode()))

