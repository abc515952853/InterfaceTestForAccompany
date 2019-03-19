import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 

sheet_name = "MemberCreate"

excel = ReadExcl.Xlrd()

@ddt.ddt
class MemberCreate(unittest.TestCase):
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
    def test_MemberCreate(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])


        name = str(data['name'])
        phone = str(data['phone'])
        startTime = str(data['startTime'])
        endTime = str(data['endTime'])
        state = str(data['state'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "name": name,
            "phone": phone,
            "startTime":startTime,
            "endTime":endTime,
            "state":state
            }
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        if r.status_code == 200:
            memberinfo = self.readdb.GetmemberInfoByPhone(phone)
            if memberinfo is not None:
                self.assertEqual(memberinfo['name'],name,case_describe + api)
                self.assertEqual(memberinfo['phone'],phone,case_describe + api)
                self.assertEqual(memberinfo['startTime'],startTime,case_describe + api)
                self.assertEqual(memberinfo['endTime'],endTime,case_describe + api)
                self.assertEqual(memberinfo['state'],state,case_describe + api)
                self.readconfig.append_dynamicdata("members_id",memberinfo['member_id'])
            else:
                self.assertTrue(memberinfo,msg='数据库数据不存在') 
        self.assertEqual(r.status_code,expected_code,case_describe + api)