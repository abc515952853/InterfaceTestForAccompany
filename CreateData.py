import pyodbc
import json
import uuid
import time
import random
import datetime

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


        self.peibanid = ['e73358d1-369a-45a0-8c4e-e5f445a21769','c542ab7d-89c4-438e-b500-0ac67f093c0f','17d720c0-b3f2-4a7a-95f8-9071cc891536']


    def CreateCenter(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]						
        name = '沈斌'+num
        centername = '运营中心'+ num
        username = 'yyzx' + num
        phone = '18511'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'7b98adb4-2daf-4c59-a9fa-21d5649a722c')
        self.cursor2.execute(sql)
        self.conn2.commit()


        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `center`(`user_id`, `center_name`, `principal_name`, `phone`, `province`, `city`, `county`, `agent_number`,`username`)\
         VALUES ('{0}','{1}','{2}','{3}','浙江省','杭州市','滨江区','{4}','{5}')".format(userid,centername,name,phone,uuid.uuid1(),username)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.Centerid = self.cursor1.fetchone()[0]

        self.conn1.commit()

    
    def CreateAssistant(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]						
        name = '沈斌'+num
        assistantname = '医生助理'+ num
        phone = '18502'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'8b6ad8cb-4389-4f4b-8187-34c18a4e7743')
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `assistant`(user_id,`center_id`, `job_number`, `name`, `phone`, `state`,`patient_number`, `doctor_number`) \
        VALUES ('{0}','{1}','{2}','{3}',{4},1,0,0)".format(userid,self.Centerid,num,assistantname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.AssistantId = self.cursor1.fetchone()[0]

        self.conn1.commit()  


    def CreateSalesman(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]							
        name = '沈斌'+num
        Salesmanname = '业务员'+ num
        phone = '18503'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'4d0eace6-11ec-49a0-a83f-5916011a2f97')
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `salesman`(`user_id`, `center_id`, `name`, `phone`, `state`) \
        VALUES ('{0}','{1}','{2}','{3}',1)".format(userid,self.Centerid,Salesmanname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.SalesmanId = self.cursor1.fetchone()[0]

        self.conn1.commit()  


    def CreateProfessor(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]							
        name = '沈斌'+num
        Professorname = '专家'+ num
        phone = '13801'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'0b0c71af-f951-4699-82e4-fd15537cae5c')
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `expert_studio`(`user_id`, `name`, `phone`, `hospital`, `title`, `province`, `city`, `county`, `expertise`, `vitae`) \
        VALUES ('{0}','{1}','{2}','浙一医院','主任医师','浙江省','杭州市','滨江区','各种癌症','50年临床经验')".format(userid,Professorname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.ProfessorId = self.cursor1.fetchone()[0]

        self.conn1.commit()

    def CreateDoctor(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]							
        name = '沈斌'+num
        doctorname = '医生'+ num
        phone = '13802'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'39d0da62-2528-4ce8-b0b8-5e3e8911e7e0')
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `doctor`(`user_id`, `expert_studio_id`, `name`, `phone`, `id_card`, `patients_number`)\
         VALUES ('{0}','{1}','{2}','{3}','330102198909286523',0)".format(userid,86,doctorname,phone)

        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.DoctorId = self.cursor1.fetchone()[0]

        self.conn1.commit()

    def CreateMeberPatient(self):
        userid = uuid.uuid1()
        t = time.time()
        num = str(int(round(t)))[-6:]						
        name = '会员患者'+num
        doctorname = '会员患者'+ num
        phone = '12702'+num
        sql = "INSERT INTO `AspNetUsers`(`Id`, `UserName`,`EmailConfirmed`, `PhoneNumberConfirmed`, `TwoFactorEnabled`,`LockoutEnabled`, `AccessFailedCount`,`PhoneNumber`,`SecurityStamp`,`ConcurrencyStamp`) VALUES ('{0}','{1}',0,1,1,0,0,'{2}','WBOKYTVIRSA3KD4KEF45YAJSUM7Y47G2','70d1970c-4c46-11e9-bbba-0242ac144502')".format(userid,phone,phone)
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `AspNetUserRoles`(`UserId`, `RoleId`) VALUES ('{0}','{1}')".format(userid,'9d6f62a3-1fee-4669-89d6-38a5e4f81b57')
        self.cursor2.execute(sql)
        self.conn2.commit()

        sql = "INSERT INTO `account`(`user_id`, `name`, `money_in`, `money_out`, `freeze_money_in`, `freeze_money_out`, `consume_money_in`, `consume_money_out`, `row_version`) \
        VALUES ('{0}','{1}',0,0,0,0,0,0,'1')".format(userid,name)
        self.cursor1.execute(sql)
        self.conn1.commit()

        sql = "INSERT INTO `member`(`user_id`, `center_id`, `salesman_id`, `name`, `phone`, `start_time`, `end_time`, `create_time`, `state`,`pause_operator_id`, `pause_operator_name`) \
        VALUES('{0}',112,76,'{1}','{2}','2019-03-21 02:51:21','2020-03-21 02:51:21','2019-03-21 02:51:21',1,'11','11')".format(userid,name,phone)
        self.cursor1.execute(sql)
        self.cursor1.execute('SELECT @@IDENTITY')
        self.MemberId = self.cursor1.fetchone()[0]
        self.conn1.commit()

        sql = "INSERT INTO `patient`(`member_id`, `doctor_id`, `assistant_id`, `name`, `phone`, `gender`, `birthday`,`province`, `city`, `county`, `diseases`)\
         VALUES ('{0}',123,76,'{1}','{2}',1,'1980-03-21 02:51:21','浙江省','杭州市','滨江区','直肠癌')".format(self.MemberId,name,phone)
        self.cursor1.execute(sql)
        self.cursor1.execute('SELECT @@IDENTITY')
        self.Patientid = self.cursor1.fetchone()[0]
        self.conn1.commit()

        self.userid = userid

        # print(self.userid,self.MemberId,self.Patientid)

    def CreateSchedule(self):
        state = int(random.sample([0,1,2],1)[0])
        sql = "INSERT INTO `schedule`(`patient_id`, `user_id`, `start_time`, `end_time`, `creator_id`, `creator`, `create_time`, `state`, `finish_time`) \
        VALUES ('{0}','{1}','2019-03-21 02:51:21','2019-03-21 05:51:21',76,'医生助理38110','2019-03-21 02:51:21',{2},'2019-03-21 05:51:21')".format(self.Patientid,self.userid,state)
        self.cursor1.execute(sql)
        self.cursor1.execute('SELECT @@IDENTITY')
        self.Scheduleid = self.cursor1.fetchone()[0]
        self.conn1.commit()

        if state == 2:
            state = 0
            sql = "INSERT INTO `schedule`(`patient_id`, `user_id`, `start_time`, `end_time`, `creator_id`, `creator`,`state`, `finish_time`) \
            VALUES ('{0}','{1}','2019-03-21 02:51:21','2019-03-21 05:51:21',76,'医生助理38110',{2},'2019-03-21 05:51:21')".format(self.Patientid,self.userid,state)
            self.cursor1.execute(sql)
            self.conn1.commit()
            self.CreateAccompany()
    
    def CreateAccompany(self):
        sql = "INSERT INTO `accompany`(`patient_id`, `user_id`, `schedule_id`, `name`,`content`, `suggest`, `tags`, `images`, `state`, `remark`) \
        VALUES ('{0}','{1}','{2}','医生助理38110','content111','suggest22222','[1],[2]','1.jpg',1,'remark333')".format(self.Patientid,self.userid,self.Scheduleid)
        self.cursor1.execute(sql)
        self.conn1.commit()


    def CreateBonus(self):
        id = random.sample(self.peibanid,1)[0]
        state = random.sample([1,0],1)[0]
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO `bonus_list`(`bonus_id`, `user_id`, `name`, `money`, `create_time`, `state`, `order_number`) \
        VALUES (5,'{0}','奖金',100,'{1}','{2}','111111')".format(id,nowtime,state,)
        self.cursor1.execute(sql)

        self.cursor1.execute('SELECT @@IDENTITY')
        self.bonus_id = self.cursor1.fetchone()[0]

        self.conn1.commit()


    def CreateAccount(self):
        id = random.sample(self.peibanid,1)[0]
        direction = random.sample([1,0],1)[0]
        account_type = random.sample([1,2,3],1)[0]
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO `account_list`(`user_id`, `title`, `before_money`, `money`, `balance`, `direction`, `create_time`, `account_type`, `business_type`, `remark`)\
         VALUES ('{0}','奖励明细',100,100,100,{1},'{2}',{3},0,'巴拉巴拉巴拉')".format('17d720c0-b3f2-4a7a-95f8-9071cc891536',direction,nowtime,account_type)
        self.cursor1.execute(sql)
        self.conn1.commit()
    
    def test(self):
        t = time.time()
        num = str(int(round(t)))[-6:]
        print(num)


        
if __name__ == "__main__":
    for i in range(100):
        time.sleep(2)
        a = Pyodbc()
        # a.CreateCenter()
        # a.CreateAssistant()
        # a.CreateSalesman()

        # a.CreateProfessor()
        # a.CreateDoctor()


        # a.CreateMeberPatient()
        # a.CreateSchedule()

        # a.CreateBonus()

        # a.CreateAccount()
        a.test()

# DELETE FROM center WHERE center_name LIKE '运营中心%';
# DELETE FROM assistant WHERE name LIKE '医生助理%';
# DELETE FROM salesman WHERE name LIKE '业务员%';
# DELETE FROM expert_studio WHERE name LIKE '专家%';
# DELETE FROM doctor WHERE name LIKE '医生%';
# DELETE FROM AspNetUsers WHERE username like '沈斌%'