'''
1-导入读取excel的包
2-打开目标文件
3-定位sheet页
4-定位行和列
5-读取数据
6-组装数据
7-retun数据，给需要的数据的地方

'''
#导入读取excel表格的数据

import xlrd
class getExcelData(object):
    def __init__(self):

        #打开目标文件

        readbook = xlrd.open_workbook(r"E:\code\person\lsn2\venv\testData\data.xls")

        #定位sheet页

        self.urlsheet = readbook.sheet_by_name("urlSheet")
        self.paramsheet = readbook.sheet_by_name("paramSheet")
        self.assertsheet = readbook.sheet_by_name("assertSheet")

        #获取最大行数
        self.urlnrows = self.urlsheet.nrows
        self.paramnrows = self.paramsheet.nrows
        self.assertnrows = self.assertsheet.nrows

        #读取数据
    def getsheetData(self,num,sheetname):
        data = []
        for i in range(1,num):
            sheetdata = sheetname.row_values(i)
            data.append(sheetdata)
        return data

    #组装数据
    def assembleDta(self):
        urllist = self.getsheetData(self.urlnrows,self.urlsheet)
        paramlist = self.getsheetData(self.paramnrows,self.paramsheet)
        assertlist = self.getsheetData(self.assertnrows,self.assertsheet)
        dataList = []
        for i in range(len(urllist)):
            new_urllist = urllist[i]
            new_paramlist = paramlist[i][1:]
            new_assertlist = assertlist[i][1:]
            new_urllist.append(new_paramlist)
            new_urllist.append(new_assertlist)
            dataList.append(new_urllist)
        return dataList


c = getExcelData()
c.assembleDta()