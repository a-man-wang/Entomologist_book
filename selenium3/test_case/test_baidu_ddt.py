import unittest
from selenium import webdriver
from ddt import ddt, data, file_data, unpack
from time import sleep

@ddt
class TestBaiduDdt(unittest.TestCase):
    """测试百度搜索"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    @data(("selenium", "selenium"), ("unittest", "unittest"), ("pytest", "pytest"))
    @unpack
    def test_search1(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @data(["selenium", "selenium"], ["unittest", "unittest"], ["pytest", "pytest"])
    @unpack
    def test_search2(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @data({"search_key": "selenium"}, {"search_key": "unittest"}, {"search_key": "pytest"})
    @unpack
    def test_search3(self, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @file_data('test_data.json')
    def test_search4(self, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)