import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 

sheet_name = "SystemLogin"

excel = ReadExcl.Xlrd()

@ddt.ddt
class SystemLogin(unittest.TestCase):
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
    def test_SystemLogin(self,data):
        url = 'http://identity.c4b102e69d03f4720a18035cb3ac0dcea.cn-beijing.alicontainer.com/connect/token'
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        username = str(data['username'])
        password = str(data['password'])

        excel = ReadExcl.Xlrd()

        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {
            "client_id":"js",
            "grant_type":"password",
            "client_secret":"ab5bb959b8e34614ae745ddebd15e2a7",
            "username":username,
            "password":password
        }
        r = requests.post(url=url,data = payload,headers = headers)

        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()

        if r.status_code == 200:
                session = r.json()["token_type"]+" "+r.json()["access_token"]
                self.readconfig.set_basedata('session_system',session)
        self.assertEqual(r.status_code,expected_code,case_describe + ",接口：connect/token")   
        
        
