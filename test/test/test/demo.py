import os
import time
from appium import webdriver
# from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",  # 操作系统
    "deviceName": "OP4ABB",  # 设备 ID
    "platformVersion": "12",  # 设备版本号
    "appPackage": "com.changsha.apps.android.mycs",  # app 包名
    "appActivity": "com.wondersgroup.eshimin.login.activity.WelcomeActivity",  # app 启动时主 Activity\
    'noReset': True,  # 是否保留 session 信息，可以避免重新登录
    # 'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串r
    'resetKeyboard': False  # 将键盘给隐藏起来
}


def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕''' #swipeDown
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕''' #swipeUp
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.25  # 起始y坐标
    y2 = l['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 跑完脚本执行关闭命令
def tearDown(self):
    self.driver.quit()


# os.system('adb kill-server')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# 进入话题广场页面
time.sleep(5)
driver.implicitly_wait(10)
# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/tv_interaction")
el1 = driver.find_element(By.ID, 'com.changsha.apps.android.mycs:id/tv_interaction')
print('进入话题广场页', driver.find_element(By.ID, 'com.changsha.apps.android.mycs:id/tv_interaction'))
el1.click()

if __name__ == '__main__':
    print(driver.get_window_size())
    time.sleep(5)
    swipeUp(driver, n=2)
