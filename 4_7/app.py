from flask import *

# flask.Flask, flask.request 이렇게 써야하는걸 바로 Flask, request 이렇게 쓸 수 있습니다

# flask 인스턴스 생성
# __name__ 은 현재 실행되고 있는 모듈의 이름을 가리키는 예약어인데
# flask는 그냥 항상 이렇게 쓴다고 생각하셔도 됩니다
app = Flask(__name__)


# / 경로로 들어왔을 때 실행될 함수
@app.route('/')
def index():
    return 'Hello world'


@app.route('/dgsw/2/1/15')
def student_2115():
    return '임재현'


def get_menu(date):
    import requests

    # API 요청
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    params = {
        'Type': 'json',
        'ATPT_OFCDC_SC_CODE': 'D10',  # 시도교육청코드
        'SD_SCHUL_CODE': '7240454',  # 표준학교코드
        'MLSV_YMD': date
    }
    r = requests.get(url, params=params)

    # JSON 파싱
    j = r.json()

    result = ''

    # 식단표 루프
    total_cal = 0
    for menu in j['mealServiceDietInfo'][1]['row']:
        result += '[' + menu['MMEAL_SC_NM'] + ']\n'

        # 식단 내용
        menu_content = menu['DDISH_NM']
        # <br/> 을 줄바꿈으로 모두 변경
        menu_content = menu_content.replace('<br/>', '\n')
        result += menu_content + '\n'

        # 칼로리 정보
        result += menu['CAL_INFO'] + '\n'
        result += '----------\n'

        cal = menu['CAL_INFO']

        # Kcal를 찾아서 그 앞까지만 subtring
        cal = cal[0:cal.find(' Kcal')]

        # 문자열을 실수형으로 변환
        cal = float(cal)
        total_cal = total_cal + cal

    # format string (python 3.6 이상)
    # f'... {변수명} ...'
    result += f'칼로리 합: {total_cal} Kcal'

    return result


def get_menu2(date):
    import requests

    # API 요청
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    params = {
        'Type': 'json',
        'ATPT_OFCDC_SC_CODE': 'D10',  # 시도교육청코드
        'SD_SCHUL_CODE': '7240454',  # 표준학교코드
        'MLSV_YMD': date
    }
    r = requests.get(url, params=params)

    # JSON 파싱
    j = r.json()

    data = {
        'menu': j['mealServiceDietInfo'][1]['row']
    }

    return data


@app.route('/menu')
def menu():
    # flask.request

    # $_GET == request.args
    # $_POST == request.form
    # $_REQUEST = request.values

    mdate = request.values.get('date')
    # date값이 없으면 None, 오늘 날짜로 설정
    if mdate is None:
        from datetime import date
        mdate = date.today().strftime('%Y%m%d')

    '''menu_data = get_menu(mdate).replace('\n', '<br>')
    print(menu_data)'''

    menu_data = get_menu2(mdate)
    # menu_data['menu'] -> [(조식 식단표), (중식 식단표), ...]

    return render_template('menu.html', menu_data=menu_data)




def index():
    return 'Hello world'


# 파이썬 내장 웹서버로 실행
app.run(host='localhost', port=2000, debug=True)