import unittest
from HTMLTestRunner import HTMLTestRunner
import datetime
import os
import ReadConfig
from common import Smtp,HTMLTestReportCN

readconfig = ReadConfig.ReadConfig()

class Runtest:
    def __init__(self):
        self.caseListFile = os.path.join(ReadConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(ReadConfig.proDir, "testcase")
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
        

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        suit = self.set_case_suite()

        # if suit is not None:
        #     TextReport='TextReport'+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.html' 
        #     with open(TextReport,'wb') as f:
        #         runner = HTMLTestReportCN.HTMLTestRunner(stream=f,title='Test Report',description='generated by HTMLTestRunner.',verbosity=2)
        #         runner.run(suit) 
            
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suit)

        # smtp = Smtp.Smtp()
        # smtp.add_accessory(TextReport)
        # smtp.send_email()

if __name__ =='__main__':
    obj = Runtest()
    obj.run()