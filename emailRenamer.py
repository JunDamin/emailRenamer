import os
import shutil
import re
from datetime import datetime
from email import policy
from email.parser import BytesParser

def prettify_filename(filename):
    return re.sub(r'[\\\/:*?"<>|.]+', "", filename)


def getEmailData(emlAddr):
    item_list = ["date", "From", "To", "Subject"] #긁어낼 아이템
    emlData = {} 
    with open(emlAddr, 'rb') as fp:
        msg = BytesParser(policy = policy.default).parse(fp)
        for item in item_list:
            if msg[item]:
                emlData[item] = msg[item]
            else:
                emlData[item] = ""
    return emlData

def makeEmailName(path, emlData):
    eml_time_format = "%a, %d %b %Y %H:%M:%S %z"
    output_time_format = "(%Y%m%d_%H%M)"
    #시간 포맷 변환
    if emlData['date']:
        emlData['dateStr'] = datetime.strptime(emlData['date'], eml_time_format).strftime(output_time_format) #시간 포맷 변환
    else:
        emlData['dateStr'] = ""
    #발신자 괄호
    emlData['From'] = "("+emlData['From']+")"
    #파일명 변환
    filename = " _ ".join([emlData[item] for item in ['dateStr', 'From', 'Subject']])
    filename = prettify_filename(filename)
    filename += ".eml"
    print(filename)
    fileAddr = os.path.join(path, filename) #경로 저장
    return fileAddr
    
def renameEmailFile(emlAddr):
    path = os.path.dirname(emlAddr)
    emlData = getEmailData(emlAddr)
    fileAddr = makeEmailName(path, emlData)
    shutil.move(emlAddr, fileAddr)
    return fileAddr


def renameEmlFiles(path):
    eml_list = [os.path.join(path, file) for file in os.listdir(path) if file[-3:] == "eml"]
    log_list = []
    for emlAddr in eml_list:
        try:
            log_list.append(renameEmailFile(emlAddr))
        except:
            print("Error")
            continue
    print("Process Completed"")
    return log_list
