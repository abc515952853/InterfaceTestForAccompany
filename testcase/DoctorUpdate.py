import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random

sheet_name = "DoctorUpdate"

excel = ReadExcl.Xlrd()

@ddt.ddt
class DoctorUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.readdb = ReadDB.Pyodbc()
        self.readconfig=ReadConfig.ReadConfig()

    @classmethod
    def tearDownClass(self):
        self.readdb.DBClose()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_DoctorUpdate(self,data):
        doctorids = list(map(str,str(self.readconfig.get_dynamicdata("Doctors_id")).split(','))) 
        doctorid = int(random.sample(doctorids,1)[0]) 
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'),doctorid)
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])


        experstudioids = list(map(str,str(self.readconfig.get_dynamicdata("expertStudios_id")).split(','))) 
        expertStudioId = int(random.sample(experstudioids,1)[0]) 
        name = str(data['name'])
        phone = str(data['phone'])
        idCard = str(data['idCard'])
        certificate = str(data['certificate'])
        avatar = str(data['avatar'])
        hospital = str(data['hospital'])
        title = str(data['title'])
        department = str(data['department'])
        expertise = str(data['expertise'])
        province = str(data['province'])
        city = str(data['city'])
        county = str(data['county'])
        vitae = str(data['vitae'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "name": name,
            "phone": phone,
            "idCard": idCard,
            "certificate": certificate,
            "avatar": avatar,
            "hospital": hospital,
            "title": title,
            "department": department,
            "expertise": expertise,
            "expertStudioId": expertStudioId,
            "province": province,
            "city": city,
            "county": county,
            "vitae": vitae
            }
        r = requests.put(url=url,data = json.dumps(payload),headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        if r.status_code == 200:
            doctorinfo = self.readdb.GetDoctorInfoById(doctorid)
            if doctorinfo is not None :
                self.assertEqual(doctorinfo['name'],name,case_describe + api)
                self.assertEqual(doctorinfo['phone'],phone,case_describe + api)
                self.assertEqual(doctorinfo['idCard'],idCard,case_describe + api)
                self.assertEqual(doctorinfo['certificate'],certificate,case_describe + api)
                self.assertEqual(doctorinfo['avatar'],avatar,case_describe + api)
                self.assertEqual(doctorinfo['hospital'],hospital,case_describe + api)
                self.assertEqual(doctorinfo['title'],title,case_describe + api)
                self.assertEqual(doctorinfo['department'],department,case_describe + api)
                self.assertEqual(doctorinfo['expertise'],expertise,case_describe + api)
                self.assertEqual(doctorinfo['expertStudioId'],expertStudioId,case_describe + api)
                self.assertEqual(doctorinfo['province'],province,case_describe + api)
                self.assertEqual(doctorinfo['city'],city,case_describe + api)
                self.assertEqual(doctorinfo['county'],county,case_describe + api)
                self.assertEqual(doctorinfo['vitae'],vitae,case_describe + api)
            else:
                self.assertTrue(doctorinfo,msg='数据库数据不存在') 
        self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)