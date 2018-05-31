import urllib2

class TCInterfaceTest(object):

    looptime = 1

    def set_up(self):
        pass

    def _test(self):
        url = "http://106.14.6.65/v1.0/token"
        url_head = {"Authorization": "key=vEWZapEpW5OezzEs5Su44xAbCiy9-arCJz7eoLJfjac2h1r4VF0"}
        url_data = '{"uid":"864408020004107", "name":"LTE Watch", "client":"device"}'

        req = urllib2.Request(url, headers=url_head, data=url_data)
        postResult = urllib2.urlopen(req).read()

        d_postRes = eval(postResult)
        print d_postRes["access_token"]
        print d_postRes["uid"]
        assert not(repr(req).__contains__("Error")) or req is not None, "Fail test !!!"
        self.qqqqqq()
        pass


    def qqqqqq(self):
        print "hello"

    def test_down(self):
        pass

if __name__ == '__main__':
    TCInterfaceTest().test()
