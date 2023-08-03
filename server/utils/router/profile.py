from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/fetchselfinfo', methods=['GET', 'POST'])
def fetch_self_info():
    data = json.loads(request.get_data(as_text=True))
    if 'stu_uuid' not in data.keys():
        print('no username in data, fxxk!')
        return jsonify(
            RetCode=1,
            Message='failed because no uuid'
        )
    book = Book()
    self_infos = book.get_stu_selfinfo(data['stu_uuid'])
    return jsonify(
        RetCode=0,
        data=self_infos,
        Message='successfully fetch selfinfo'
    )


@app.route('/updatebachelorinfo', methods=['GET', 'POST'])
def update_bachelorinfo():
    data = json.loads(request.get_data(as_text=True))

    checklist = ['username', 'infos']
    for key in checklist:
        if key not in data.keys():
            print(f'no {key} in data, fxxk!')
            return jsonify(
                RetCode=1,
                Message=f'failed because no {key}'
            )
        
    username, infos = data['username'], data['infos']
    print(f"{username} update its bachelor info")

    book = Book()
    book.update_bachelordest(username, infos)
    return jsonify(
        RetCode=0,
        Message='update successfully'
    )


@app.route('/updatemasterinfo', methods=['GET', 'POST'])
def update_masterinfo():
    data = json.loads(request.get_data(as_text=True))

    checklist = ['username', 'infos']
    for key in checklist:
        if key not in data.keys():
            print(f'no {key} in data, fxxk!')
            return jsonify(
                RetCode=1,
                Message=f'failed because no {key}'
            )
        
    username, infos = data['username'], data['infos']
    print(username, " update its master info")

    infos = data['infos']
    book = Book()
    res = book.update_masterdest(username, infos)
    return jsonify(
        RetCode=0,
        Message='update successfully'
    )