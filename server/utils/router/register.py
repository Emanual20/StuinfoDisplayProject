from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/registernewuser', methods=['GET', 'POST'])
def register_newuser():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    checklist = ['emailaddress', 'username', 'password']
    for key in checklist:
        if key not in data.keys():
            print(f'no {key} in data, fxxk!')
            return jsonify(
                RetCode=1,
                Message=f'failed because no {key}'
            )

    # check if emailaddress already exists
    emailaddress = data['emailaddress']
    res_matchusername = book.get_matchemail(emailaddress)
    if res_matchusername is not None:
        print(f"In register_newuser: Email already exists {emailaddress}")
        return jsonify(
            RetCode=1,
            Message=f'Email already exists {emailaddress}'             
        )

    # check if hightutor matches
    highbatch, highclass, hightutor = data['highbatch'], data['highclass'], data['hightutor']
    MatchItems = book.check_hctutor(
        hc=highclass,
        hb=highbatch,
        hctutor=hightutor
    )
    if MatchItems is None:
        print(f"In register_newuser: Mismatch ({highbatch}, {highclass}, {hightutor})")
        return jsonify(
            RetCode=1,
            Message=f'Mismatch hightutor'             
        )

    username, password = data['username'], data['password']
    retCode = book.insert_stuifonewuser(emailaddress, username, password, highclass, highbatch)
    return jsonify(
        RetCode=retCode,
        Message='Successfully register a new account.'
    )

@app.route('/deleteuseraccount', methods=['GET', 'POST'])
def delete_account():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    uuid = data['stu_uuid']
    try:
        RetCode = book.delete_user(uuid)
        Message = 'Successfully delete an account.'
    except:
        RetCode = -1
        Message = 'Delete account failed.'

    return jsonify(
        RetCode=RetCode,
        Message=Message
    )    