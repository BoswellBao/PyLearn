# import xlrd
# import os
# base_path=os.path.dirname(__file__)
# print(os.path.dirname(__file__))
# file_path=os.path.join(base_path,'getChannal.xls')
# rf=xlrd.open_workbook(file_path,'r')
# table=rf.sheet_by_name('getTVChannal')
# rownum=table.nrows
# colnum=table.ncols
# print(rownum,colnum)
# for i in table.row_values(0): print(i)
# print(table.row_values(0))
# excel_data = [rownum - 1]
# for i in range(rownum):
#     excel_data.append(table.row_values(i))
# print(excel_data[2][3])
# for i in excel_data:print(i)#读excel简单一个循环，一个一维数组append，关键是下面的ddt用法

# import ddt
# import unittest
# from ddtExp import DataPro
# @ddt.ddt
# class testDDT(unittest.TestCase):
#     a=DataPro()
#     datalist=a.data_pro()
#     arr=[2]
#     a=datalist.__len__()
#     print(a)
#     for i in range(a):arr.append(datalist[i])#可行的，明天开始写下去
#     for i in arr:print(i)
#     @ddt.data(arr)
#     @ddt.unpack
#     def test_ddt(self,para1,para2):
#         print(para1,para2)
#
# if __name__ == '__main__':
#     unittest.main()

import os
import xlwt
import xlrd
from xlutils.copy import copy

rf = xlrd.open_workbook( os.path.join(os.path.dirname(__file__), 'getChannal.xls'))
wf = copy(rf)
print(type(wf))
index = wf.sheet_index('getTVChannal')
wt_sheet = wf.get_sheet(index)
print(type(wt_sheet))


# a = xlwt.Workbook()
# a.

