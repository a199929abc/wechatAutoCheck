import os
from string import Template
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


def swipe_up(distance, time):  #distance为滑动距离，time为滑动时间
    width = 1080
    height = 2340  # width和height根据不同手机而定
    driver.swipe(1 / 2 * width, 9 / 10 * height, 1 / 2 * width, (9 / 10 - distance) * height, time)

def get_friends():
    # 好友id
    address_list=''
    address_list = driver.find_elements_by_id('com.tencent.mm:id/ft6')
    for address in address_list:
        # 昵称
        friend=''
        friend = address.get_attribute('text')
        # 过滤掉自己、微信团队、文件夹传输助手
        if friend != '微信团队' and friend != '文件夹传输助手':
            friends.append(friend)

        # 获取到最后一个好友返回
        if friend == '一只叉烧包':
            global friends_end_flag
            friends_end_flag=False
            return 0
    swipe_up(1/2, 2000)
def is_del(person, count):
    if count == "1":
        time.sleep(2)
        print('点击微信搜索框')
        driver.find_element_by_id('com.tencent.mm:id/he6').click()
        time.sleep(2)
        print('在搜索框输入搜索信息')
        driver.find_element_by_id('com.tencent.mm:id/bxz').send_keys(person)
        time.sleep(2)
        print('点击搜索到的好友')
        driver.find_element_by_id('com.tencent.mm:id/ir3').click()
        # 转账
        driver.find_element_by_id('com.tencent.mm:id/auj').click()
        print("点击加号")
        driver.find_element_by_id('com.tencent.mm:id/au0').click()
        time.sleep(2)
        print("转账中")
        driver.find_elements_by_id('com.tencent.mm:id/rr')[5].click()
        print("输入钱数")
        driver.find_element_by_id('com.tencent.mm:id/e64').click()
        time.sleep(2)
        driver.find_element_by_id('com.tencent.mm:id/e6c').click()
        time.sleep(10)
        souce = driver.page_source
        result=check(souce,'请输入支付密码')
        if result==True:
            good_friend.append(person)
        else:
            bad_friend.append(person)
        return result
    return
def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("不存在！") 
        return False
    else: 
        print("存在！") 
        return True
 
def search_back():
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/dn').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/rs').click()
    time.sleep(2)
    # 清除搜索框，输入下一个
    driver.find_element_by_id('com.tencent.mm:id/fsv').click()
if __name__ == '__main__':
    good_friend=[]
    bad_friend=[]
    friends_end_flag=True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)
    #login to the wechat
    friends=[]
    i=0
    while(friends_end_flag==True):
        get_friends()
        if(i==1):
            friends_end_flag=False
        i+=1
    friends_set = set(friends)
    print(friends_set)
    print(len(friends_set))
    time.sleep(5)
    for inx, val in enumerate(friends_set):
        return_value=""
        if inx == 0:
            return_value = is_del(val, "1")
        else:
            return_value = is_del(val, "")
        print("we are good friend : " +val)
