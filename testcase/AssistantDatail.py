import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random


sheet_name = "AssistantDatail"

excel = ReadExcl.Xlrd()

@ddt.ddt
class AssistantDatail(unittest.TestCase):
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
    def test_AssistantDatail(self,data):
        assistants = list(map(str,str(self.readconfig.get_dynamicdata("assistants_id")).split(','))) 
        assistant = int(random.sample(assistants,1)[0]) 

        api = str(data['api']).format(self.readconfig.get_basedata('api_version'),assistant)
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        r = requests.get(url=url,headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        print(r.json())
        if r.status_code == 200:
            assistantinfo = self.readdb.GetAssistanctInfoById(r.json()['id'])
            if assistantinfo is not None and len(r.json()) > 0:
                self.assertEqual(assistantinfo['center_id'],int(r.json()['centerId']),case_describe + api)
                self.assertEqual(assistantinfo['job_number'],r.json()['jobNumber'],case_describe + api)
                self.assertEqual(assistantinfo['name'],r.json()['name'],case_describe + api)
                self.assertEqual(assistantinfo['phone'],r.json()['phone'],case_describe + api)
                self.assertEqual(assistantinfo['avatar'],r.json()['avatar'],case_describe + api)
                # self.assertEqual(assistantinfo['patient_number'],r.json()['patient_number'],case_describe + api)
                # self.assertEqual(assistantinfo['doctor_number'],r.json()['doctor_number'],case_describe + api)
            else:
                self.assertTrue(assistantinfo,msg='数据库数据不存在') 
                self.assertTrue(r.json(),msg='数据库数据不存在')
        self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)