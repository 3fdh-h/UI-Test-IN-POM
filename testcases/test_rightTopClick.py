# -*-coding:utf-8-*-
# @FileName  :test_rightTopClick.py
# @Time      :2024/4/10 13:50
# @Author    :lusong
"""
本文件用于执行测试首页右上角的功能点，如进入web网站，进入开发者服务中心等
"""
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains动作链可以对鼠标、键盘等进行更多的操作
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import config
from pages.page_homeRightTop import RightTopPage
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('begin_to_end')
class TestPublishClick:
    @allure.title("点击下载app网站")
    def test_clickPhoneSite(self, begin_to_end):
        """
        :param begin_to_end:
        :return: 测试点击手机网站
        """
        self.driver = begin_to_end
        rt = RightTopPage(self.driver)
        # 需要将图标所在的元素传入ActionChains中，所以需要先获取元素，不能直接用路径，类型为webelement
        webelement_phone_pc = rt.locate_element(rt.phone_and_pc)
        # 使用动作链的移动光标函数将光标放在图标上
        ActionChains(self.driver).move_to_element(webelement_phone_pc).perform()
        time.sleep(1)
        # 点击指定元素
        rt.click(rt.download_app)
        time.sleep(2)
        # 切换句柄到当前页面
        self.driver.switch_to_window(self.driver.window_handles[-1])
        assert self.driver.current_url == "http://newsapp.cmstop.com/appdown/"
        # 调用封装方法，可以关闭当前页面并回到首页
        rt.close_and_return()

    @allure.title("点击web网站")
    def test_clickWebSite(self, begin_to_end):
        """
        :param begin_to_end
        :return:
        """
        self.driver = begin_to_end
        rt = RightTopPage(self.driver)
        # 获取访问其他端链接的图标
        webelement_phone_pc = rt.locate_element(rt.phone_and_pc)
        # 使用动作链的移动光标函数将光标放在图标上
        ActionChains(self.driver).move_to_element(webelement_phone_pc).perform()
        time.sleep(1)
        rt.click(rt.visit_pc)
        # 切换句柄到当前页面
        self.driver.switch_to_window(self.driver.window_handles[-1])
        try:
            assert self.driver.current_url == "https://www.r.cmstop.xyz/"
        # 关闭并返回
        finally:
            rt.close_and_return()

    @allure.title("点击手机网站")
    def test_clickPhonrSite(self, begin_to_end):
        """
        :param begin_to_end
        :return:
        """
        self.driver = begin_to_end
        rt = RightTopPage(self.driver)
        # 获取访问其他端链接的图标
        webelement_phone_pc = rt.locate_element(rt.phone_and_pc)
        # 使用动作链的移动光标函数将光标放在图标上
        ActionChains(self.driver).move_to_element(webelement_phone_pc).perform()
        time.sleep(1)
        rt.click(rt.visit_wap)
        # 切换句柄到当前页面
        self.driver.switch_to_window(self.driver.window_handles[-1])
        expe_el = self.driver.find_element(By.XPATH, '//span[text()="扫描二维码访问"]')
        assert expe_el.text == "扫描二维码访问"
        # 关闭并返回
        rt.close_and_return()
