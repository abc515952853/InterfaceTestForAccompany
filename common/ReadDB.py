import pyodbc
import ReadConfig
import uuid
import time


class Pyodbc:
    def __init__(self,):
        driver = 'SQL Server Native Client 11.0'  # 因版本不同而异
        readconfig=ReadConfig.ReadConfig()
        DBIp = readconfig.get_basedata('db_ip')
        DBUserName = readconfig.get_basedata('db_username')
        DBPassWord = readconfig.get_basedata('db_password')
        DBName= readconfig.get_basedata('db_dbname')
        self.conn = pyodbc.connect(driver=driver, server=DBIp, user=DBUserName, password=DBPassWord, database=DBName)
        self.cursor = self.conn.cursor()

    def DBClose(self):
        self.conn.close()
    
    def DBDelete(self,formname):
        sql = "delete [dbo].{}".format(formname)
        self.cursor.execute(sql)
        self.conn.commit()

    def GetCustomer(self,name):
        time.sleep(1)






            
        

        
        