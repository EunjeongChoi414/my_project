from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import urllib

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbMeetUp

app = Flask(__name__)


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def write_user_info():
    leader_name_receive = request.form['leader_name_give']
    member_name_receive = request.form['member_name_give']
    user = {
        'id': leader_name_receive,
        'member': member_name_receive
    }
    db.users.insert_one(user)
    return jsonify({'result': 'success'})
# // 클릭한 날짜 저장하기

@app.route('/when')
def when():
    return render_template('when.html')

# // 클릭한 날짜 저장하기
@app.route('/when', methods=['POST'])
def save_dates():
    dates_receive = request.form.getlist('dates_give[]')
    id_receive = request.form['id_give']

    print(id_receive)
    print(urllib.parse.unquote(id_receive))
    db.users.update_one({'id': urllib.parse.unquote(id_receive)}, {'$set': {'ava_dates': dates_receive}})
    return jsonify({'result': 'success', 'msg': '날짜 저장완료'})

@app.route('/when2')
def when2():
    return render_template('when2.html')
# //클릭한 날짜 보여주기
# //선택한 시간 저장하기

@app.route('/when3')
def when3():
    return render_template('when3.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
