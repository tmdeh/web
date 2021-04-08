import requests
from datetime import datetime
# API 요청
url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
params = {
    'Type': 'json',
    'ATPT_OFCDC_SC_CODE': 'D10',  # 시도교육청코드
    'SD_SCHUL_CODE': '7240454',  # 표준학교코드
    'MLSV_YMD': '' #20210407
}
a = int(datetime.today().strftime("%Y%m%d"))
params['MLSV_YMD'] = a

r = requests.get(url, params=params)

# JSON 파싱
j = r.json()

# 식단표 루프
total_cal = 0
for menu in j['mealServiceDietInfo'][1]['row']:
    print('[' + menu['MMEAL_SC_NM'] + ']')

    # 식단 내용
    menu_content = menu['DDISH_NM']
    # <br/> 을 줄바꿈으로 모두 변경
    menu_content = menu_content.replace('<br/>', '\n')
    print(menu_content)

    # 칼로리 정보
    print(menu['CAL_INFO'])
    print('----------')

    cal = menu['CAL_INFO']

    # Kcal를 찾아서 그 앞까지만 subtring
    cal = cal[0:cal.find(' Kcal')]

    # 문자열을 실수형으로 변환
    cal = float(cal)
    total_cal = total_cal + cal

# format string (python 3.6 이상)
# f'... {변수명} ...'
print(f'칼로리 합: {total_cal} Kcal')