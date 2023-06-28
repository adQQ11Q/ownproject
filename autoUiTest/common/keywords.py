


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class WebKeywords:



    def __init__(self,url):
        self.driver =webdriver.Chrome()
        self.url = url


    # 打开浏览器
    def open_gc(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # 退出浏览器
    def quits(self):
        self.driver.quit()

        # 点击元素的方法

    def touch_click(self, ele, value):

        return self.driver.find_element(ele, value).click()

        # 输入内容

    def input_ele_text(self, name, value, text):
        ele = self.driver.find_element(name, value)
        ele.clear()
        ele.send_keys(text)

        # 窗口切换

    def switch_frame(self, n):
        self.driver.switch_to.window(self.driver.window_handles(n))

        # 关闭页签

    def close_frame(self, n):
        self.driver.switch_to.window(self.driver.window_handles(n))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles(0))

        # 等待

    def wait(self, m):
        time.sleep(m)

