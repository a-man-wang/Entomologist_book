from selenium import webdriver
import unittest
from time import sleep
from parameterized import parameterized


class TestBaidu(unittest.TestCase):
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

    @parameterized.expand(
        [
            ("selenium", "selenium"),
            ("unittest", "unittest"),
            ("pytest", "pytest")
        ]
    )
    def test_search(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # def test_search_key_selenium(self,):
    #     """测试搜索selenium"""
    #     search_key = "selenium"
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + "_百度搜索")
    #
    # def test_search_key_unittest(self):
    #     """测试搜索unittest"""
    #     search_key = "unittest"
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()