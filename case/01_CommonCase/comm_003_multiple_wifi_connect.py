#-*- encoding: utf-8 -*-
from common import ping
from common import WiFi

wifi = WiFi()
wifi.connect()
ping('www.baidu.com')


