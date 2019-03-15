import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random

sheet_name = "AccompanyCreate"

excel = ReadExcl.Xlrd()

@ddt.ddt
class AccompanyCreate(unittest.TestCase):
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
    def test_AccompanyCreate(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = str(data['expected_code'])

        patientids = list(map(str,str(self.readconfig.get_dynamicdata("patients_id")).split(','))) 
        patientid = int(random.sample(patientids,1)[0]) 

        content = str(data['content'])
        suggest = str(data['suggest'])
        tags = list(map(str,str(data['tags']).split(',')))
        images = list(map(str,str(data['images']).split(',')))
        scheduleStartTime = str(data['scheduleStartTime'])
        scheduleEndTime = str(data['scheduleEndTime'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "patientid": patientid,
            "content": content,
            "suggest": suggest,
            "tags": tags,
            "images": images,
            "scheduleStartTime": scheduleStartTime,
            "scheduleEndTime": scheduleEndTime
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