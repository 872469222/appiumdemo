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
time.sleep(7)
# 处理首页弹窗
# el1 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/iv_close")
# el1.click()
# el1 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/tv_countdown")
# el1.click()
# 进入搜索页
time.sleep(3)
driver.implicitly_wait(5)
el1 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/search_flipper")
el1.click()
# 输入关键词搜索--博物馆
time.sleep(3)
driver.implicitly_wait(5)
el3 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/et_search")
el3.send_keys("长沙博物馆")
# 点击博物馆搜索，展示跟博物馆相关的信息
# time.sleep(3)
driver.implicitly_wait(5)
el4 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/tv_name")
el4.click()
# 这段代码进入信用长沙
# driver.find_element_by_class_name("android.widget.LinearLayout").click()
# 进入长沙博物馆首页
time.sleep(3)
# implicitly_wait()方法用来等待页面加载完成（直观的就是浏览器tab页上的小圈圈转完），implicitly_wait(
# 10)，超时时间5s，5秒内一旦加载完成，就执行下一条语句；如果10秒内页面都没有加载完，就超时抛出异常。
driver.implicitly_wait(5)
el4 = driver.find_element_by_xpath("//android.widget.TextView[@text='长沙博物馆']")
el4.click()
# 通过定位到输入框
time.sleep(1)
adb1 = "adb shell input tap 351 1027"
os.system(adb1)
time.sleep(1)
adb2 = "adb shell input tap 966 1147"
os.system(adb2)
time.sleep(2)
# 输入姓名
'adb shell input text ”你好哇“'
