from base.base_driver import init_driver
import time

class TestLogin:
    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login1(self):
        assert 1

    def test_login2(self):
        assert 0