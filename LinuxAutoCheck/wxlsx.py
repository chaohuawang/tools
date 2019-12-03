#!/usr/bin/env python
#coding=utf-8
import xlsxwriter
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 定义时间标志变量
now= datetime.datetime.today()
print (now)
nowTime = now.strftime('%Y-%m-%d %H:00:00')#现在
print (nowTime)
lastTime = now-datetime.timedelta(hours=1)
print (lastTime)
pastTime = lastTime.strftime('%Y-%m-%d 00:00:00')#过去一小时时间
print (pastTime)

# 定义输出excel文件名
ExcelFileName = 'Monitor.xlsx'
workbook = xlsxwriter.Workbook(ExcelFileName)
# 定义sheet的名字
#worksheet1 = workbook.add_worksheet('双十一检查项')
#worksheet2 = workbook.add_worksheet('业务功能检查')
#worksheet3 = workbook.add_worksheet('落地网关及资源检查')
worksheet4 = workbook.add_worksheet('服务器基础检查')

# 定义sheet中title的字体format
bold = workbook.add_format({'bold': True})
red = workbook.add_format({'fg_color': '#F4B084'})
def getlist():  # 读取hebing.txt
    with open('monitor_hebing.txt', 'r+') as f:
        s1 = f.readlines()
    f.close()
    s2 = []
    for i in s1:
            if '\n' in i:
                    s2.append(i[:-1])
            else:
                    s2.append(i)
    return s2
def fenge():  # 分割
    list0 = []  # 存贮空格行
    for num, val0 in enumerate(getlist()):
        if val0.split(':')[0] == '主机名':
            list0.append(num)
    list0.append(len(getlist()))
    list1 = []   # 存贮内容
    for num1,val1 in enumerate(list0[1:]):
        temp = getlist()[list0[num1]:list0[num1+1]]
        list1.append(temp)
    return list1
    
def wxlsx(worksheetN):   # 写入表格
    worksheet=worksheetN
    title = ['主机名','服务器IP','分区','总空间','使用空间','剩余空间','磁盘使用率','磁盘巡检状态','总内存大小','已用内存','内存剩余大小','内存使用率','内存巡检状态','平均1分钟负载','平均5分钟负载','平均15分钟', '检查人','检查日期','备注']
    for i1, val in enumerate(title):
        worksheet.write(0, i1,val,bold)
#        first_col = worksheet4.col(i1)
#        first_col.width = 180 * 20
    for i2, val2 in enumerate(title):
        for i3, val3 in enumerate(fenge()):
            #print (i3,val3)
            for j in val3:
                #print (j,val2,"<<==")
                if j.split(':')[0] == val2:
                    #print (i2,i3,j.split(':')[1])
                    if j.split(':')[1] == '不正常': #以下判断计划变色使用
                        worksheet.write(i3 + 1, i2, j.split(':')[1],red)
                    else:
                        worksheet.write(i3 + 1, i2, j.split(':')[1] )

wxlsx(worksheet4)
workbook.close()
