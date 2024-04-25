# -*-coding:utf-8-*-
# @FileName  :page_login.py
# @Time      :2024/4/8 16:37
# @Author    :lusong

"""
登录页面文件，包含登录页面的元素和操作方法
"""
from selenium.webdriver.common.by import By
from base.BasePage import BasePage
import config
import time

class LoginPage(BasePage):
    """
    登录页面元素
    """
    username_input = (By.XPATH, '//*[@id="identity"]')  # 用户名输入框
    password_input = (By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div/div/input')  # 密码输入框
    login_btn = (By.XPATH, '//*[@id="app"]/div/div/form/button')  # 登录按钮
    site_yufabu = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]')  # 预发布站点
    site_weiyu = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]')  # 维语站点
    cancel_btn = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
    url = config.YUFABU_URL

    def login(self, username, password, site):
        """
        登录操作
        :param username: 用户名
        :param password: 密码
        :param site: 站点选择 "yufabu"-预发布 "weiyu"-维语站点
        :return:
        """
        self.get(config.YUFABU_URL)
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        time.sleep(2)
        self.click(self.login_btn)
        # 判断传入参数，进入预发布环境或维语环境
        if site == "yufabu":
            self.click(self.site_yufabu)
        elif site == "weiyu":
            self.click(self.site_weiyu)
        # 判断立即去审核是否存在，存在则取消
        if self.is_element_exist(self.cancel_btn):
            self.click(self.cancel_btn)
