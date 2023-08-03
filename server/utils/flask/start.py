from flask import jsonify
from utils.flask.app import app

@app.errorhandler(404)
def handler_404_error(err):
    resData = {
        "resCode": 404,
        "data": [],
        "message": err
    }
    return jsonify(resData)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    arrData = "Please do not hack this database."
    return jsonify(
        exception=arrData
    )

from utils.router import *

def quick_start(mode: str='dev'):
    if mode in ['dev', 'develop', 'development']:
        host, port = '127.0.0.1', 1943
    elif mode in ['product', 'production']:
        host, port = '0.0.0.0', 8890
    else:
        raise Exception(f"Invalid Mode {mode}")

    return app.run(host=host, port=port, debug=True)    