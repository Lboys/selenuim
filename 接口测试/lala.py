import xlrd

#读取excel文件
def excel():
    wb = xlrd.open_workbook('1024.xlsx')# 打开Excel文件
    sheet = wb.sheet_by_name('content')#通过excel表格名称(rank)获取工作表
    dat = []  #创建空list
    for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                data=str(cells[0])#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
                dat.append(data) #把每次循环读取的数据插入到list
    return dat
a = excel() #返回整个函数的值
print(a)

def test(a):   #a变量传入
    for b in a:  #循环读取a变量list
        print(b)
        return b
test(a)