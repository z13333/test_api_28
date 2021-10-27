"""
主要实现的是基础的接口请求,最基本get,past,header,url
"""

import requests
from loguru import logger

from setting import BASE_URL
# from setting import LOGIN_INFO

from cacheout import Cache  # 缓存所用

cache = Cache()


# 定义类

class Base(object):

    # 实现url的方法
    def get_url(self, path, params=None):
        """

        :param path: 接口路径
        :param params: 查询字符串
        :return: 返回url
        """
        if params:
            return BASE_URL + path + '?' + params
        return BASE_URL + path

    # 实现get方法
    def get(self, url):
        """

        :param url: url地址
        :return: 返回请求后的响应体
        """
        try:
            response = requests.get(url, headers=self.get_headers())
            result = response.json()
            logger.info("请求get数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求get方法失败，返回数据：{}".format(e))

    # 实现post方法
    def post(self, url, data):
        """

        :param url: url地址
        :return: 返回请求后的响应体
        """
        try:
            response = requests.post(url, json=data, headers=self.get_headers())
            result = response.json()
            logger.info("请求post数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求post方法失败，返回数据：{}".format(e))

    # 登录
    def login(self, username, password):
        '''

        :param username: 用户名
        :param password: 密码
        :return:
        '''
        login_path = "/admin/auth/login"
        login_url = self.get_url(login_path)
        login_data = {"username": username, "password": password}
        result = self.post(login_url, login_data)
        logger.info('获取登录用户数据:{}'.format(login_data))
        try:
            if 0 == result.get('errno'):
                logger.info('请求登录接口成功')
                token = result.get('data').get('token')
                cache.set('token', token)  # 把'token'值保存到缓存中
                logger.info('11111:{}',token)
                logger.info('22222:{}'.format(cache.get('token')))
            else:
                logger.error('请求登录接口失败：{}'.format(result))

        except Exception as e:
            logger.error('请求登录接口异常，异常数据：{}'.format(e))

    # 请求头
    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        token = cache.get('token')
        if token:
            headers.update({"X-Litemall-Admin-Token": token})
            # else:
            #     self.login(LOGIN_INFO.get('username'),LOGIN_INFO.get('password'))
            logger.warning('请求头信息返回数据：{},提示：多个接口需要带token\n'.format(headers))
        return headers


#  调用 __main__ 方法，从这里开始运行。
if __name__ == '__main__':
    b = Base()
    print(b.get_url("/admin/auth/login"))
    print(b.get_url("/admin/auth/login", "page=1&limit=20&sort=add_time&order=besc"))
    print(b.get("http://www.weather.com.cn/data/sk/101010100.html"))
