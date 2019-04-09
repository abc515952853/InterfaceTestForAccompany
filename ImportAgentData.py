import xlrd
import xlwt
from xlutils.copy import copy
import os

import uuid
import requests
import json

from xpinyin import Pinyin

proDir = os.path.split(os.path.realpath(__file__))[0]

def GetAgentDataFromExcl():
    xlsPath = os.path.join(proDir,'代理商数据.xlsx')
    print(proDir)
    openfile = xlrd.open_workbook(xlsPath,'w',formatting_info= False)
    newfile = copy(openfile)

    sheet = openfile.sheet_by_name('代理商数据')
    row = sheet.row_values(0)
    rowNum  = sheet.nrows
    colNum = sheet.ncols 
    
    cls = []
    curRowNo = 1
    while hasNext(rowNum,curRowNo):
        s = {}  
        col = sheet.row_values(curRowNo)  
        i = colNum  
        for x in range(i):
            s[row[x]] = conversion_cell(sheet,curRowNo,x,col[x])
        cls.append(s)
        curRowNo += 1
    return cls

def conversion_cell(sheet,curRowNo,curColNo,cell):
    #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error  
    if sheet.cell(curRowNo,curColNo).ctype == 2:
            no =  int(cell)
    else:
            no = cell
    return no

def hasNext(rownum,curRowNo):  
    if rownum == 0 or rownum <= curRowNo :  
        return False  
    else:  
        return True 

def SetDataToDb():
    data = GetAgentDataFromExcl()
    
    for i in range(len(data)):
        RealName = str(data[i]['RealName'])
        Phone = str(data[i]['Phone'])
        StoreNumber = int(data[i]['StoreNumber'])
    

        session = 'Bearer 4e28f4511f6fda9f392d5a817fb7d501a855f34e3bed85e87a985da8fb1b7f52'
        url = 'http://admingateway.c4b102e69d03f4720a18035cb3ac0dcea.cn-beijing.alicontainer.com/api/v1.0/Salesman'

        headers = {'Content-Type': "application/json",'Authorization':session}
        payload ={
            "agentNumber": StoreNumber,
            "name": RealName,
            "password": "Pass123$",
            "phone": Phone,
            "username": StoreNumber
            }
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)
        if r.status_code == 200:
            print(str(StoreNumber),r.status_code)
        else:
            print(str(StoreNumber),r.status_code,r.text)



if  __name__ == '__main__':
    SetDataToDb()
