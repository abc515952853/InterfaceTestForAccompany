import pyodbc
import json
import uuid
import time

class Pyodbc:
    def __init__(self,):
        driver = 'MySQL ODBC 8.0 ANSI Driver'  # 因版本不同而异
        DBIp = '101.37.179.99'
        DBPort = 3306
        DBUserName = 'root'
        DBPassWord = 'djejeUJ3qj^su22'
        DBName1= 'accompanying'
        DBName2= 'accompanying_identity'
        self.conn1 = pyodbc.connect(driver=driver,server=DBIp,port = DBPort,user=DBUserName, password=DBPassWord, database=DBName1)
        self.cursor1 = self.conn1.cursor()

        self.conn2 = pyodbc.connect(driver=driver,server=DBIp,port = DBPort,user=DBUserName, password=DBPassWord, database=DBName2)
        self.cursor2 = self.conn2.cursor()


    def CreateCenter(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-5:]						
        name = '沈斌'+num
        centername = '运营中心'+ num
        phone = '18501'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`) VALUES ('{0}','{1}',0,0,1,0,0)".format(userid,name)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `center`(`user_id`, `center_name`, `principal_name`, `phone`, `province`, `city`, `county`, `agent_number`)\
         VALUES ('{0}','{1}','{2}','{3}','浙江省','杭州市','滨江区','{4}')".format(userid,centername,name,phone,uuid.uuid1(),)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.Centerid = self.cursor1.fetchone()[0]

        self.conn1.commit()

    
    def CreateAssistant(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-5:]						
        name = '沈斌'+num
        assistantname = '医生助理'+ num
        phone = '18502'+num
        # sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`) VALUES ('{0}','{1}',0,0,1,0,0)".format(userid,name)
        # self.cursor2.execute(sql)
        # self.conn2.commit()

        sql = "INSERT INTO `assistant`(`center_id`, `job_number`, `name`, `phone`, `state`,`patient_number`, `doctor_number`) \
        VALUES ('{0}','{1}','{2}','{3}',1,0,0)".format(self.Centerid,num,assistantname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.AssistantId = self.cursor1.fetchone()[0]

        self.conn1.commit()  


    def CreateSalesman(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-5:]							
        name = '沈斌'+num
        Salesmanname = '业务员'+ num
        phone = '18503'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`) VALUES ('{0}','{1}',0,0,1,0,0)".format(userid,name)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `salesman`(`user_id`, `center_id`, `name`, `phone`, `state`) \
        VALUES ('{0}','{1}','{2}','{3}',1)".format(userid,self.Centerid,Salesmanname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.SalesmanId = self.cursor1.fetchone()[0]

        self.conn1.commit()  


    def CreateProfessor(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-5:]							
        name = '沈斌'+num
        Professorname = '专家'+ num
        phone = '13801'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`) VALUES ('{0}','{1}',0,0,1,0,0)".format(userid,name)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `expert_studio`(`user_id`, `name`, `phone`, `hospital`, `title`, `province`, `city`, `county`, `expertise`, `vitae`) \
        VALUES ('{0}','{1}','{2}','浙一医院','主任医师','浙江省','杭州市','滨江区','各种癌症','50年临床经验')".format(userid,Professorname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.ProfessorId = self.cursor1.fetchone()[0]

        self.conn1.commit()

    def CreateDoctor(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-5:]							
        name = '沈斌'+num
        doctorname = '医生'+ num
        phone = '13802'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`) VALUES ('{0}','{1}',0,0,1,0,0)".format(userid,name)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `doctor`(`user_id`, `expert_studio_id`, `name`, `phone`, `id_card`, `patients_number`)\
         VALUES ('{0}','{1}','{2}','{3}','330102198909286523',0)".format(userid,self.ProfessorId,doctorname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.DoctorId = self.cursor1.fetchone()[0]

        self.conn1.commit()
        
if __name__ == "__main__":
    for i in range(20):
        time.sleep(2)
        a = Pyodbc()
        a.CreateCenter()
        a.CreateAssistant()
        a.CreateSalesman()

        a.CreateProfessor()
        a.CreateDoctor()

# DELETE FROM center WHERE center_name LIKE '运营中心%';
# DELETE FROM assistant WHERE name LIKE '医生助理%';
# DELETE FROM salesman WHERE name LIKE '业务员%';
# DELETE FROM expert_studio WHERE name LIKE '专家%';
# DELETE FROM doctor WHERE name LIKE '医生%';
# DELETE FROM AspNetUsers WHERE username like '沈斌%'