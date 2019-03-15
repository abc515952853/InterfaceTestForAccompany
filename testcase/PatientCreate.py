import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random

sheet_name = "PatientCreate"

excel = ReadExcl.Xlrd()

@ddt.ddt
class PatientCreate(unittest.TestCase):
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
    def test_PatientCreate(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        doctorids = list(map(str,str(self.readconfig.get_dynamicdata("doctors_id")).split(','))) 
        doctorid = int(random.sample(doctorids,1)[0])

        assistantids = list(map(str,str(self.readconfig.get_dynamicdata("assistants_id")).split(','))) 
        assistantid = int(random.sample(assistantids,1)[0])

        name = str(data['name'])
        phone = str(data['phone'])
        relationship = str(data['relationship'])
        diseases = str(data['diseases'])
        province = str(data['province'])
        city = str(data['city'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "name": name,
            "phone": phone,
            "relationship": relationship,
            "phone": phone,
            "diseases": diseases,
            "province": province,
            "city": city,
            "doctorid": doctorid,
            "assistantid": assistantid,
            }
        # r = requests.post(url=url,data = json.dumps(payload),headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        # # if r.status_code == 200:
        # #     self.readdb.GetRoles()
        #       self.readconfig.append_dynamicdata("assistant_id",str(r.json()['id']))
        # # self.assertEqual(r.status_code,expected_code,case_describe + api)
        print(url,payload)