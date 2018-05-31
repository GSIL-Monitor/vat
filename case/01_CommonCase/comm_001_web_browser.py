#-*- encoding: utf-8 -*-

from common import Firefox
from common import create_logger
from common import get_file_name

web_list = [
    'www.zhihu.com',
    'www.baidu.com',
    'www.qq.com'
]
web_head = "http://"
log = create_logger(get_file_name())
firefox = Firefox()
wb = firefox.browser()
fail_count = 0
for web in web_list:
    address = web if web.startswith(web_head) else web_head + web
    log.info("navigate url: {0}".format(address))
    wb.get(address)
    if wb.title.__contains__("出错"):
        log.warning("navigate url: {0} Failed!".format(address))
        fail_count += 1
        log.warning("fail count: {0}".format(fail_count))

    assert fail_count < 3, "web browser test failed!"

