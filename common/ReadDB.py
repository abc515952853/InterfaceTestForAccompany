import pyodbc
import ReadConfig
import uuid
import time


class Pyodbc:
    def __init__(self,):
        driver = 'MySQL ODBC 8.0 ANSI Driver'  # 因版本不同而异
        readconfig=ReadConfig.ReadConfig()
        DBIp = readconfig.get_basedata('db_ip')
        DBUserName = readconfig.get_basedata('db_username')
        DBPassWord = readconfig.get_basedata('db_password')
        DBName= readconfig.get_basedata('db_dbname')
        print(DBIp,DBUserName,DBPassWord,DBName)
        self.conn = pyodbc.connect(driver=driver,server=DBIp, user=DBUserName, password=DBPassWord, database=DBName)
        # self.conn = pymysql.connect(host='127.0.0.1', port=33061,user='accompanying',passwd='Accompanying123321',db='accompanying',charset ='utf8')
        # self.cursor = self.conn.cursor()

    # def DBClose(self):
    #     self.conn.close()
    
    # def DBDelete(self,formname):
    #     sql = "delete [dbo].{}".format(formname)
    #     self.cursor.execute(sql)
    #     self.conn.commit()

    def GetCustomer(self):
        sql = "SELECT * FROM user_salesman"
        # self.cursor.execute(sql)
        # a= self.cursor.fetchone()
        # print(a)






            
        

        
        