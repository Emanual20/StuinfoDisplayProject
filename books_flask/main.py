from flask import Flask, jsonify, request
from books import Book
import json
from settings import BOOK_LIST, RSA_1024_PRIV_KEY, REQUSET_LISTS, TITLES
import re
import rsa
import base64
import time
import random

"""
接口说明：
1.返回的是json数据
2.结构如下
{
    resCode： 0, # 非0即错误 1
    data： # 数据位置，一般为数组
    message： '对本次请求的说明'
}
"""


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,Accept,Origin,Referer,User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.after_request(after_request)


# 检查是否含有特殊字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        # 说明合法
        return False
    else:
        # 不合法
        return True


# 解密函数
def get_secret_key(cryptdata):
    # print("cryptdata = ", cryptdata)
    privkey = rsa.PrivateKey.load_pkcs1(RSA_1024_PRIV_KEY)
    msg = rsa.decrypt(base64.b64decode(cryptdata), privkey)
    # msg = rsa.decrypt(base64.b64decode(cryptdata), RSA_1024_PRIV_KEY)
    # print("str(msg) = ", msg)
    # print("str(msg) = ", msg.decode().split(":")[1])
    try:
        result = {
            "request_time":msg.decode().split(":")[0],  # 防止爬虫利用这个反复爬取
            "request_url":msg.decode().split(":")[1],
            "request_infos": msg.decode().split(":")[2]
        }
    except:
        result = {
            "request_time":'',  # 防止爬虫利用这个反复爬取
            "request_url":'',
            "request_infos": ''
        }
    # print("result = ", result)
    return result


@app.errorhandler(404)
def handler_404_error(err):
    resData = {
        "resCode": 404, # 非0即错误 1
        "data": [],# 数据位置，一般为数组
        "message": err
    }
    return jsonify(resData)


@app.route('/user_stuinfos', methods=['GET', 'POST'])
def get_specific_stuinfos(stu_uuid):
    book = Book()
    sql_data = book.get_stu_infos(stu_uuid)
    print(stu_uuid, " request specific stuinfos")
    print(sql_data)
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


@app.route('/get_all2stuperminfos', methods=['GET', 'POST'])
def get_all2stu_perminfos():
    data = json.loads(request.get_data(as_text=True))
    if 'stu_uuid' not in data.keys():
        print('no stu_uuid in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no stu_uuid'
        }
        return jsonify(resData)

    book = Book()
    stu_uuid = data['stu_uuid']
    res = book.get_allstuperm_infos(stu_uuid)
    print(stu_uuid, " request all the data it can check")
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
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because no username'
        }
        return jsonify(resData)
    book = Book()
    nusername = data['username']
    print(nusername, "request all the admitted info he can check")
    res_bachelor = book.get_bachelor_infos()
    res_admitted = book.get_stu_admittedinfos(nusername)
    res_forbidden = book.get_stu_forbiddeninfos(nusername)
    res_stunameinfo = book.get_uuid2stuname()
    stuname2info = {}
    for each in res_stunameinfo:
        stuname2info[each['stu_uuid']] = each['stu_name']

    for iter in res_admitted:
        iter['stu_touuid'] = stuname2info[iter['stu_touuid']]
        DestType = iter['stu_desttype']
        if DestType == 0:
            iter['stu_dest'] = "未知"
        elif DestType == 4:
            iter['stu_dest'] = "待定"

    for iter in res_forbidden:
        # iter['stu_touuid'] = stuname2info[iter['stu_touuid']]
        DestType = iter['stu_desttype']
        if DestType == 0:
            iter['stu_dest'] = "未知"
        elif DestType == 1:
            iter['stu_dest'] = "非内地升学"
        elif DestType == 2:
            iter['stu_dest'] = "内地升学"
        elif DestType == 3:
            iter['stu_dest'] = "工作"
        else:
            iter['stu_dest'] = "待定"
        iter['stu_mastermajor'] = "该用户暂未向您开放详细查看权限"
        iter['stu_masterorphd'] = None
        iter['stu_masterperiod'] = None
        iter['stu_furtherinfo'] = None
        iter['stu_direction'] = None
    resData = {
        "resCode": 0,  # 非0即错误 1
        "data": [res_bachelor, res_admitted, res_forbidden],  # 数据位置，一般为数组
        "message": 'Successfully fetch all the admitted data of this user'
    }
    return jsonify(resData)


def is_allow_domain_time(request_time, request_url):
    if(int(time.time() * 1000) - int(request_time) > 300000):
        return True
    if request_url not in REQUSET_LISTS:
        # 只有指定的域名才能访问
        # resData = {
        #     "resCode": 1, # 非0即错误 1
        #     "data": [],# 数据位置，一般为数组
        #     "message": '你猜，你使劲猜'
        # }
        # return jsonify(resData)
        return True
    return False


@app.route('/checknamepw', methods=['GET', 'POST'])
def check_namepw():
    # data = request.get_json()
    data = json.loads(request.get_data(as_text=True))
    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)
    if 'password' not in data.keys():
        print('no password in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no password'
        }
        return jsonify(resData)
    book = Book()
    nusername = data['username']
    npassword = data['password']
    res_nuserinfo = book.get_user_password(nusername, npassword)
    print(nusername, "request login", ", matching record: ", res_nuserinfo)
    flag = res_nuserinfo is None
    resData = {
        "resCode": int(flag),
        "data": [res_nuserinfo],
        "message": "Password verified finished."
    }
    return jsonify(resData)


@app.route('/updatebachelorinfo', methods=['GET', 'POST'])
def update_bachelorinfo():
    data = json.loads(request.get_data(as_text=True))
    if data['key'] != 'update':
        print('Mismatching operation, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because mismatching operation'
        }
        return jsonify(resData)

    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)
    username = data['username']
    print(username, " update its bachelor info")
    if 'infos' not in data.keys():
        print('no infos in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no infos'
        }
        return jsonify(resData)
    infos = data['infos']
    book = Book()
    res = book.update_bachelordest(username, infos)
    resData = {
        "resCode": 0,
        "data": [],
        "message": 'update successfully'
    }
    return jsonify(resData)


@app.route('/updatemasterinfo', methods=['GET', 'POST'])
def update_masterinfo():
    data = json.loads(request.get_data(as_text=True))
    if data['key'] != 'update':
        print('Mismatching operation, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because mismatching operation'
        }
        return jsonify(resData)

    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)

    username = data['username']
    print(username, " update its master info")
    if 'infos' not in data.keys():
        print('no infos in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no infos'
        }
        return jsonify(resData)

    infos = data['infos']
    book = Book()
    res = book.update_masterdest(username, infos)
    resData = {
        "resCode": 0,
        "data": [],
        "message": 'update successfully'
    }
    return jsonify(resData)


@app.route('/updatepermission', methods=['GET', 'POST'])
def update_permission():
    data = json.loads(request.get_data(as_text=True))
    if data['key'] != 'update':
        print('Mismatching operation, fxxk!')
        resData = {
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because mismatching operation'
        }
        return jsonify(resData)

    if 'infos' not in data.keys():
        print('no infos in data, fxxk!')
        resData = {
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because no infos'
        }
        return jsonify(resData)

    username = data['username']
    stu_uuid = data['stu_uuid']
    infos = data['infos']
    print(username, " update its readable permission")

    book = Book()
    ret_info = book.update_masterpermission(username, stu_uuid, infos)
    print(ret_info)

    resData = {
        "resCode": 0,  # 非0即错误 1
        "data": [],  # 数据位置，一般为数组
        "message": 'Successfully update permissions'
    }
    return jsonify(resData)


@app.route('/updateallpermissions', methods=['GET', 'POST'])
def update_allpermissions():
    data = json.loads(request.get_data(as_text=True))
    if data['key'] != 'update':
        print('Mismatching operation, fxxk!')
        resData = {
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because mismatching operation'
        }
        return jsonify(resData)

    if 'infos' not in data.keys():
        print('no infos in data, fxxk!')
        resData = {
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because no infos'
        }
        return jsonify(resData)

    if 'allpermvalue' not in data.keys():
        print('no allpermvalue in data, fxxk!')
        resData = {
            "resCode": 1,  # 非0即错误 1
            "data": [],  # 数据位置，一般为数组
            "message": 'failed because no allpermvalue'
        }
        return jsonify(resData)

    stu_uuid = data['stu_uuid']
    print(stu_uuid, " update all its readable permission")
    infos = data['infos']
    permsvalue = data['allpermvalue']

    book = Book()
    ret_info = book.update_allpermission(stu_uuid, permsvalue, infos)

    resData = {
        "resCode": 0,  # 非0即错误 1
        "data": [],  # 数据位置，一般为数组
        "message": 'Successfully update permissions'
    }
    return jsonify(resData)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    book = Book()
    arrData = "Please do not hack this database."
    return jsonify(arrData)


if __name__ == '__main__':
    print("__name__ = ", __name__)
    app.run(host='127.0.0.1', port=1943, debug=True)
    # app.run(host='0.0.0.0', port=8889, debug=True)
