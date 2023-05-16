import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",  # 操作系统
    "deviceName": "OP4ABB",  # 设备 ID
    "platformVersion": "12",  # 设备版本号
    "appPackage": "com.changsha.apps.android.mycs",  # app 包名
    "appActivity": "com.wondersgroup.eshimin.login.activity.WelcomeActivity",  # app 启动时主 Activity\
    'noReset': True,  # 是否保留 session 信息，可以避免重新登录
    'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串r
    'resetKeyboard': False  # 将键盘给隐藏起来
}


# 跑完脚本执行关闭命令
def tearDown(self):
    self.driver.quit()


# os.system('adb kill-server')

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

a = driver.available_ime_engines
if __name__ == '__main__':
    print(a)
