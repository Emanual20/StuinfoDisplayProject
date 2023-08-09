from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/checknamepw', methods=['GET', 'POST'])
def check_namepw():
    data = json.loads(request.get_data(as_text=True))
    checklist = ['username', 'password']
    for key in checklist:
        if key not in data.keys():
            app.logger.warning(f'no {key} in data, fxxk!')
            return jsonify(
                RetCode=1,
                Message=f'failed because no {key}'
            )

    book = Book()
    nusername, npassword = data['username'], data['password']
    res_nuserinfo = book.get_user_password(nusername, npassword)
    app.logger.info(f"{nusername} request login matching record: {res_nuserinfo}")
    flag = res_nuserinfo is None
    message_suffix = "failed" if flag else "successful"
    return jsonify(
        RetCode=int(flag),
        data=[res_nuserinfo],
        Message=f"Password verified {message_suffix}."
    )

@app.route('/updatepassword', methods=['GET', 'POST'])
def update_password():
    data = json.loads(request.get_data(as_text=True))
    checklist = ['username', 'npassword']
    for key in checklist:
        if key not in data.keys():
            app.logger.warning(f'no {key} in data, fxxk!')
            return jsonify(
                RetCode=1,
                Message=f'failed because no {key} in data'
            )
        
    username, new_password = data['username'], data['npassword']
    app.logger.info(f"{username} update its password")
    book = Book()
    RetCode = book.update_userpassword(username, new_password)
    return jsonify(
        RetCode=0,
        Message='successful update your password, please login again..!'
    )