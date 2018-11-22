from flask import Flask, request, json, render_template
from ImageProcessing import *
from ImageModification import get_result
import time
from flask_cors import cross_origin, CORS



__author__ = "avinash"
app = Flask(__name__, static_url_path='', static_folder='templates')
CORS(app)


@cross_origin()
@app.route("/test", methods=['GET', 'POST'])
def process():
    data = request.get_json(force=True)
    print("hit")
    time_stamp = time.strftime("%Y%m%d-%H%M%S")
    image_name = "./images/" + time_stamp + ".jpg"
    convert_to_image(image_name, data)
    print("converted")
    # percentage = modify_image(image_name)
    res = get_result(image_name)
    output = {'result': res}
    # pres = modify_image()
    response = app.response_class(response=json.dumps(output), status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003, debug=True)
