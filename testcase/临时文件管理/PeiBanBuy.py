import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json
import uuid 
import random

sheet_name = "PeiBanBuy"

excel = ReadExcl.Xlrd()

@ddt.ddt
class DoctorCreate(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
        # self.readdb = ReadDB.Pyodbc()
        # self.readconfig=ReadConfig.ReadConfig()

    @classmethod
    def tearDownClass(self):
        pass
        # self.readdb.DBClose()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_DoctorCreate(self,data):
        url = str(data['api'])
        case_id = str(data['case_id'])
        case_describe = str(data['case_describe'])
        expected_code = int(data['expected_code'])

        IsCenterBuy = bool(data["IsCenterBuy"])
        PeibanOrderNumber = str(data["PeibanOrderNumber"])
        Quantity = int(data['Quantity'])
        ReceiveStreet = str(data['ReceiveStreet'])
        ReceiveProvince = str(data['ReceiveProvince'])
        ReceiveCity = str(data['ReceiveCity'])
        ReceivePhone = str(data['ReceivePhone'])
        ReceiveCounty = str(data['ReceiveCounty'])
        ReceiveName = str(data['ReceiveName'])
        StoreNumber = str(data['StoreNumber'])

        # # excel = ReadExcl.Xlrd()

        headers = {'Content-Type': "application/json"}
        payload ={
            "IsCenterBuy":IsCenterBuy,
            "PeibanOrderNumber":PeibanOrderNumber,
            "Quantity":Quantity,
            "ReceiveStreet":ReceiveStreet,
            "ReceiveProvince":ReceiveProvince,
            "ReceiveCity":ReceiveCity,
            "ReceivePhone":ReceivePhone,
            "ReceiveCounty":ReceiveCounty,
            "ReceiveName":ReceiveName,
            "StoreNumber":StoreNumber
            }
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)

        # # # #处理请求数据到excl用例文件
        # # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        # # # excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        # # # excel.save()

        # if r.status_code == 200:
        #     print(r.status_code)