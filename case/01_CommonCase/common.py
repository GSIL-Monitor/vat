#-*- encoding: utf-8 -*-
import sys
import time
import logging
import subprocess
from selenium import webdriver
from configparser import ConfigParser

try:
    import pywifi
except ImportError:
    print("please install pywifi lib")
    sys.exit(0)


WIFI_SSID = "HiWiFi-WAC"  # wifi ssid
WIFI_PASSWORD = "wacval2017" # wifi password


def get_file_name():
    return getattr(sys.modules['__main__'], '__file__', None).split('/')[-1]


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s.%(msecs)03d: [%(name)s] [%(levelname)s] %(message)s','%Y%m%d %H:%M:%S')
    # if file:
    #     file_handle = logging.FileHandler(file)
    #     file_handle.setLevel(logging.INFO)
    #     file_handle.setFormatter(formatter)
    #     logger.addHandler(file_handle)
    # #
    # console_handle = logging.StreamHandler()
    # console_handle.setLevel(logging.DEBUG)
    # console_handle.setFormatter(formatter)
    # logger.addHandler(console_handle)

    return logger

log = create_logger(__name__)

# def connect_wifi(ssid=WIFI_SSID, password=WIFI_PASSWORD):
#     wifi = pywifi.PyWiFi()
#     wireless = wifi.interfaces()[0]
#     log.info("wireless adapter: %s" % wireless.name())
#     profile = pywifi.Profile()
#     profile.ssid = ssid
#     profile.auth = pywifi.const.AUTH_ALG_OPEN
#     profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
#     profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
#     profile.key = password
#     wireless.remove_all_network_profiles()
#     tmp_profile = wireless.add_network_profile(profile)
#     log.info("Connect to {}".format(profile.ssid))
#     wireless.connect(tmp_profile)
#     time.sleep(10)
#     assert wireless.status() == pywifi.const.IFACE_CONNECTED, "Connect {0} Failed!".format(profile.ssid)
#     log.info("Connect {0} Success!".format(profile.ssid))


class WiFi(object):
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.wireless = self.wifi.interfaces()[0]
        log.info("wireless adapter: %s" % self.wireless.name())
        self.profile = pywifi.Profile()
        self.add_profile = None

    def set_profile(self, ssid, password):
        self.profile.ssid = ssid
        self.profile.auth = pywifi.const.AUTH_ALG_OPEN
        self.profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        self.profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        self.profile.key = password
        self.wireless.remove_all_network_profiles()
        self.add_profile = self.wireless.add_network_profile(self.profile)

    def connect(self, ssid=WIFI_SSID, password=WIFI_PASSWORD):
        log.info("Connect to {}".format(ssid))
        self.set_profile(ssid, password)
        self.wireless.connect(self.add_profile)
        time.sleep(10)
        assert self.wireless.status() == pywifi.const.IFACE_CONNECTED, "Connect {0} Failed!".format(ssid)
        log.info("Connect {0} Success!".format(self.profile.ssid))

    def disconnect(self):
        self.wireless.remove_all_network_profiles()
        time.sleep(2)
        assert self.wireless.status() == pywifi.const.IFACE_DISCONNECTED, "Disconnect Failed!"
        log.info("Disconnect Success!".format(self.profile.ssid))


def ping(host, count=100):
    command = "ping {0} -n {1}".format(host, count)
    log.info(command)
    error_cause = [
        "请求找不到主机",
        "请求超时",
        "100%丢失",
        "传输失败"
    ]
    error_count = 0
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while pipe.poll() is None:
        line = pipe.stdout.readline()
        if line:
            result = (str(line, encoding='GB2312'))
            for err in error_cause:
                if result.__contains__(err):
                    error_count += 1

            assert error_count < 10, "ping failed!"
    log.info("ping passed")


class Firefox(object):
    def __init__(self):
        self.wb = webdriver.Firefox()
        self.wb.set_page_load_timeout(300)
        self.wb.implicitly_wait(30)

    def __del__(self):
        time.sleep(1)
        self.wb.quit()

    def set_profile(self):
        '''
        will cause firefox crash after call quit() method, so unused currently!
        :return:
        '''
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.startup.homepage", "about:blank")
        profile.set_preference("startup.homepage_welcome_url", "about:blank")
        profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        return profile

    def browser(self):
        return self.wb


class GetConfig(object):
    def __init__(self, file):
        self.config = ConfigParser()
        self.config_path = file
        self.config.read(self.config_path)

    def get_int(self, section, key, default=0):
        try:
            return self.config.getint(section, key)
        except BaseException as e:
            return default

    def get_str(self, section, key, default=None):
        try:
            return self.config.get(section, key)
        except BaseException as e:
            return default

    def set_value(self, section, key, value):
        self.config.set(section, key, value)
        self.config.write(open(self.config_path, 'w'))



if __name__ == '__main__':
    log = create_logger("ffjsdljfld")
    log.hasHandlers()
    log.info("info")
    log.warning("warning")