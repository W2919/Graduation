# -*- coding: utf-8 -*-
# @Time   : 2025/1/18 21:09
# @Author : WWEE
# @File   : test.py
import requests

# 免费API示例：ipinfo.io
response = requests.get("https://ipinfo.io/")
data = response.json()

# 提取位置信息
location = data  # 经纬度字符串，格式为 "latitude,longitude"
print(f"经纬度: {location}")