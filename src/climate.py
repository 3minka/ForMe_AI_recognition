import requests
import json
from src.funcs import speak
from src.funcs import game_input

# 날씨 클래스
class Climate:
    location = {
        '서울' : {'lat' : 37.566, 'long' : 126.9784},
        '런던' : {'lat' : 51.5085, 'long' : -0.1257},
        '뉴욕' : {'lat' : 40.7143, 'long' : -74.006},
        '포항' : {'lat' : 36.8144, 'long' : 128.1211}
        }
    

    # 말했던 단어 저장
    user_answered = []

    # 위치 정보 담당
    def start(self):
        print('')
        print('=' * 45)
        print('어느 나라의 날씨를 조회할까요 ? ex) 서울 런던 뉴욕 포항')
        speak('어느 나라의 날씨를 조회할까요 ')

        print('나라를 이야기 해주세요.')
        speak('나라를 이야기 해주세요.')
    
        # 사용자 단어 입력
        while 1:
            user_input = game_input()
            # user_input = input('입력하세요 : ')
            if user_input:
                # 위치 정보가 서울 런던 뉴욕 포항 중에 하나인 지 확인
                if user_input in list(self.location.keys()):
                    break
                else:
                    print('서울 런던 뉴욕 포항 중의 나라가 아닙니다. 다시 입력해주세요.')
                    speak('알수없는 나라 입니다. 다시 입력해주세요.')
        # 단어가 입력되면 리스트에 저장
        self.user_answered.append(str(user_input))
        
        return self.user_answered

    # 포항 날씨 조회
    def searching(self):
        user_answered = self.start()
        lat = self.location[user_answered[0]]["lat"]
        long = self.location[user_answered[0]]["long"]

        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true')
        try:
            response = requests.get(url_info)
        except:
            print('날씨 조회 중 홈페이지 오류가 발생했습니다.')
        
        # response 로 얻어온 json을 파이썬이 사용할 수 있도록 변경
        data = json.loads(response.text)
        self.printing(user_answered[0], data['current_weather']['temperature'])
    
    # 날씨 프린트
    def printing(self, loc, temp):
        print('')
        print('=' * 45)
        print(f'{loc}날씨는 {temp}도 입니다.')
        speak(f'{loc}날씨는 {temp}도 입니다.')
        print('')