import pyodbc
import ReadConfig
import uuid
import time


class Pyodbc:
    def __init__(self,):
        driver = 'MySQL ODBC 8.0 ANSI Driver'  # 因版本不同而异
        readconfig=ReadConfig.ReadConfig()
        DBIp = readconfig.get_basedata('db_accompanying_ip')
        DBPort = int(readconfig.get_basedata('db_accompanying_port'))
        DBUserName = readconfig.get_basedata('db_accompanying_username')
        DBPassWord = readconfig.get_basedata('db_accompanying_password')
        DBName= readconfig.get_basedata('db_accompanying_dbname')
        self.conn = pyodbc.connect(driver=driver,server=DBIp,port = DBPort,user=DBUserName, password=DBPassWord, database=DBName)
        self.cursor = self.conn.cursor()

    def DBClose(self):
        self.conn.close()
    
    def DBDelete(self,formname):
        sql = "delete [dbo].{}".format(formname)
        self.cursor.execute(sql)
        self.conn.commit()

    def GetRoles(self):
        sql = "SELECT * FROM user_salesman"
        self.cursor.execute(sql)
        a= self.cursor.fetchone()
        print(a)

# if __name__ == "__main__":
#     a = Pyodbc()
#     a.GetRoles()






            
        

        
        