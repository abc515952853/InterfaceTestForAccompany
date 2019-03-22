import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid
import random

sheet_name = "AssistantAll"

excel = ReadExcl.Xlrd()

@ddt.ddt
class AssistantAll(unittest.TestCase):
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
    def test_AssistantAll(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        sessiondata = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        key = str(data['key'])
        start = str(data['start'])
        end = str(data['end'])
        
        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(sessiondata)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload = {}
        if len(key) > 0:
            payload["key"]  = key
        if len(start) > 0:
            payload["start"]= start
        if len(end) > 0:
            payload["end"]= end
        r = requests.get(url=url,params = payload,headers = headers)

        # #处理请求数据到excl用例文件
        # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # excel.save()

        if r.status_code == 200:
            if sessiondata == 'session_system':
                assistantinfo = self.readdb.GetAssistantInfoAllByKey(key,start,end)
            else:
                centerid = list(map(str,str(self.readconfig.get_dynamicdata("centers_id")).split(',')))[-1] 
                assistantinfo = self.readdb.GetAssistantInfoAllByKey(key,start,end,centerid)
            if assistantinfo is not None and len(r.json()) > 0:
                responeassistantid = []
                for i in range(len(r.json())):
                    responeassistantid.append(r.json()[i]['id'])
                    self.assertIn(int(r.json()[i]['id'].upper()),assistantinfo,case_describe + api)
                self.assertEqual(len(assistantinfo),len(responeassistantid),case_describe + api)
            else:
                self.assertFalse(r.json(),msg='返回数据有误') 
                self.assertFalse(assistantinfo,msg='数据库数据有误') 
        self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)