import sys
from src.search import Search
from src.climate import Climate
from src.game import Game
from src.funcs import menu_to_text
from src.funcs import assistant_check
from src.funcs import speak



# 전체 프로그램 실행
while 1:
    print('=' * 45)
    print('음성 비서를 부르세요. 종료를 원하시면 종료라고 말 하세요. (비서, 비서야)')
    speak('음성 비서를 부르세요. 종료를 원하시면 종료라고 말 하세요.')

    # 음성 비서 호출 무한 대기
    while 1:
        assistant = assistant_check()
        if assistant:
            break
    
    # 음성 비서 호출
    if assistant in ['비서야', '비서']:
        speak('네')
        print('')
        print('=' * 45)
        print('검색, 날씨 조회, 게임 등을 선택할 수 있습니다.')

        # 메뉴 음성 입력 무한 대기
        while 1:
            menu, topic = menu_to_text()
            if menu:
                break

        # 네이버 검색
        if menu in ['검색', '검색해']:   
            speak('검색합니다.')
            naver = Search(topic)
            naver.searching()
            print('')
        # 날씨
        elif menu in ['날씨', '날씨조회']:
            climate = Climate()
            climate.searching()
        # 끝말잇기
        elif menu in ['게임', '끝말잇기']:
            game = Game()
            game.start()
        # 메뉴 선택에서 전체 종료 하기
        elif menu == '종료':
            speak('음성 비서를 종료합니다.')
            exit(0)
        # 이외의 입력
        else:
            speak('메뉴를 다시 이야기 해주세요.')

    # 종료 입력 시 프로그램 종료
    elif assistant == '종료':
        # 음성 비서 실행이 끝나면 종료 (while loop 나오기)
        print('음성 비서를 종료합니다.')
        speak('음성 비서를 종료합니다.')
        break
    # 이외의 단어 입력
    else:
        print('다시 이야기 해주세요.')
        speak('다시 이야기 해주세요.')  