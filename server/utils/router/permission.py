from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/updateselfpermission', methods=['GET', 'POST'])
def update_self_permission():
    data = json.loads(request.get_data(as_text=True))

    username, stu_uuid, tp = data['username'], data['stu_uuid'], data['tp']
    book = Book()
    ret_info = book.update_masterpermission(username, stu_uuid, tp)
    app.logger.info(f"{username} update its self permission")

    return jsonify(
        RetCode=0,
        Message='Successfully update permissions'
    )