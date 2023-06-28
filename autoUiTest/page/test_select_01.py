

import pytest,time,os

from autoUiTest.common.keywords import WebKeywords

def test_query_01():


    func =WebKeywords("https://www.baidu.com")
    # 打开百度
    func.open_gc()
    func.wait(3)
    # 输入搜索内容
    func.input_ele_text("xpath","//*[@id=\"kw\"]","李白")
    func.wait(3)
    # 点击百度
    func.touch_click("xpath","//*[@id=\"su\"]")
    func.quits()
    print("hello1 word")





if __name__ == '__main__':
    pass