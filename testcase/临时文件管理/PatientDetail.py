import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random


sheet_name = "PatientDatail"

excel = ReadExcl.Xlrd()

@ddt.ddt
class PatientDatail(unittest.TestCase):
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
    def test_PatientDatail(self,data):
        patientids = list(map(str,str(self.readconfig.get_dynamicdata("patients_id")).split(','))) 
        patientid = int(random.sample(patientids,1)[0]) 

        api = str(data['api']).format(self.readconfig.get_basedata('api_version'),patientid)
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
            patientinfo = self.readdb.GetPatienInfoById(patientid)
            if patientinfo is not None and len(r.json()) > 0:
                self.assertEqual(patientinfo['name'],r.json()['name'],case_describe + api)
                self.assertEqual(patientinfo['phone'],r.json()['phone'],case_describe + api)
                self.assertEqual(patientinfo['relationship'],r.json()['relationship'],case_describe + api)
                self.assertEqual(patientinfo['phone'],r.json()['phone'],case_describe + api)
                self.assertEqual(patientinfo['diseases'],r.json()['diseases'],case_describe + api)
                self.assertEqual(patientinfo['province'],r.json()['province'],case_describe + api)
                self.assertEqual(patientinfo['city'],r.json()['city'],case_describe + api)
                self.assertEqual(patientinfo['doctorid'],r.json()['doctorid'],case_describe + api)
                self.assertEqual(patientinfo['assistantid'],r.json()['assistantid'],case_describe + api)
            else:
                self.assertTrue(patientinfo,msg='数据库数据不存在') 
                self.assertTrue(r.json(),msg='数据库数据不存在')
        self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)