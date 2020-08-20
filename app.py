from flask import Flask, render_template, redirect

app = Flask(__name__)


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/when')
def when():
    return render_template('when.html')


@app.route('/when2')
def when2():
    return render_template('when2.html')

@app.route('/when3')
def when3():
    return render_template('when3.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
