import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random

sheet_name = "ShipmentLogistics"

excel = ReadExcl.Xlrd()

@ddt.ddt
class ShipmentLogistics(unittest.TestCase):
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
    def test_ShipmentLogistics(self,data):
        api = str(data['api']).format(self.readconfig.get_basedata('api_version'))
        case_id = str(data['case_id'])
        session = str(data['session'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        ordernumbers = list(map(str,str(self.readconfig.get_dynamicdata("orders_number")).split(','))) 
        ordernumber = int(random.sample(ordernumbers,1)[0]) 

        logisticsName = str(data['logisticsName'])
        logisticsNumber = str(data['logisticsNumber'])
        shipperName = str(data['shipperName'])
        shippedTime = str(data['shippedTime'])

        # # excel = ReadExcl.Xlrd()

        url = self.readconfig.get_basedata('url_url')+api

        session =  self.readconfig.get_basedata(session)
        requestid = str(uuid.uuid1())
        headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
        payload ={
            "orderNumber":ordernumber,
            "logisticsName":logisticsName,
            "logisticsNumber": logisticsNumber,
            "shipperName": shipperName,
            "shippedTime": shippedTime
            }
        # r = requests.put(url=url,data = json.dumps(payload),headers = headers)

        # # #处理请求数据到excl用例文件
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # excel.save()

        # # if r.status_code == 200:
        # #     self.readdb.GetRoles()
        # # self.assertEqual(r.status_code,expected_code,case_describe + api + r.text)
        print(url,payload)