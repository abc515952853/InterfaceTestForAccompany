import pyodbc
import ReadConfig
import uuid
import time


class Pyodbc:
    def __init__(self,):
        driver = 'MySQL ODBC 8.0 ANSI Driver'  # 因版本不同而异
        readconfig=ReadConfig.ReadConfig()
        DBIp = readconfig.get_basedata('db_ip')
        DBPort = readconfig.get_basedata('db_port')
        DBUserName = readconfig.get_basedata('db_username')
        DBPassWord = readconfig.get_basedata('db_password')
        DBName= readconfig.get_basedata('db_dbname')
        print(DBIp,DBUserName,DBPassWord,DBName)
        self.conn = pyodbc.connect(driver=driver,server=DBIp,port = DBPort,user=DBUserName, password=DBPassWord, database=DBName)
        self.cursor = self.conn.cursor()

    def DBClose(self):
        self.conn.close()
    
    def DBDelete(self,formname):
        sql = "delete [dbo].{}".format(formname)
        self.cursor.execute(sql)
        self.conn.commit()

    def GetCustomer(self):
        sql = "SELECT * FROM user_salesman"
        self.cursor.execute(sql)
        a= self.cursor.fetchone()
        print(a)






            
        

        
        