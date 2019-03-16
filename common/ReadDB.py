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

    def GetCenterInfoByName(self,name):
        sql = "SELECT center_name,principal_name,phone,province,city,county,username,center_id,agent_number,create_time,remark  FROM center WHERE center_name = '{0}'".format(name)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            centerinfo  = {
                "centerName": data[0],
                "principalName": data[1],
                "phone": data[2],
                # "password": data[4],
                "province": data[3],
                "city": data[4],
                "county": data[5],
                "username": data[6],
                "centerid":data[7]
            }
        else:
            centerinfo = None
        return centerinfo

    def GetCenterInfoById(self,id):
        sql = "SELECT center_name,principal_name,phone,province,city,county,username,center_id,agent_number,create_time,remark  FROM center WHERE center_id = '{0}'".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            centerinfo  = {
                "centerName": data[0],
                "principalName": data[1],
                "phone": data[2],
                # "password": data[4],
                "province": data[3],
                "city": data[4],
                "county": data[5],
                "username": data[6],
                "centerid":data[7]
            }
        else:
            centerinfo = None
        return centerinfo

    def GetCenterInfoAllByKey(self,key,start,end):
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'
            
        if len(key) > 0:
            sql = "SELECT center_id from center \
            WHERE phone like '%{0}%' or principal_name like '%{0}%' or center_name like '%{0}%' ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        else:
            sql = "SELECT center_id from center \
            ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        centeridinfo = []
        if data is not None:
            for i in range(len(data)):
                centeridinfo.append(data[i][0])
        else:
            centeridinfo = None
        return centeridinfo

    def GetAssistantInfoByJobnumber(self,jobNumber):
        sql = "SELECT assistant_id,center_id,job_number,name,phone,avatar FROM assistant \
        WHERE job_number = '{0}'".format(jobNumber)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            assistantinfo ={
                "assistant_id":data[0],
                "center_id" : data[1],
                "job_number" : data[2],
                "name" : data[3],
                "phone" : data[4],
                "avatar" : data[5],
                "assistant_id":data[6]
            }
        else:
            assistantinfo = None
        return assistantinfo
        


# if __name__ == "__main__":
#     a = Pyodbc()
#     a.GetRoles()






            
        

        
        