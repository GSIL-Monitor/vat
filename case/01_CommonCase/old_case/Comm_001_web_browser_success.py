# -*- coding: utf-8 -*-

"""
Description:
浏览网页

Procedure:
1.打开网址 www.tianya.cn
2.打开网址 www.baidu.com
3.打开网址 www.163.com

"""
from src.browser import Browser

class TCWebBrowserSuccess(object):

    looptime = 100

    def set_up(self):
        self.wb = Browser()
        pass

    def _test(self):
        self.wb.navigate_url("www.tianya.cn")
        self.wb.waiting()

        self.wb.navigate_url("www.baidu.com")
        self.wb.waiting()

        self.wb.navigate_url("www.163.com")
        self.wb.waiting()

        pass

    def test_down(self):
        self.wb.quite()
        pass
