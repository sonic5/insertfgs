from json import dumps as json_dumps

# from sanic import Sanic
# from sanic.response import json
import xlrd

import db
from model.user import User
from model.worker import Worker
def getec(i,j,cint=False):
    if table.row_values(i)[j]!='':
         if str(table.row_values(i)[j])[0]=="'":
             return str(table.row_values(i)[j])[1:]
  
         else:
             if cint:
                 try:
                     return str(int(table.row_values(i)[j]))
                 except:
                     return str(table.row_values(i)[j])
             return str(table.row_values(i)[j])
    else:
        return '' 
    
    
def splitn(s):
    if s.find(",")!=-1:
        return s
    n=3
    l=[s[i:i+n] for i in range(0, len(s), n)]
    r=''
    for i in range(l.__len__()):
        if i==l.__len__()-1:
            r+=l[i]
        else:           
            r+=l[i]+','
    return r    
            
         
 
# from gi import require_version
# require_version('Atspi', '2.0')
# app = Sanic(__name__)
# 
# @app.route("/")
# async def test(request):
cm = db.MySQLCommand('127.0.0.1', 3306, 'root', 'a4152637', 'fgs')
cm.connectMysql()

data = xlrd.open_workbook('C:/Users/Administrator/Desktop/lk.xlsx')
table=data.sheet_by_index(0)

for i in range(1,table.nrows ):
     
    user=User()
    user.userName=getec(i,0)
    user.contractId=getec(i,1)
    user.address=getec(i,2)
    user.gate=getec(i,3,True)
    user.room=splitn(getec(i,4,True))
    user.manageState=getec(i,5)
    user.property=getec(i,6)
    user.selfArea=getec(i,7)
    user.sharedArea=getec(i,8)
    user.quotaFee=getec(i,9)
    user.remission=getec(i,10)
    user.pl=getec(i,11)
    user.fee=getec(i,12)
    user.wholeSet=getec(i,13)
    user.cardId=getec(i,14)

    user.tele=getec(i,15,True)

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

