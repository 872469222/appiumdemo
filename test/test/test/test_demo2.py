import os
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup(self):
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
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # self.driver.implicitly_wait(10)
    def test_dem0(self):
        time.sleep(3)
        # el1 = self.driver.find_element_by_id("com.changsha.apps.android.mycs:id/iv_close")
        # el1.click()
        time.sleep(5)
        el1 = self.driver.find_element_by_id("com.changsha.apps.android.mycs:id/tv_interaction")
        el1.click()
        time.sleep(5)
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
            ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
            "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
            ".View/android.view.View[8]/android.view.View/android.widget.TextView")
        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
            ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
            "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
            ".View/android.view.View[1]/android.view.View[1]/android.widget.EditText")
        el3.send_keys("我的长沙我在长沙")
        time.sleep(4)
        # 这段代码ok
        # 拉起本地相册
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
            ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
            "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
            ".View/android.view.View[1]/android.view.View[2]/android.view.View["
            "2]/android.widget.Button")
        el4.click()
        time.sleep(4)
        # 进入相册
        adb1 = "adb shell input tap 842 1896"
        os.system(adb1)
        time.sleep(1)
        adb2 = "adb shell input tap 926 1953"
        os.system(adb2)
        # 选择相册里的图片上传 使用adb 的input 定位（这里需要优化）
        adb1 = "adb shell input tap 72 323"
        os.system(adb1)
        time.sleep(1)
        adb2 = "adb shell input tap 368 727"
        os.system(adb2)
        # 移动到选择话题
        time.sleep(4)
        el4 = self.driver.find_element_by_xpath("//android  .widget.TextView[@text='请选择话题']")
        el4.click()
        # 进入话题页面，选择五一去哪里玩
        time.sleep(4)
        # 这个Text 参数需要随时对应活动页面的更改
        el5 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='夏日打卡计划']")
        el5.click()
        # 填写动态内容，添加图片，选择话题，点击提交按钮
        time.sleep(4)
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
            ".widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager"
            "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view"
            ".View/android.view.View[2]/android.widget.Button[2]")
        el1.click()

    def tearDown(self):
        self.driver.quit()
