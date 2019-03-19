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

    def GetAssistantInfoAllByKey(self,key,start,end,centeid = None):
        sql = "SELECT assistant_id from assistant"
        if len(key) > 0:
            sql = sql + "WHERE phone like '%{0}%' or job_number like '%{0}%' or name like '%{0}%'".format(key)

        if len(key)>0 and centeid is not None:
            sql = sql +" and center_id = {0}".format(centeid)
        elif len(key) ==0 and centeid is not None:
            sql = sql +" WHERE center_id = {0}".format(centeid)
            
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'

        sql = sql+ " ORDER BY create_time desc  LIMIT {0},{1}".format(start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        assistantidinfo = []
        if data is not None:
            for i in range(len(data)):
                assistantidinfo.append(data[i][0])
        else:
            assistantidinfo = None
        return assistantidinfo

    def GetAssistanctInfoById(self,id):
        sql = "SELECT center_id,job_number,name,phone,avatar,patient_numberstate,doctor_number FROM assistant WHERE assistant_id = '{0}'".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            centerinfo  = {
                "center_id": data[0],
                "job_number": data[1],
                "name": data[2],
                "phone": data[3],
                "avatar": data[4],
                "state":data[5],
                "patient_number":data[6],
                "doctor_number":data[7]
            }
        else:
            centerinfo = None
        return centerinfo
    
    def GetAssistantCountByCenterid(self,centerid = None):
        if centerid is None:
            sql = "SELECT count(*) from assistant"
        else:
            sql = "SELECT count(*) from assistant where center_id={0}".format(centerid)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            assistantcountinfo = data[0]
        else:
            assistantcountinfo = None
        return assistantcountinfo

    def GetexpErtstudioInfoByName(self,name):
        sql = "SELECT expert_studio_id,phone,name,avatar,hospital,title,province,city,county,expertise,vitae,remark,doctor_number FROM center \
        WHERE center_name = '{0}'".format(name)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            expertstudioinfo  = {
            "expert_studio_id":data[0],
            "phone": data[1],
            "name": data[2],
            "avatar": data[3],
            "hospital": data[4],
            "title": data[5],
            "province": data[6],
            "city": data[7],
            "county": data[8],
            "expertise": data[9],
            "vitae": data[10],
            "remark": data[11]
            }
        else:
            expertstudio = None
        return expertstudio

    def GetExpertstudioInfoAllByKey(self,key,start,end):
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'
            
        if len(key) > 0:
            sql = "SELECT expert_studio_id from expert_studio \
            WHERE phone like '%{0}%' or job_number like '%{0}%' or name like '%{0}%' ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        else:
            sql = "SELECT expert_studio_id from expert_studio \
            ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        expertstudioidinfo = []
        if data is not None:
            for i in range(len(data)):
                expertstudioidinfo.append(data[i][0])
        else:
            expertstudioidinfo = None
        return expertstudioidinfo
    
    def GetExpertStudioinfoById(self,id):
        sql = "SELECT center_name,principal_name,phone,province,city,county,username,center_id,agent_number,create_time,remark,doctor_number  FROM center WHERE center_id = '{0}'".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            expertstudioinfo  = {
            "expert_studio_id":data[0],
            "phone": data[1],
            "name": data[2],
            "avatar": data[3],
            "hospital": data[4],
            "title": data[5],
            "province": data[6],
            "city": data[7],
            "county": data[8],
            "expertise": data[9],
            "vitae": data[10],
            "remark": data[11],
            "doctor_number":data[12]
            }
        else:
            centerinfo = None
        return centerinfo

    def GetExpertstudioCount(self):
        sql = "SELECT count(*) from expert_studio"
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            expertstudiocountinfo = data[0]
        else:
            expertstudiocountinfo = None
        return expertstudiocountinfo

    def GetDoctorinfoInfoByName(self,name):
        sql = "SELECT doctor_id,name,phone,idCard,certificate,avatar,hospital,title,department,expertise,expertStudioId,province,city,county,vitae FROM doctor \
        WHERE name = '{0}'".format(name)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            doctorinfo  = {
            "doctor_id":data[0],
            "name": data[1],
            "phone": data[2],
            "idCard": data[3],s
            "certificate": data[4],
            "avatar": data[5],
            "hospital": data[6],
            "title": data[7],
            "department": data[8],
            "expertise": data[9],
            "expertStudioId": data[10],
            "province": data[11],
            "city": data[12],
            "county": data[13],
            "vitae": data[14]
            }
        else:
            doctorinfo = None
        return doctorinfo

    def GetDoctorInfoAllByKey(key,start,end):
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'
            
        if len(key) > 0:
            sql = "SELECT doctor_id from doctor \
            WHERE expertise like '%{0}%' or name like '%{0}%' or phone like '%{0}%' ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        else:
            sql = "SELECT doctor_id from center \
            ORDER BY create_time desc  LIMIT {1},{2}".format(key,start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        doctoridinfo = []
        if data is not None:
            for i in range(len(data)):
                doctoridinfo.append(data[i][0])
        else:
            doctoridinfo = None
        return doctoridinfo
    
    def GetDoctorInfoById(self,id):
        sql = "SELECT name,phone,idCard,certificate,avatar,hospital,title,department,expertise,expertStudioId,province,city,county,vitae  FROM doctorinfo \
        WHERE doctor_id = '{0}'".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            doctorinfo  = {
                "name": name,
                "phone": phone,
                "idCard": idCard,
                "certificate": certificate,
                "avatar": avatar,
                "hospital": hospital,
                "title": title,
                "department": department,
                "expertise": expertise,
                "expertStudioId": experstudioid,
                "province": province,
                "city": city,
                "county": county,
                "vitae": vitae
            }
        else:
            doctorinfo = None
        return doctorinfo

    def GetDoctorCountByCenterid(self,expertstudioid = None):
        if expertstudioids is None:
            sql = "SELECT count(*) from doctor"
        else:
            sql = "SELECT count(*) from doctor where expert_studio_id={0}".format(centerid)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            doctorcountinfo = data[0]
        else:
            doctorcountinfo = None
        return doctorcountinfo

    def GetSalesmanInfoByName(self,name):
        sql = "SELECT salesman_id,user_id,center_id,name,phone,agent_number,state,qrcode FROM salesman \
        WHERE name = '{0}'".format(name)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            salesmaninfo  = {
            "salesman_id":data[0],
            "user_id": data[1],
            "center_id": data[2],
            "name": data[3],s
            "phone": data[4],
            "agent_number": data[5],
            "state": data[6],
            "qrcode": data[7]
            }
        else:
            salesmaninfo = None
        return salesmaninfo

    def GetSalesmanInfoAllByKey(self,key,start,end,centeid = None):
        sql = "SELECT salesman_id from salesman"
        if len(key) > 0:
            sql = sql + "WHERE phone like '%{0}%' or name like '%{0}%'".format(key)

        if len(key)>0 and centeid is not None:
            sql = sql +" and center_id = {0}".format(centeid)
        elif len(key) ==0 and centeid is not None:
            sql = sql +" WHERE center_id = {0}".format(centeid)
            
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'

        sql = sql+ " ORDER BY create_time desc  LIMIT {0},{1}".format(start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        salesmanidinfo = []
        if data is not None:
            for i in range(len(data)):
                salesmanidinfo.append(data[i][0])
        else:
            salesmanidinfo = None
        return salesmanidinfo

    def GetSalesmanInfoById(self,id):
        sql = "SELECT salesman_id,user_id,center_id,name,phone,agent_number,state,qrcode FROM salesman \
        WHERE salesman_id = {0}".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            salesmaninfo  = {
            "salesman_id":data[0],
            "user_id": data[1],
            "center_id": data[2],
            "name": data[3],
            "phone": data[4],
            "agent_number": data[5],
            "state": data[6],
            "qrcode": data[7]
            }
        else:
            salesmaninfo = None
        return salesmaninfo

    def GetSalesmanCountByCenterid(self,centerid = None):
        if centerid is None:
            sql = "SELECT count(*) from salesman"
        else:
            sql = "SELECT count(*) from salesman where center_id={0}".format(centerid)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            salesmancountinfo = data[0]
        else:
            salesmancountinfo = None
        return salesmancountinfo
    
    def GetmemberInfoByPhone(self,phone):
        sql = "SELECT member_id,center_id,salesman_id,name,phone,starttime,endtime,state FROM member \
        WHERE phone = '{0}'".format(phone)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            memberinfo  = {
            "member_id":data[0],
            "center_id":data[1],
            "salesman_id":data[2],
            "name": data[3],
            "phone": data[4],
            "startTime":data[5],
            "endTime":data[6],
            "state":data[7]
            }
        else:
            memberinfo = None
        return memberinfo

    def GetMenberInfoAllByKey(self,key,start,end,centeid = None):
        sql = "SELECT member_id from member"
        if len(key) > 0:
            sql = sql + "WHERE phone like '%{0}%' or name like '%{0}%'".format(key)

        if len(key)>0 and centeid is not None:
            sql = sql +" and center_id = {0}".format(centeid)
        elif len(key) ==0 and centeid is not None:
            sql = sql +" WHERE center_id = {0}".format(centeid)
            
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'

        sql = sql+ " ORDER BY create_time desc  LIMIT {0},{1}".format(start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        memberidinfo = []
        if data is not None:
            for i in range(len(data)):
                memberidinfo.append(data[i][0])
        else:
            memberidinfo = None
        return memberidinfo
    
    def GetPatientInfoByPhone(self,phone):
        sql = "SELECT patient_id,name,phone,relationship,phone,diseases,province,city,doctorid,assistantid FROM patient \
        WHERE phone = '{0}'".format(phone)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            patientinfo  = {
                "patient_id":data[0],
                "name": data[1],
                "phone": data[2],
                "relationship": data[3],
                "phone": data[4],
                "diseases": data[5],
                "province": data[6],
                "city": data[7],
                "doctorid": data[8],
                "assistantid": data[9]
            }
        else:
            patientinfo = None
        return patientinfo

    def GetPatientInfoAllByKey(self,key,start,end,centeid = None):
        sql = "SELECT a.patient_id FROM patient a inner JOIN member b on a.member_id = b.member_id"
        if len(key) > 0:
            sql = sql + "WHERE phone like '%{0}%' or name like '%{0}%'".format(key)

        if len(key)>0 and centeid is not None:
            sql = sql +" and b.center_id = {0}".format(centeid)
        elif len(key) ==0 and centeid is not None:
            sql = sql +" WHERE b.center_id = {0}".format(centeid)
            
        if len(start) == 0:
            start = '0'
        if len(end) == 0:
            end = '19'

        sql = sql+ " ORDER BY create_time desc  LIMIT {0},{1}".format(start,end)
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        patientidinfo = []
        if data is not None:
            for i in range(len(data)):
                patientidinfo.append(data[i][0])
        else:
            patientidinfo = None
        return patientidinfo
    
    def GetPatienInfoById(self,id):
        sql = "SELECT patient_id,name,phone,relationship,phone,diseases,province,city,doctorid,assistantid FROM patient \
        WHERE patient_id = '{0}'".format(id)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            patientinfo  = {
                "patient_id":data[0],
                "name": data[1],
                "phone": data[2],
                "relationship": data[3],
                "phone": data[4],
                "diseases": data[5],
                "province": data[6],
                "city": data[7],
                "doctorid": data[8],
                "assistantid": data[9]
            }
        else:
            patientinfo = None
        return patientinfo

    def GetPatientCountByCenterid(self,centerid = None):
        if centerid is None:
            sql = "SELECT count(*) FROM patient a inner JOIN member b on a.member_id = b.member_id"
        else:
            sql = "SELECT count(*) FROM patient a inner JOIN member b on a.member_id = b.member_id WHERE b.center_id ={0}".format(centerid)
        self.cursor.execute(sql)
        data= self.cursor.fetchone()
        if data is not None:
            patientcountinfo = data[0]
        else:
            patientcountinfo = None
        return patientcountinfo
        
        

# if __name__ == "__main__":
#     a = Pyodbc()
#     a.GetRoles()






            
        

        
        