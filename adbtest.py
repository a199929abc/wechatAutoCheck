import os
import unittest
from appium import webdriver
from time import sleep
import time

desired_caps = {
    "platformName": "Android", # 系统
    "platformVersion": "10.0", # 系统本号
    "deviceName": "ELE_AL00", # 设备名
    "appPackage": "com.tencent.mm", # 包名
    'unicodeKeyboard': False,
    "appActivity": ".ui.LauncherUI", # app 启动时主 Activity
    'noReset': True # 保留 session 信息，可以避免重新登录
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

def swipe_up(distance, time):  #distance为滑动距离，time为滑动时间
    width = 1080
    height = 2340  # width和height根据不同手机而定
    driver.swipe(1 / 2 * width, 9 / 10 * height, 1 / 2 * width, (9 / 10 - distance) * height, time)
friends = []
def get_friends():
    # 好友id
    friend=''
    address_list=''
    address_list = driver.find_elements_by_id('com.tencent.mm:id/ft6')
    for address in address_list:
        # 昵称
        friend = address.get_attribute('text')
        # 过滤掉自己、微信团队、文件夹传输助手
        if friend != '微信团队' and friend != '文件夹传输助手':
            friends.append(friend)
    
        # 获取到最后一个好友返回
      #  if friend == '🌀 一只叉烧包 nn':
        #    return

for i in range(0,60):
    get_friends()
    driver.swipe(100, 1000, 100, 100)
new_lst = []
for k in friends:
    if k not in new_lst:
        new_lst.append(k)
print(len(new_lst))             
print(*new_lst, sep='\n')
