from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import urllib

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbMeetUp

app = Flask(__name__)


# HTML 화면 보여주기
@app.route('/user_info')
def home():
    return render_template('index.html')

@app.route('/user_info', methods=['POST'])
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

@app.route('/date')
def date_page():
    return render_template('date.html')

# // 클릭한 날짜 저장하기
@app.route('/date', methods=['POST'])
def save_dates():
    dates_receive = request.form.getlist('dates_give[]')
    id_receive = request.form['id_give']
    db.users.update_one({'id': urllib.parse.unquote(id_receive)}, {'$set': {'ava_dates': dates_receive}})
    return jsonify({'result': 'success'})

@app.route('/time')
def when2():
    return render_template('time.html')

@app.route('/dates', methods=['GET'])
def get_dates():
    member_receive = request.args.get('member_give')
    get_id = db.users.find_one({'member': urllib.parse.unquote(member_receive)}, {'_id': False})
    get_date = db.users.find_one({'id': get_id['id']}, {'_id': False})
    print(get_date['ava_dates'])
    return jsonify({'result': 'success', 'dates': get_date['ava_dates']})

@app.route('/time_dates', methods=['POST'])
def save_time_dates():
    time_dates_receive = request.form.getlist('time_dates_give[]')
    member_receive = request.form['member_give']
    db.users.update_one({'member': urllib.parse.unquote(member_receive)}, {'$set': {'ava_timeDates': time_dates_receive}})
    return jsonify({'result': 'success', 'msg': "시간날짜 저장완료"})


# //선택한 시간 저장하기
@app.route('/result')
def when3():
    return render_template('result.html')

@app.route('/the_result', methods=['GET'])
def get_time_dates():
    member_receive = request.args.get('member_give')
    get_id = db.users.find_one({'member': urllib.parse.unquote(member_receive)}, {'_id': False})
    get_team = list(db.users.find({'id': get_id['id']}, {'_id': False}))
    print(get_team)
    return jsonify({'result': 'success', 'team': get_team})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
