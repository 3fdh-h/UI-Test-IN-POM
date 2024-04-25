# -*-coding:utf-8-*-
# @FileName  :test_resourceLibrary.py
# @Time      :2024/4/10 下午5:40
# @Author    :luoqingrong
"""
本文件测试素材库功能，包括：创建目录、删除目录、上传图片、上传音频、上传视频
"""
import allure
import pytest
import pyautogui
import pygetwindow as pw
from selenium.webdriver.common.by import By

import config
from pages.page_resourceLibrary import LibraryPage
from pages.page_leftMenu import LeftMenuPage
import time


@pytest.mark.usefixtures('begin_to_end')
class TestLibrary:
    @allure.title("素材库创建目录")
    def test_createDirectory(self, begin_to_end):
        self.driver = begin_to_end
        lrp = LibraryPage(self.driver)
        lrp.create_directory()
        time.sleep(2)
        lrp.delete_newDirectory()
        time.sleep(1)

    @allure.title("素材库上传图片")
    def test_uploadImage(self, begin_to_end):
        """
        使用pyautogui控制windows窗口直接使用文件路径上传图片
        :param begin_to_end:
        :return: 素材库上传文件，选择本地文件上传
        """
        self.driver = begin_to_end
        lrp = LibraryPage(self.driver)
        lf = LeftMenuPage(self.driver)
        lf.click_suck_manage()
        # 向file类型input传入内容
        lrp.upload_resources(config.img_route)
        time.sleep(5)
        expect_el = self.driver.find_element(By.XPATH, '//div[@class="upload_header"]/div[1]')
        assert expect_el.text == "处理完成（1/1）"
        lrp.click(lrp.success_close_btn)  # 关闭上传成功提示
        time.sleep(2)
        lrp.delete_resources()  # 删除刚刚上传的资源
        time.sleep(2)
        lf.click_workbench()  # 回到工作台

    @allure.title("素材库上传音频")
    def test_uploadAudio(self, begin_to_end):
        """
        上传本地音频
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        lrp = LibraryPage(self.driver)
        lf = LeftMenuPage(self.driver)
        lf.click_suck_manage()  # 点击进入素材管理
        # 向file类型input传入内容
        lrp.upload_resources(config.audio_route)
        time.sleep(5)
        expect_el = self.driver.find_element(By.XPATH, '//div[@class="upload_header"]/div[1]')
        assert expect_el.text == "处理完成（1/1）"
        lrp.click(lrp.success_close_btn)  # 关闭上传成功提示
        time.sleep(2)
        lrp.delete_resources()  # 删除刚刚上传的资源
        time.sleep(2)
        lf.click_workbench()  # 回到工作台
        time.sleep(1)

    @allure.title("素材库上传视频")
    def test_uploadVideo(self, begin_to_end):
        """
        上传本地音频
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        lrp = LibraryPage(self.driver)
        lf = LeftMenuPage(self.driver)
        lf.click_suck_manage()  # 点击进入素材管理
        # 向file类型input传入内容
        lrp.upload_resources(config.video_route)
        time.sleep(10)
        expect_el = self.driver.find_element(By.XPATH, '//div[@class="upload_header"]/div[1]')
        assert expect_el.text == "处理完成（1/1）"
        lrp.click(lrp.success_close_btn)  # 关闭上传成功提示
        time.sleep(2)
        lrp.delete_resources()  # 删除刚刚上传的资源
        time.sleep(2)
        lf.click_workbench()  # 回到工作台
