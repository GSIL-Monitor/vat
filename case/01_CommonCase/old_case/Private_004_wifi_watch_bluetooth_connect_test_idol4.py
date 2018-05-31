from src import log
from time import sleep
from src.mobiledriver import android_driver as m_dev


class TCAlcatelIdol4(object):

    looptime = 100

    def set_up(self):
        pass

    def _test(self):

        self.close_bluetooth()
        self.enter_movetime()
        self.login_movetime()

        log.write_log("Click Menu")
        m_dev(resourceId="com.alcatel.movetime:id/main_menu_list").click()
        sleep(1)

        log.write_log("Click Watch menu")
        m_dev(resourceId="com.alcatel.movetime:id/menu_list_watch_layout").click()  # click watch icon enter ui
        if not m_dev(text="Disconnected").exists:
            raise Warning("Disconnected fail !!!")

        self.open_bluetooth()

        self.enter_movetime()

        log.write_log("Click Menu")
        m_dev(resourceId="com.alcatel.movetime:id/main_menu_list").click()
        sleep(1)

        log.write_log("Click Watch menu")
        m_dev(resourceId="com.alcatel.movetime:id/menu_list_watch_layout").click()  # click watch icon enter ui

        for i in xrange(60):
            log.write_log("Check connecting")
            if (m_dev(text="Watch", resourceId="com.alcatel.movetime:id/watch_title_text").exists and
                    m_dev(text="Watch face").exists):
                break
            sleep(1)
        else:
            raise Warning("time out, Connected fail !!!")

        log.write_log("Connect success, test pass !!!")
        m_dev.press.home()

    def test_down(self):
        pass

    def close_bluetooth(self):
        self.enter_bluetooth_menu()

        log.write_log("close bluetooth")
        if m_dev(text="ON").exists:
            m_dev(text="ON").click()  # close bluetooth
            sleep(3)

    def open_bluetooth(self):
        self.enter_bluetooth_menu()

        log.write_log("open bluetooth")
        m_dev(text="OFF").click()    # open bluetooth
        sleep(3)

    def enter_bluetooth_menu(self):
        log.write_log("press home")
        m_dev.press.home()

        log.write_log("press all apps")
        m_dev(description='ALL APPS').click()

        log.write_log("scroll to Settings")
        m_dev(scrollable=True).scroll.to(text="Settings")

        log.write_log("Click Settings")
        m_dev(text="Settings").click()

        log.write_log("Click bluetooth")
        m_dev(text="Bluetooth").click()
        sleep(1)

    def login_movetime(self):
        sleep(3)
        if m_dev(resourceId="com.alcatel.movetime:id/input_login_account").exists:
            m_dev(resourceId="com.alcatel.movetime:id/input_login_account").set_text("weijianrong")
            m_dev(resourceId="com.alcatel.movetime:id/input_login_password").set_text("1234567890")
            m_dev(resourceId="com.alcatel.movetime:id/login_login_btn").click()
            sleep(3)

    def enter_movetime(self):
        log.write_log("press home")
        m_dev.press.home()

        log.write_log("press all apps")
        m_dev(description='ALL APPS').click()

        log.write_log("scroll to MOVETIME")
        m_dev(scrollable=True).scroll.to(text="MOVETIME")

        log.write_log("Click MOVETIME")
        m_dev(text="MOVETIME").click()