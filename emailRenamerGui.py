import PySimpleGUI as sg
from emailRenamer import renameEmlFiles

sg.change_look_and_feel('DarkAmber')

layout = [[sg.Text("eml 파일경로를 선택해 주세요.")],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Button(button_text="변환시작", key="OK"), sg.Button(button_text="종료", key='Cancel')]]

window = sg.Window('emailRenamer v.0.2', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if event == 'OK':
        renameEmlFiles(values[0])
        
window.close()