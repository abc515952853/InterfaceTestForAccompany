import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import json 

apiversion = 'api/AppVersion'
apiread = 'api/AppVersion/{0}/Read'

sheet_name = "AppVersion"

excel = ReadExcl.Xlrd()


@ddt.ddt
class AppVersion(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.readdb = ReadDB.Pyodbc()
        # self.readconfig=ReadConfig.ReadConfig()

        # self.readdb.DBDelete("[member]")

    # @classmethod
    # def tearDownClass(self):
        # self.readdb.DBClose()

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_AppVersion(self,data):
        self.readdb.GetCustomer()

