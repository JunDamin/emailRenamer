import PySimpleGUI as sg
from emailRenamer import renameEmlFiles

sg.change_look_and_feel('DarkAmber')

layout = [[sg.Text("eml 파일경로를 선택해 주세요.")],
          [sg.Input(size=(70, 5)), sg.FolderBrowse(button_text="폴더선택")],
          [sg.Output(size=(80, 20))],
          [sg.Button(button_text="변환시작", key="OK"), sg.Button(button_text="종료", key='Cancel')]]

window = sg.Window('emailRenamer v.0.2', icon="email.ico",layout=layout)

openText = '''
======================================================================
폴더를 선택하고 변환 시작을 누르면 해당 폴더안에 있는 eml파일명 변환 작업이 진행됩니다.
eml 파일이 "(연월일_시간)_(발신자)_제목" 형식으로 변환됩니다.

참고사항
  - 사내메일이나 웹메일 상관 없이 eml 파일이면 작동합니다.
  - 경로 + 파일명이 너무 길면 변환이 안되기도 합니다.
======================================================================
'''

endText = '''
======================================================================
{}개 변환 작업이 완료 되었습니다.
======================================================================
'''


window.read(timeout=10)
print(openText)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if event == 'OK':
        output = renameEmlFiles(values[0], window)
        print(endText.format(len(output)))
window.close()