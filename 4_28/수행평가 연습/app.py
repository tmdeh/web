from flask import *
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import os

os.environ['APP_SETTINGS'] = 'setting.cfg'

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

mysql = MySQL(cursorclass= DictCursor)
mysql.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def login_post():
    inputID = request.values['id']
    inputPW = request.values['pw']

    conn = mysql.get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT user_pw, user_name FROM user2 where user_id = %s;', [inputID])
    # 결과 1개 가져오기
    row = cursor.fetchone()

    err = ''
    if(row is None):
        err = 'ID, 비밀번호가 올바르지 않습니다.'
        return render_template('/login.html', err = err)
    elif row['user_pw'] == inputPW:
        session['name'] = row['user_name'] #세션
        name = session['name']
        return render_template('/index_logged.html', err = err)

  

@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/join', methods = ['POST'])
def join_post():
    userid = request.values['id']
    name = request.values['name']
    pw = request.values['pw']

    conn = mysql.get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO `user2` (`pk`, `user_id`, `user_name`, `user_pw`) VALUES (NULL, "%s", "%s", "%s");', [userid], [name], [pw])

    row = cursor.fetchone()
    print(row)
    return render_template('join.html')

@app.route('/index_logged')
def index_logged():
    return render_template('index_logged.html')



app.run(host='localhost', port=3000, debug=True)