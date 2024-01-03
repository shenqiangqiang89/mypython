# -*- coding: utf-8 -*-
import openpyxl
import requests
import json

url = 'https://w-1.test.betawm.com/Beta.UserTokenExtH5Api/User/Register?AliAppId=111069841'
headers = {
    "Content-Type": "application/json"
}
# 打开Excel文件
workbook = openpyxl.load_workbook('test.xlsx')

# 选择一个工作表
sheet = workbook.active
print('获取每一行的值并打印')
# 获取每一行的值并打印
for row in sheet.iter_rows(values_only=True):
    print(row[1])
    data = {'userId': row[1]}
    payload = json.dumps(data)
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

# 关闭Excel文件
workbook.close()