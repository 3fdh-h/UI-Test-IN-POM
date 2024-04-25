# -*-coding:utf-8-*-
# @FileName  :conftest.py
# @Time      :2024/4/10 8:58
# @Author    :lusong

"""
conftest.py文件是pytest的配置文件，里面可以定义操作，在fixture中使用，也可以定义pytest的钩子函数
"""
import pytest
from selenium import webdriver

import config
from pages.page_login import LoginPage


# 所有测试用例使用一个窗口实例
@pytest.fixture(scope='session', name='begin_to_end')
def begin_to_end():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    lp = LoginPage(driver)
    lp.login(config.username, config.password, "weiyu")
    yield driver
    driver.quit()
