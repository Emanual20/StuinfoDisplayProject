from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/user_stuinfos', methods=['GET', 'POST'])
def get_specific_stuinfos(stu_uuid):
    book = Book()
    sql_data = book.get_stu_infos(stu_uuid)
    resData = {
        "resCode": 0, 
        "data": sql_data,
        "message": "request successful" 
    }
    return jsonify(resData)


@app.route('/get_stuinfos', methods=['GET', 'POST'])
def get_all_stuinfos():
    book = Book()
    res = book.get_allstu_infos()
    resData = {
        "resCode": 0,
        "data": res,
        "message": 'Successful get all student infos'
    }
    return jsonify(resData)

@app.route('/fetchadmittedinfo', methods=['GET', 'POST'])
def fetch_admitted_info():
    data = json.loads(request.get_data(as_text=True))
    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)
    book = Book()
    nusername = data['username']
    print(nusername, "request all the admitted info he can check")
    res_highinfo = book.get_stu_highinfos(nusername)
    res_bachelor = book.get_bachelor_infos(res_highinfo)
    res_admitted = book.get_stu_admittedinfos(nusername, res_highinfo)
    res_forbidden = book.get_stu_forbiddeninfos(nusername, res_highinfo)
    res_stunameinfo = book.get_uuid2stuname()
    stuname2info = {}
    for each in res_stunameinfo:
        stuname2info[each['stu_uuid']] = each['stu_nickname']
    for each in res_bachelor:
        each['stu_name'] = stuname2info[each['stu_uuid']]
    for each in res_admitted:
        for key in ['stu_city', 'stu_dest', 'stu_mastermajor', 'stu_direction']:
            if each[key] is None: each[key] = 'UnKnown'
        each['stu_name'] = stuname2info[each['stu_uuid']]
    for each in res_forbidden:
        for key in ['stu_city', 'stu_dest', 'stu_mastermajor', 'stu_direction']:
            if each[key] is None: each[key] = 'UnKnown'
        each['stu_name'] = '[CLS]'

    return jsonify(
        RetCode=0,
        data=[res_bachelor, res_admitted, res_forbidden],
        Message='Successfully fetch admitted data..'
    )

@app.route('/fetchmapinfo', methods=['GET', 'POST'])
def fetch_map_info():
    data = json.loads(request.get_data(as_text=True))
    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)
    book = Book()
    nusername = data['username']
    print(nusername, "request all the map info")
    res_highinfo = book.get_stu_highinfos(nusername)
    res_bachelor = book.get_bachelor_infos(res_highinfo)

    ret_pos_lis = []
    for each in res_bachelor:
        xpos, ypos = each['stu_bachelorxpos'], each['stu_bachelorypos']
        if xpos is not None and ypos is not None:
            ret_pos_lis.append([xpos, ypos])

    return jsonify(
        RetCode=0,
        data=[ret_pos_lis],
        Message='Successfully fetch admitted data..'
    )