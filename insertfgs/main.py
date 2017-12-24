from json import dumps as json_dumps

from sanic import Sanic
from sanic.response import json
import xlrd

import db
from model.user import User
from model.worker import Worker

 
# from gi import require_version
# require_version('Atspi', '2.0')
# app = Sanic(__name__)
# 
# @app.route("/")
# async def test(request):
cm = db.MySQLCommand('127.0.0.1', 3306, 'root', 'a4152637', 'fgs', 'worker')
cm.connectMysql()

data = xlrd.open_workbook('/home/sonic/1.xlsx')
table=data.sheet_by_index(0)

for i in range(1,table.nrows ):
     
    user=User()
    user.userName=str(table.row_values(i)[0])
    user.contractId=str(table.row_values(i)[1])[1:]
    user.address=str(table.row_values(i)[2])
    user.gate=str(int(table.row_values(i)[3]))
    user.room=str(table.row_values(i)[4])
    user.manageState=str(table.row_values(i)[5])
    user.property=str(table.row_values(i)[6])
    user.selfArea=str(table.row_values(i)[7])
    user.sharedArea=str(table.row_values(i)[8])
    user.quotaFee=str(table.row_values(i)[9])
    user.remission=str(table.row_values(i)[10])
    user.pl=str(table.row_values(i)[11])
    user.fee=str(table.row_values(i)[12])
    user.wholeSet=str(table.row_values(i)[13])
    if table.row_values(i)[14]!='' or table.row_values(i)[14]!="'":
        user.cardId=str(table.row_values(i)[14])[1:]
    else:
        user.cardId=''
    if table.row_values(i)[15]!='':
        user.tele=str(int(table.row_values(i)[15]))
    else:
        user.tele=''
    user.workerId='lk'
    user.id='0'
 
    obj = user.__dict__
  
    print(obj)
    cm.doMysql('''insert into userinfo  values (
    %(id)s,
    %(userName)s,
    %(contractId)s,
    %(address)s,
    %(gate)s,
    %(room)s,
    %(manageState)s,
    %(property)s,
    %(selfArea)s,
    %(sharedArea)s,
    %(quotaFee)s,
    %(remission)s,
    %(pl)s,
    %(fee)s,
    %(wholeSet)s,
    %(cardId)s,
    %(tele)s,
    %(workerId)s
    )''', obj)
  
# 
#     # jrow = json(row)
# 
cm.closeMysql()
 
# return jrow
# 
#app.run(host="0.0.0.0", port=8000)

