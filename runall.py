
import os
import unittest
import time
import HTMLTestRunner
from common.configEmail import ConfigEmail


def run_case(dir = "testCase"):
    case_dir = os.getcwd() + "\\" + dir
    print(case_dir)
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test_case.py",top_level_dir=None)
    return discover
if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    report_path = os.getcwd() + "\\testReport\\" + current_time + "test_report.html"
    fp = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告",description=u"用例详情")
    runner.run(run_case())
    fp.close()
    
    #发送邮件
    re = ConfigEmail()
    re.send_mail()


