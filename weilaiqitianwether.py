# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:47:19 2018

@author: lenovo
"""

import urllib.request as r
import json
print("欢迎使用全球天气app")
city= input('请输入城市拼音：')
address='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'

info = r.urlopen(address.format(city)).read().decode('utf-8','ignore')
print(info)
data=json.loads(info)

print("1.查看当前城市天气 2.查看其它城市天气 3.保存当前城市天气")
menno = input("请输入菜单：")
if menno == '1':
    print('1.查看当前城市天气')
if menno == '2':
    print('2.查看其它城市天气')
if menno == '3':
    print('3.保存当前城市天气')
list=data['list']
diyitian=list[0]
diertian=list[1]
disantian=list[2]
disitian=list[3]
diwutian=list[4]
diliutian=list[5]
diqitian=list[6]


print(diyitian['weather'][0]['description'])

print('第一天的天气为：'+'\n'
      '时间:' + str(diyitian['dt_txt']) + '\n'
      +'温度:' + str(diyitian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度:' + str(diyitian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(diyitian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(diyitian['weather'][0]['description']) + '\n'
      +'气压：' + str(diyitian['main']['pressure']) + 'P'
      )
print('........................')

print('第二天的天气为：'+'\n'
      '时间：' + str(diertian['dt_txt']) + '\n'
      +'温度：' + str(diertian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(diertian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(diertian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(diertian['weather'][0]['description']) + '\n'
      +'气压：' + str(diertian['main']['pressure']) + 'P'
      )
print('........................')

print('第三天的天气为：'+'\n'
      '时间：' + str(disantian['dt_txt']) + '\n'
      +'温度：' + str(disantian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(disantian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(disantian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(disantian['weather'][0]['description']) + '\n'
      +'气压：' + str(disantian['main']['pressure']) + 'P'
      )

print('........................')



print('第四天的天气为：'+'\n'
      '时间：' + str(disitian['dt_txt']) + '\n'
      +'温度：' + str(disitian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(disitian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(disitian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(disitian['weather'][0]['description']) + '\n'
      +'气压：' + str(disitian['main']['pressure']) + 'P'
      )

print('........................')



print('第五天的天气为：'+'\n'
      '时间：' + str(diwutian['dt_txt']) + '\n'
      +'温度：' + str(diwutian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(diwutian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(diwutian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(diwutian['weather'][0]['description']) + '\n'
      +'气压：' + str(diwutian['main']['pressure']) + 'P'
      )

print('........................')

print('第六天的天气为：'+'\n'
      '时间：' + str(diliutian['dt_txt']) + '\n'
      +'温度：' + str(diliutian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(diliutian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度：' + str(diliutian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气：' + str(diliutian['weather'][0]['description']) + '\n'
      +'气压：' + str(diliutian['main']['pressure']) + 'P'
      )

print('........................')

print('第七天的天气为：'+'\n'
      '时间：' + str(diqitian['dt_txt']) + '\n'
      +'温度：' + str(diqitian['main']['temp']) + '摄氏度' + '\n'
      +'最高温度：' + str(diqitian['main']['temp_max']) + '摄氏度' + '\n'
      +'最低温度:' + str(diqitian['main']['temp_min']) + '摄氏度' + '\n'
      +'天气:' + str(diqitian['weather'][0]['description']) + '\n'
      +'气压:' + str(diqitian['main']['pressure']) + 'P'
      )

print('........................')