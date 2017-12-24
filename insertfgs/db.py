import logging
import pymysql
import traceback

class MySQLCommand(object):
    def __init__(self,host,port,user,passwd,db,table):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.table = table
        

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db,charset='utf8',cursorclass = pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def queryOne(self,sql,param=None):
         

        try:
            self.cursor.execute(sql,param)
            row = self.cursor.fetchone()
            
            return row

        except:
            print(sql + ' execute failed.')
    def queryAll(self,sql,param=None):
        try:
 
            self.cursor.execute(sql,param)
 
            row = self.cursor.fetchall()
             
            return row

        except:
            print(sql + ' execute failed.')

 

    def doMysql(self,sql,param=None):
 
      
        try:
            r=self.cursor.execute(sql,param)
            self.conn.commit()
            return r
        except Exception as e:
            print(e)
            self.conn.rollback()


    def closeMysql(self):
        self.cursor.close()
        self.conn.close()