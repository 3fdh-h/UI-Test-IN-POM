# -*-coding:utf-8-*-
# @FileName  :test_publishArticle.py
# @Time      :2024/4/10 18:14
# @Author    :lusong
"""
本文件用于从顶栏左上角加号进入文章文章稿件发布
"""
import os
import time

import allure
import pyautogui
from selenium.webdriver.common.by import By

import config
from pages.page_leftMenu import LeftMenuPage
from pages.page_submissionRep import SubmissionRepPage
from pages.page_textNews import TextNewsPage
from pages.page_resourceLibrary import LibraryPage
import pytest


@pytest.mark.usefixtures("begin_to_end")
class TestPubTextNews:

    @allure.title("左上角加号进入发布文章稿件时预览")
    def test_preview_text_news(self, begin_to_end):
        """
        测试从首页左上角加号进入发布文章稿件时预览
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        # 通过加号进入文稿编辑页面
        add_icon = self.driver.find_element(By.XPATH, '//i[@class="iconfont-icon-tianjia1"]')  # 加号添加
        add_icon.click()  # 点击加号
        time.sleep(2)
        add_textNews = self.driver.find_element(By.XPATH, '//span[text()="文章稿件"]')  # 文章稿件
        add_textNews.click()
        time.sleep(2)
        # 切换标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 填充文稿
        tnp = TextNewsPage(self.driver)
        # 如果弹出智媒助理，则点击关闭
        # TODO 智媒助理弹窗存在问题
        # 即使没有弹出，也会定位到
        if tnp.is_element_exist(tnp.zmzl_close_btn):
            tnp.click(tnp.zmzl_close_btn)
        # 填充必要稿签
        # tnp.select_send_to(0)  # 不选择发布栏目
        time.sleep(4)
        tnp.fill_required_tag("自动化测试预览文章标题", "自动化测试预览来源")
        # 填充文章内容
        tnp.fill_article_content("自动化测试预览文章内容")
        time.sleep(1)
        tnp.finish_publish(1)  # 预览
        time.sleep(5)
        expect_element = self.driver.find_element(By.XPATH, '//div[text()="扫描二维码访问"]')
        assert expect_element.text == "扫描二维码访问"
        time.sleep(2)
        tnp.click(tnp.preview_back_btn)  # 预览后返回
        tnp.close_and_return()  # 关闭当前页面并返回

    @allure.title("左上角加号进入发布文章稿件功能")
    def test_publish_text_news(self, begin_to_end):
        """
        测试从首页左上角加号进入文章稿件发布功能
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        # TODO 发布文章封装成可被其他测试用例调用的函数
        # 先创建栏目
        srp = SubmissionRepPage(self.driver)
        srp.create_column('自动化栏目', False)
        time.sleep(1)
        # 通过加号进入文稿编辑页面
        add_icon = self.driver.find_element(By.XPATH, '//i[@class="iconfont-icon-tianjia1"]')  # 加号添加
        add_icon.click()  # 点击加号
        time.sleep(1)
        add_textNews = self.driver.find_element(By.XPATH, '//span[text()="文章稿件"]')  # 文章稿件
        add_textNews.click()
        time.sleep(2)
        # 切换标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 填充文稿
        tnp = TextNewsPage(self.driver)
        # 填充必要稿签
        tnp.select_send_to(0)  # 选择发布栏目
        time.sleep(4)
        if tnp.is_element_exist(tnp.zmzl_close_btn):
            tnp.click(tnp.zmzl_close_btn)
        tnp.fill_required_tag("自动化测试文章标题", "自动化测试来源")
        # 填充文章内容
        tnp.fill_article_content("自动化测试文章内容")
        tnp.finish_publish(2)  # 发布
        time.sleep(2)
        el = self.driver.find_element(By.XPATH, '//p[text()="内容提交成功"]').text == "内容提交成功"
        tnp.close_and_return()
        # 删除文章和栏目
        lm = LeftMenuPage(self.driver)
        lm.click(lm.submission_rep)  # 回到稿件库
        srp.delete_article()  # 删除最新稿件，包含彻底删除
        """删除栏目"""
        srp.delete_column()  # 删除栏目
        lm.click(lm.workbench)  # 回到工作台

    @allure.title("从工作台的发稿入口发稿")
    def test_publishTextNewsFromWorkbench(self, begin_to_end):
        """
        测试从工作台的发稿入口进入文稿编辑页面
        :return:
        """
        self.driver = begin_to_end
        # 先创建栏目
        srp = SubmissionRepPage(self.driver)
        srp.create_column('自动化栏目', False)
        time.sleep(1)
        # 先点击工作台确保回到工作台页面
        workbench = self.driver.find_element(By.XPATH, '//span[text()="工作台"]')
        workbench.click()
        time.sleep(2)
        fabu = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/section/section/main/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/i')
        fabu.click()
        time.sleep(2)
        # 切换标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 填充文稿
        tnp = TextNewsPage(self.driver)
        # 填充必要稿签
        tnp.select_send_to(0)  # 不选择发布栏目
        time.sleep(4)
        if tnp.is_element_exist(tnp.zmzl_close_btn):
            tnp.click(tnp.zmzl_close_btn)
        tnp.fill_required_tag("自动化测试文章标题", "自动化测试来源")
        # 填充文章内容
        tnp.fill_article_content("自动化测试文章内容")
        tnp.finish_publish(2)  # 发布
        time.sleep(2)
        el = self.driver.find_element(By.XPATH, '//p[text()="内容提交成功"]').text == "内容提交成功"
        tnp.close_and_return()
        srp = SubmissionRepPage(self.driver)
        lm = LeftMenuPage(self.driver)
        lm.click(lm.submission_rep)  # 回到稿件库
        srp.delete_article()
        srp.delete_column()  # 删除栏目
        lm.click(lm.workbench)  # 回到工作台

    @pytest.mark.usefixtures("begin_to_end")
    @allure.title("从选择封面图进入上传图片回显至列表中")
    def test_uploadIsDisplay(self, begin_to_end):
        """
        测试从选择封面图进入上传图片是否回显至列表中
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        # 通过加号进入文稿编辑页面
        add_icon = self.driver.find_element(By.XPATH, '//i[@class="iconfont-icon-tianjia1"]')  # 加号添加
        add_icon.click()  # 点击加号
        time.sleep(1)
        add_textNews = self.driver.find_element(By.XPATH, '//span[text()="文章稿件"]')  # 文章稿件
        add_textNews.click()
        time.sleep(2)
        # 切换标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        tnp = TextNewsPage(self.driver)
        if tnp.is_element_exist(tnp.zmzl_close_btn):
            tnp.click(tnp.zmzl_close_btn)
        tnp.click(tnp.single_img_btn)  # 点击单图
        tnp.click(tnp.add_icon1)  # 点击添加图片
        time.sleep(2)
        tnp.click(tnp.all_resource_tab)  # 全部素材
        time.sleep(2)
        absolute_route = os.path.abspath(config.img_route)
        tnp.send_keys(tnp.dialog_upload_file_input, absolute_route)
        time.sleep(5)
        exp_pic = tnp.locate_element(tnp.first_pic_title)  # 获取预期元素
        assert exp_pic.text == 'lusong-auto-img-1.png'
        tnp.close_and_return()
