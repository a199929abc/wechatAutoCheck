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
        if friend != '微信团队' and friend != '文件传输助手' and friend != 'Z.K.H':
            friends.append(friend)

        # 获取到最后一个好友返回
        if friend == '一只叉烧包':
            global friends_end_flag
            friends_end_flag=False
            return 0
    swipe_up(1/2, 2300)
def is_del(person, count):
    if count == "1":
        time.sleep(1)
        #print('点击微信搜索框')
        driver.find_element_by_id('com.tencent.mm:id/he6').click()
        time.sleep(1)
        #print('在搜索框输入搜索信息')
        driver.find_element_by_id('com.tencent.mm:id/bxz').send_keys(person)
        time.sleep(1)
        #print('点击搜索到的好友')
        driver.find_element_by_id('com.tencent.mm:id/ir3').click()
        # 转账
        time.sleep(2)
        driver.find_element_by_id('com.tencent.mm:id/auj').click()
        #print("点击加号")
        driver.find_element_by_id('com.tencent.mm:id/au0').click()
        time.sleep(2)
        #print("转账中")
        driver.find_elements_by_id('com.tencent.mm:id/rr')[5].click()
        time.sleep(2)
        #print("输入钱数")
        driver.find_element_by_id('com.tencent.mm:id/e64').click()
        time.sleep(2)
        driver.find_element_by_id('com.tencent.mm:id/e6c').click()
        time.sleep(6)
        souce = driver.page_source
        result=check(souce)
        if result==True:
            good_friend.append(person)
            for i in range (0,6):
                driver.keyevent(4)
                sleep(0.5)
        else:
            bad_friend.append(person)
            print("Delete fake friend : ")
            print(person)

        return result
    return
def check(string): 
    sub_str='请输入支付密码'
    if (string.find(sub_str) == -1): 
        print("不存在！")
        driver.find_element_by_id('com.tencent.mm:id/ffp').click()
        delate()
        return False
    else: 
        print("存在！") 
        return True
def delate(): 
    driver.keyevent(4)
    time.sleep(2)
    driver.keyevent(4)  
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/d8').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/h8t').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/d8').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/ijq').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/ffp').click()
    time.sleep(2)
    #click confirm ->tuichu*2->com.tencent.mm:id/d8->com.tencent.mm:id/h8t->com.tencent.mm:id/d8->
    #->	com.tencent.mm:id/ijq->	com.tencent.mm:id/ffp 删除
    return 0

if __name__ == '__main__':
    start_time = time.time()
    good_friend=[]
    bad_friend=[]
    friends_end_flag=True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(6)
    #driver.find_element_by_id('com.tencent.mm:id/dtx').click()
    #login to the wechat
    friends=[]
    i=0
    while(friends_end_flag==True):
        get_friends()
        if(i==54):
            friends_end_flag=False
        i+=1
        print(i)
    friends_set = set(friends)
    print(friends_set)
    print(len(friends_set))
    time.sleep(5)
    for inx, val in enumerate(friends_set):
        return_value=""
        return_value = is_del(val, "1")
    print("Your fake friends are ： ")
    print(*bad_friend, sep = "\n")  
    print("Total: ") 
    print(len(bad_friend))
    print("fake friend")
    print("Total time spend is : ")
    print("--- %s seconds ---" % (time.time() - start_time))