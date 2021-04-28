
from flask import *
import time
app = Flask(__name__)

# 편의상 채팅기록은 전역변수로 만들어서 쓰겠습니다.
# 실제 개발하실때는 이렇게 하시면 안돼요!
chats = []

@app.route('/chat')
def chat():
    return render_template('chat.html', chats=chats)

@app.route('/chat/data')
def chat_data():
    # 요청하는 클라이언트가 마지막으로 받은 채팅의 번호
    last_chat = request.values.get('last_chat')
    
    # request.values는 항상 문자열 혹은 None)
    # 값이 없거나, 숫자 형태가 아닐 수도 있음
    # 문자열을 숫자 타입으로 바꿔주되, 오류 발생시 0으로 사용
    try:
        last_chat = int(last_chat)
    except:
        last_chat = 0
    
    # time.sleep(초) - 해당 초만큼 대기
    #time.sleep(3)
    
    # 클라이언트에게 없는 최신 채팅만 보내주기
    # ['안녕하세요', '저는', '홍길동입니다']
    # 마지막으로 2개만 클라이언트가 받아갔다면, last_chat == 2
    # 그러면 우리가 반환해야하는 값은 저는 다음의 메시지부터 반환을 해야하고
    # chats을 2번째 인덱스 이후만 추출하여 반환
    #new_chats = chats[last_chat:]
    
    # 클라이언트가 받아간 이후에 새 채팅이 있다면 바로 응답
    if last_chat != len(chats):
        pass
    else: # 클라이언트가 받아간 이후 새 채팅이 없음
        for i in range(10):
            # 1초씩 10번 쉬는동안 새 채팅이 생기면 루프를 빠져나감
            if last_chat != len(chats):
                break
            time.sleep(1)
    
    new_chats = chats[last_chat:]
    return {'chats': new_chats, 'last_chat': len(chats)} 

@app.route('/chat/write', methods=['POST'])
def chat_write():
    content = request.values.get('content', '')
    
    # 저장
    chats.append(content)
    
    # 원래 채팅 목록 페이지로 이동
    #return redirect('/chat')
    return {'result': 'success'}

# 젤 아래에 위치!
app.run(host='localhost', port=5000, debug=True)