import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 

sheet_name = "ExpertStudioCreate"

excel = ReadExcl.Xlrd()

@ddt.ddt
class ExpertStudioCreate(unittest.TestCase):
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
    def test_ExpertStudioCreate(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        phone = str(data['phone'])
        name = str(data['name'])
        avatar = str(data['avatar'])
        hospital = str(data['hospital'])
        title = str(data['title'])
        province = str(data['province'])
        city = str(data['city'])
        county = str(data['county'])
        expertise = str(data['expertise'])
        vitae = str(data['vitae'])
        remark = str(data['remark'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "phone": phone,
            "name": name,
            "avatar": avatar,
            "hospital": hospital,
            "title": title,
            "province": province,
            "city": city,
            "county": county,
            "expertise": expertise,
            "vitae": vitae,
            "remark": remark
            }
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        if r.status_code == 200:
            expertstudioinfo = self.readdb.GetExpertstudioInfoByName(name)
            if expertstudioinfo is not None:
                self.assertEqual(expertstudioinfo['phone'],phone,case_describe + api)
                self.assertEqual(expertstudioinfo['name'],name,case_describe + api)
                self.assertEqual(expertstudioinfo['avatar'],avatar,case_describe + api)
                self.assertEqual(expertstudioinfo['hospital'],hospital,case_describe + api)
                self.assertEqual(expertstudioinfo['title'],title,case_describe + api)
                self.assertEqual(expertstudioinfo['province'],province,case_describe + api)
                self.assertEqual(expertstudioinfo['city'],city,case_describe + api)
                self.assertEqual(expertstudioinfo['county'],county,case_describe + api)
                self.assertEqual(expertstudioinfo['expertise'],expertise,case_describe + api)
                self.assertEqual(expertstudioinfo['vitae'],vitae,case_describe + api)
                self.assertEqual(expertstudioinfo['remark'],remark,case_describe + api)
                self.readconfig.append_dynamicdata("expertstudios_id",expertstudioinfo['expert_studio_id'])
            else:
                self.assertTrue(expertstudioinfo,msg='数据库数据不存在') 
        self.assertEqual(r.status_code,expected_code,case_describe + api)