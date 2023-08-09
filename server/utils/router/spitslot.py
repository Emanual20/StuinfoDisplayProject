from utils.flask.app import app
from utils.db import Book
from flask import request, jsonify

import json

@app.route('/updatespitslot', methods=['GET', 'POST'])
def upload_spitslotinfo():
    data = json.loads(request.get_data(as_text=True))
    if data['key'] != 'updatespitslot' or 'stu_uuid' not in data.keys() or 'info' not in data.keys():
        return jsonify(
            RetCode=1,
            Message='failed because mismatching info'
        )
    
    stu_uuid, spit_info, book = data['stu_uuid'], data['info'], Book()
    book.insert_spitslot(stu_uuid, spit_info)
    app.logger.info(f"{stu_uuid} upload spit_info: {spit_info}")
    return jsonify(
        RetCode=0,
        Message='上传吐槽信息成功！'        
    )

@app.route('/recentspitslot', methods=['GET', 'POST'])
def get_spitslotinfo():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    data = book.get_recent_spitslot(spit_num=20)
    return jsonify(
        RetCode=0,
        data=data,
        Message='fetch recent spitslot successfully..!'
    )