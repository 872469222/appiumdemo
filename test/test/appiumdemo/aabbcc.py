import os
import time
from telnetlib import EC
from appium import webdriver
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "platformName": "Android",  # 操作系统
    "deviceName": "OP4ABB",  # 设备 ID
    "platformVersion": "12",  # 设备版本号
    "appPackage": "com.changsha.apps.android.mycs",  # app 包名
    "appActivity": "com.wondersgroup.eshimin.login.activity.WelcomeActivity",  # app 启动时主 Activity\
    #  "capabilities": "uiautomator2",
    'noReset': True,  # 是否保留 session 信息，可以避免重新登录
    'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串r
    'resetKeyboard': False  # 将键盘给隐藏起来
}


# 跑完脚本执行关闭命令
def tearDown(self):
    self.driver.quit()


# os.system('adb kill-server')
time.sleep(5)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
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


# 去除弹窗
# time.sleep(5)
# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/iv_close")
# el1.click()

# 进入话题广场页面


# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/tv_interaction")
# el1 = driver.find_element(By.ID, 'com.changsha.apps.android.mycs:id/tv_interaction')
# el1 = driver.find_element_by_id('com.changsha.apps.android.mycs:id/tv_interaction')
time.sleep(5)
el1 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/iv_interaction")
el1.click()
print("是否进入话题广场页面", el1)
# 下滑4次
time.sleep(5)
swipeUp(driver, n=4)
# 关注用户
time.sleep(5)
# #el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[2]/android.widget.Button")
el2 = driver.find_element_by_xpath("//android.widget.Button[@text='关注']")
# el4 = driver.find_element_by_xpath("//android.widget.TextView[@text='请选择话题']")

el2.click()
print("关注用户", el2)
# 点击收藏
time.sleep(5)
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                   "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                   "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                   ".View/android.view.View[2]/android.widget.TextView[4]")
el3.click()
# 点击评论 进入评论页面
time.sleep(5)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                   "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                   "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                   ".View/android.view.View[2]/android.widget.TextView[3]")
el4.click()
# 点击写评论 弹出评论框
time.sleep(5)
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                   "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                   "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                   ".View[2]/android.view.View[1]/android.widget.TextView[2]")
el5.click()
# 编写评论（存在senks 输入不了的问题）
time.sleep(5)
# 设置输入法为搜狗

# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[1]")
# 输入评论


if __name__ == '__main__':
    print(driver.get_window_size())
