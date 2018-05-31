# -*- coding: utf-8 -*-

"""
此脚本实现长时间自动ftp 下载测试，双击运行即可
"""
import ftplib
from time import strftime

ftp_server = "space.tcl-ta.com"         # ftp 地址
ftp_user = "ftp_sz_am"                  # ftp 用户名
ftp_password = "T201jinh"               # ftp 密码
ftp_timeout = 60                        # ftp连接超时时间
ftp_download_file_path = "/USB730L"     # ftp 服务器下载目录路径
ftp_download_file_name = "FRANCO 3D CAD 032717.zip" # 下载文件名(包括扩展名)
local_path = "d:/"                      # 本地目录路径
# ftp_download_count = 1000

ftp = ftplib.FTP()

def ftp_login():
    try:
        ftp.connect(ftp_server, 21, ftp_timeout)
        ftp.login(ftp_user, ftp_password)
        print ftp.getwelcome()
        ftp.dir()
    except ftplib.error_perm:
        ftp.quit()
        raise Warning("ftp login failed !!!")

def download_file(file_name, l_path, ftp_path):
    try:
        ftp.cwd(ftp_path)
        ftp.dir()
        f_name = 'RETR' + file_name
        i = 0
        # for i in xrange(10):
        while(True):
            print log_time_format() + "*"*20 + "count [%s]" % (i+1) + "*"*20
            print "%s [%s] downloading ......" % (log_time_format(), file_name)
            ftp.retrbinary(f_name, open(l_path+file_name, 'wb').write)
            print "%s [%s] download finish" % (log_time_format(), file_name)
            i += 1
    except ftplib.error_perm:
        ftp.quit()
        raise Warning("[%s] download failed !!!")

def log_time_format():
    return strftime("%Y-%m-%d %H:%M:%S")


def upload_file():
    pass

if __name__ == "__main__":
    ftp_login()
    download_file(ftp_download_file_name, local_path, ftp_download_file_path)
    ftp.quit()

