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
    # 'automationName': 'UiAutomator1',
    'noReset': True,  # 是否保留 session 信息，可以避免重新登录
    'unicodeKeyboard': False,  # 使用 unicodeKeyboard 的编码方式来发送字符串r
    'resetKeyboard': True  # 将键盘给隐藏起来
}


# 跑完脚本执行关闭命令
def tearDown(self):
    self.driver.quit()


# os.system('adb kill-server')
# 连接Appium Server，初始化自动化环境
time.sleep(5)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 设置搜过为默认输入法
# 'com.sohu.inputmethod.sogouoem/.SogouIME'


def swipeUp(driver, t=500, n=1):
    """向上滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.75  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    """向下滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.25  # 起始y坐标
    y2 = l['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipLeft(driver, t=500, n=1):
    """向左滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swipRight(driver, t=500, n=1):
    """向右滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 去除弹窗
time.sleep(5)
# el1 = driver.find_element(By.ID, "com.changsha.apps.android.mycs:id/iv_close")
# el1.click()
# print("去除弹窗", el1)

# 进入话题广场页面
time.sleep(5)
el1 = driver.find_element(By.ID, 'com.changsha.apps.android.mycs:id/tv_interaction')
el1.click()
print("是否进入话题广场页面", el1)
# 下滑4,5,6,7,8次
time.sleep(5)
swipeUp(driver, n=8)
# 关注用户
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[2]/android.widget.Button")
# el2 = driver.find_element(By.CLASS_NAME, "//android.widget.Button[@text='关注']")
time.sleep(10)
driver.implicitly_wait(10)
el2 = driver.find_element(By.XPATH, '//android.widget.Button')
# el2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                     ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                     "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                     "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                     ".View[2]/android.view.View[2]/android.widget.Button")
el2.click()
# # el2 = driver.find_element_by_xpath("//android.widget.Button[@text='关注']")
# el2 = driver.find_element(By.,"//android.widget.Button[@text='关注']")
# el2.click()
print("关注用户", el2)
# 点击收藏
time.sleep(5)
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View/android.view.View[2]/android.widget.TextView[4]")
el3 = driver.find_element(By.XPATH, "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                    ".View/android.view.View[2]/android.widget.TextView[4]")
el3.click()
print("点击收藏", el3)

# 点击评论 进入评论页面
time.sleep(5)
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View/android.view.View[2]/android.widget.TextView[3]")
el4 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                    ".View/android.view.View[2]/android.widget.TextView[3]")
el4.click()
print("进入评论页面", el4)
# 点击写评论 弹出评论框
time.sleep(5)
# el5 = driver.find_element(By.XPATH, "//android.widget.TextView[@text='评论']")
# el5.click()

el5 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                    ".View[2]/android.view.View[1]")
# el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
#                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
#                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
#                                    ".View[2]/android.view.View[1]/android.widget.TextView[2]")
el5.click()
print("点击弹窗，弹出评论框", el5)
time.sleep(5)
el6 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                    ".View[2]/android.view.View[1]")
el6.click()

# 编写评论（存在senks 输入不了的问题）
# 实现手机键盘自带搜索操作
text = "hello world "
os.system(f"adb shell input text '{text}'")
print("键盘输入的信息", text)
# 评论用户动态，点击发布按钮
time.sleep(5)
el7 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
                                    "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
                                    ".View[2]/android.view.View[4]")
el7.click()
print("评论用户成功", el7)
# 关闭 窗口 返回到首页
# 关闭评论窗口
time.sleep(5)
a = TouchAction(driver).tap(x=987, y=731).perform()
print("关闭评论窗口", a)

# 返回到话题广场首页
time.sleep(5)
# el8 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#                                     ".FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android"
#                                     ".view "
#                                     ".ViewGroup/android.view.ViewGroup/android.widget.ImageView")

el8 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
                                    "/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
el8.click()
print("返回到话题广场首页", el8)
if __name__ == '__main__':
    print(driver.get_window_size())
