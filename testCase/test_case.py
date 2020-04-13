from common.configHttp import ConfigHttp
from common.readExcel import getExcelData
from common.writeExcel import writerExcel
import unittest,json
from ddt import ddt,data,unpack
import HTMLTestRunner
import time,os

wr = writerExcel()
re = ConfigHttp()
excelData = getExcelData()
test_data = excelData.assembleDta()

@ddt
class MytestCase(unittest.TestCase):
    
    @ddt
    @data(*test_data)
    @unpack
    def test_request(self,id,url,name,method,param,expect):
        print(id,url,name,method,param,expect)
        param = param[0]
        expect = expect[0]
        real = re.getRequest(method,url,param)
        print("kankanleixing ",type(real))
        try:
            status = self.assertEqual(real,int(expect))
            print(status)
        except AssertionError as msg:
            status = "Error"
        finally:
            if status == None:
                wr.writer(int(id),real,"Success")
            else:
                wr.writer(int(id),real,"Faile")

if __name__ == '__main__':
    unittest.main()


