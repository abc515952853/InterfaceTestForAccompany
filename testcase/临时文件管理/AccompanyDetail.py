import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random


sheet_name = "AccompanyDetail"

excel = ReadExcl.Xlrd()

@ddt.ddt
class AccompanyDetail(unittest.TestCase):
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
    def test_AccompanyDetail(self,data):
        accompanyids = list(map(str,str(self.readconfig.get_dynamicdata("accompanys_id")).split(','))) 
        accompanyid = int(random.sample(accompanyids,1)[0]) 

        api = str(data['api']).format(self.readconfig.get_basedata('api_version'),accompanyid)
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

        if r.status_code == 200:
            Accompanyinfo = self.readdb.GetAccompanyinfoById(id)
            if Accompanyinfo is not None and len(r.json()) > 0:
                self.assertEqual(Accompanyinfo['patientid'],r.json()['patientid'],case_describe + api)
                self.assertEqual(Accompanyinfo['content'],r.json()['content'],case_describe + api)
                self.assertEqual(Accompanyinfo['suggest'],r.json()['suggest'],case_describe + api)
                self.assertEqual(Accompanyinfo['tags'],r.json()['tags'],case_describe + api)
                self.assertEqual(Accompanyinfo['images'],r.json()['images'],case_describe + api)
                self.assertEqual(Accompanyinfo['scheduleStartTime'],r.json()['scheduleStartTime'],case_describe + api)
                self.assertEqual(Accompanyinfo['scheduleEndTime'],r.json()['scheduleEndTime'],case_describe + api)
            else:
                self.assertTrue(Accompanyinfo,msg='数据库数据不存在') 
                self.assertTrue(r.json(),msg='数据库数据不存在')
        self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)