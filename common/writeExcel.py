import os
import xlrd

from xlutils.copy import copy
class writerExcel(object):
    def __init__(self):
        print("将结果写入")
    try:
        dir = "testData"
        filename = os.path.dirname(os.getcwd()) + "\\" + dir
        print(filename)
        mybook = xlrd.open_workbook(filename + "\\" + "data.xls")
        print(mybook)
        wb = copy(mybook)
        ws = wb.get_sheet(2)
    except FileNotFoundError as msg:
        print(msg)
    def writer(self,id,real,status):
        try:
            print("写入")
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save(self.filename + "\\" + "data.xls")
            return "ok"
        except Exception as msg:
            print(msg)
if __name__ == '__main__':
    a = writerExcel()
    a.writer(3, "0", 'sucees')


