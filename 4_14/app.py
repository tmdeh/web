# 20210414

from flask import *

app = Flask(__name__)

# 세션을 사용하기 위해서 암호화키 설정
# app.secret_key = '12345678'
# 혹은 settings.cfg에
# SECRET_KEY = '12345678'

# pip install flask-mysql
from flaskext.mysql import MySQL
import pymysql

# 1. 설정파일 만들기
# settings.cfg 파일에 설정값 입력

# 2. 환경변수에 설정파일의 경로를 적어주기
# bash쉘: export APP_SETTINGS=settings.cfg
# 윈도우: set APP_SETTINGS=settings.cfg

# 혹은 파이썬으로 현재 환경변수에 값을 넣어주기
import os

os.environ['APP_SETTINGS'] = 'settings.cfg'

# 3. flask에 설정파일이 있다고 알려주기
app.config.from_envvar('APP_SETTINGS')

# DB연결 정보 입력
'''mysql = MySQL(host='web.dgsw.kr', port=3306, 
                user='s2000', password='20002000', 
                db='s2000',
                cursorclass=pymysql.cursors.DictCursor)
'''
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
# Flask 인스턴스와 연결
mysql.init_app(app)


@app.route('/delete/<pk>')
def guestbook_delete():
    conn = mysql.get_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM guestbook WHERE pk = %s', (pk,))

    conn.commit()

    return redirect('/')

@app.route('/write', methods=['POST'])
def write():
    conn = mysql.get_db()
    cursor = conn.cursor()

    # 입력값을 받되, 없을 경우 공백
    # .strip()은 좌우 여백 제거
    author = request.values.get('author', '').strip()
    content = request.values.get('content', '').strip()

    # print(author)
    # print(content)

    # 둘다 공백이 아닐때만 DB에 입력
    if author != '' and content != '':
        # 컬럼 순서가 pk, author, content, inserted_at
        # pk에는 AUTOINCREMENT를 걸어뒀으므로 NULL 입력시 자동으로 숫자 고유값이 들어감
        # inserted_at 에는 현재 작성시간을 입력하기 위해 mysql/mariadb 내장 함수인 NOW() 사용

        # SQL Injection 방어를 위해서 쿼리문에 사용자 입력값을 그대로 넣으면 안되겠죠?
        # escape를 해서 넣어야 하는데, 쿼리문에 %s 로 자리를 지정해주고,
        # 쿼리문 다음 인자로 해당 값들을 넘겨주면 자동으로 escape 해줍니다.
        cursor.execute('INSERT INTO guestbook VALUES (NULL, %s, %s, NOW());', (author, content,))
        #                                              author,   ㄴ> content

        # DB의 변경사항 반영
        conn.commit()
        # 변경사항을 반영하지 않으려면
        # conn.rollback()

    # 작성이 끝났으면 / 주소로 돌려보냄
    return redirect('/')





# 젤 아래에 위치!
app.run(host='localhost', port=2000, debug=True)