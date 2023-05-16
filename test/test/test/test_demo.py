import os
import time
from telnetlib import EC
# from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
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


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', "desired_caps")
driver.implicitly_wait(10)


# 跑完脚本执行关闭命令
def tearDown(self):
    self.driver.quit()


# os.system('adb kill-server')


def swipeUp(driver, t=500, n=1):
    """向上滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    """向下滑动屏幕"""
    l = driver.get_window_size()
    #  x1 = l['width'] * 0.5  # x坐标
    x1 = l['width'] * 5000.5  # x坐标
    # y1 = l['height'] * 0.25  # 起始y坐标
    y1 = l['height'] * 5000.55  # 起始y坐标
    # y2 = l['height'] * 0.75  # 终点y坐标
    y2 = l['height'] * 5000.85  # 终点y坐标
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


driver.implicitly_wait(5)

# 去除弹窗
# time.sleep(5)
# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/iv_close")
# el1.click()

# 进入话题广场页面
time.sleep(5)
driver.implicitly_wait(10)
# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/tv_interaction")
el1 = driver.find_element(By.ID, 'com.changsha.apps.android.mycs:id/tv_interaction')
print("是否进入话题广场页面", el1)
el1.click()
# 下滑
driver.swipe(200, 800, 200, 100, 2000);
# 关注用户/点赞/评论
# time.sleep(3)
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[2]/android.widget.Button")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[2]/android.widget.TextView[3]")
# el3.click()
# el4 = driver.find_element_by_id("com.changsha.apps.android.mycs:id/iv_mine")
# el4.clear()

if __name__ == '__main__':
    print(driver.get_window_size())
    time.sleep(5)
