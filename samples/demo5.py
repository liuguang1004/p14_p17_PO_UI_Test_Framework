# encoding: utf-8
# @author: newdream_daliu
# @file: demo5.py
# @time: 2022-07-24 11:44
# @desc:
import unittest

class demo5Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        cls.num=100
        print('setUpClass %d' % cls.num)
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
    def setUp(self) -> None:
        print('setUp')
        print('setUp %d'%self.num)
    def tearDown(self) -> None:
        print('tearDown')
    def test_case01(self):
        print('test_case01')
        print('test_case01 %d'%self.num)
    def test_case02(self):
        print('test_case02')
if __name__ == '__main__':
    unittest.main()