"""
@Time : 2021/10/26 22:58
@Author : Administrator
@Email : ruslan@163.com
@File : test_user_manager_case.py
@Project : test_api_28
@feature : 
@实现步骤： 主要实现的是用户管理的测试用例
"""
from apis.user_manager import UserManagerApi
import unittest    # 测试所用的包

class TestUserManagerCase(unittest.TestCase):

    user_id = 562     # 这是个类变量

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManagerApi()


    #  实现添加测试用例
    # @unittest.skip('暂时跳过')
    def test01_add_user(self):
        # 1. 定义数据
        username = 'testb002'
        password = 'testb002'
        # 2. 调用添加管理员接口
        result = self.user.add_user(username,password)
        # 获取id值,赋值给类名变量
        if result.get('data').get('id'):
            TestUserManagerCase.user_id = result.get('data').get('id')
        # 3. 进行断言
        self.assertEqual(0,result.get("errno"))


    # 实现编辑测试用例
    # @unittest.skip('暂时跳过')
    def test02_edit_user(self):

        # 1.定义数据
        new_username = 'testc113'
        new_password = 'testc113'
        # 2.调用编辑接口
        result = self.user.edit_user(TestUserManagerCase.user_id,new_username,new_password)
        # 3.进行断言
        self.assertEqual(0,result.get("errno"))


    # 实现删除测试用例
    # @unittest.skip('暂时跳过')
    def test04_delete_user(self):
        new_user = 'testc113'
        password = 'testc113'
        # 2.调用删除接口
        result = self.user.delete_user(TestUserManagerCase.user_id,new_user,password)
        # 3.进行断言
        self.assertEqual(0,result.get("errno"))


    # 实现查询测试用例
    # @unittest.skip('暂时跳过')
    def test03_get_user(self):
        result = self.user.get_user()
        self.assertEqual(402, result.get("errno"))
