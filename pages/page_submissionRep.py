# -*-coding:utf-8-*-
# @FileName  :page_submissionRep.py
# @Time      :2024/4/12 上午11:44
# @Author    :luoqingrong

"""
稿件库页面
"""
import time
from typing import Tuple
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class SubmissionRepPage(BasePage):
    SubmissionRep = (By.XPATH, '//span[text()="稿件库"]')   # 进入稿件库模块
    create_column_btn = (By.XPATH, '//span[text()="新建栏目"]')  # 点击新建栏目按钮
    column_name_input = (By.XPATH, '//input[@placeholder="填写栏目名称"]')  # 输入栏目名称
    column_commit_btn = (By.XPATH, '//div[@aria-label="添加栏目"]//span[text()="确定"]')  # 提交栏目信息
    # text = //span[contains(@class, 'el-tooltip item') and contains(text(), '栏目1')]
    column_select = (By.XPATH, '//span[contains(text(), "自动化栏目")]')  # 选中新建栏目
    column_more_btn = (By.XPATH, '//span[@class="custom-tree-node focus"]/span[2]/span/span/button/i')
    column_move = (By.XPATH, '//div[@class="group-ul el-scrollbar"]/div[3]')
    column_delete_btn = (
    By.XPATH, '/html/body/div[@class="el-popover el-popper group-option-popver"]/div/button[last()]/span')
    column_delete_commit_btn = (By.XPATH, '/html/body/div[last()-1]/div/div[last()]/button[2]/span')
    column_update_btn = (
    By.XPATH, '/html/body/div[@class="el-popover el-popper group-option-popver"]/div/button[last()-4]/span')
    column_update_commit_btn = (By.XPATH, '//div[@aria-label="编辑栏目"]//span[text()="确定"]')  # 提交栏目信息
    article_title = (By.XPATH, '//div[text()="自动化测试文章标题"]')  # 指定文章稿件标题
    article_more_select = (
    By.XPATH, '//div[@class="medialist-doc-item-view"]/div[last()]/div[last()]/div[last()]/div/span')  # 点击稿件后的更多按钮
    column_release = (By.XPATH, '//div[@refname="optionFooter"]/button[1]/i')  # 点击上版按钮，在稿件详情中
    delete_article_btn = (By.XPATH, '//div[@refname="optionFooter"]/button[last()]/i')  # 点击删稿按钮，在稿件详情中
    lineoff_article_btn = (By.XPATH, '//div[@class="option-view"]//span[contains(text(),"下线")]')  # 下线按钮
    lineoff_commit_btn = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')  # 下线确定
    exit_detial_btn = (By.XPATH, '//div[@class="tabs-title"]//i[@class="iconfont icon-quxiao-"]')  # 退出详情
    # 与上版相关
    # layout_select_btn = (By.XPATH, '//span[text()="版面选择"]')  # 版面选择按钮
    # layout_auto_module = (By.XPATH, '//span[text()="自动化版面模块"]')  # 自动化版面模块
    layout_auto_channel = (
    By.XPATH, '//div[@class="el-dialog__body"]/div/div/div[4]/div[1]/div[1]/div[1]/div[2]')  # 模块下第一个频道的加号按钮
    zujian_select_btn = (By.XPATH, '//span[text()="组件选择"]')  # 组件选择按钮
    zujian_auto_module = (By.XPATH, '//span[text()="自动化组件模块"]')  # 自动化组件模块
    zujian_auto_unit = (
    By.XPATH, '//div[@class="el-dialog__body"]/div/div/div[4]/div[1]/div[1]/div[1]/div[2]')  # 模块下第一个组件的加号按钮
    release_commit_btn = (By.XPATH, '//div[@aria-label="上版"]//span[text()="确定"]')  # 上版确定按钮
    delete_commit_btn = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')  # 删除稿件确定按钮
    success_tips = (By.XPATH, '/html/body/div[3]/div/h2')  # 上版成功提示
    delete_completely = (By.XPATH, '//span[contains(text(),"彻底删除")]')  # 彻底删除
    approval_input = (By.XPATH, '//form/div[3]/div/div/div/input')  # 审核流输入框
    approval_select = (By.XPATH, '/html/body/div[last()]/div/div/ul/li[2]')  # 选择新建的第一个审核流
    no_approval_select = (By.XPATH, '/html/body/div[last()]/div/div/ul/li[1]')  # 选择无需审核

    def create_column(self, column_name, need_approval):
        """
        创建栏目，多种选择，可以选择是否需要审核
        :param column_name: 栏目名称
        :param need_approval: True 需要审核，False 不需要审核
        :return:
        """
        self.click(self.SubmissionRep)
        time.sleep(1)
        self.click(self.create_column_btn)
        time.sleep(1)
        self.send_keys(self.column_name_input, column_name)
        time.sleep(1)
        if need_approval:
            self.click(self.approval_input)
            self.click(self.approval_select)
            time.sleep(1)
        self.click(self.column_commit_btn)
        time.sleep(3)

    def update_column(self):
        """
        更改栏目名称
        :return:
        """
        self.click(self.column_select)
        time.sleep(3)
        self.click(self.column_more_btn)
        time.sleep(2)
        self.click(self.column_update_btn)
        self.send_keys(self.column_name_input, '修改')
        time.sleep(1)
        self.click(self.column_update_commit_btn)
        time.sleep(3)

    def update_column_approval(self):
        """
        更改栏目审核流
        :return:
        """
        self.click(self.column_select)
        time.sleep(3)
        self.click(self.column_more_btn)
        time.sleep(2)
        self.click(self.column_update_btn)
        self.click(self.approval_input)
        self.click(self.no_approval_select)
        time.sleep(1)
        self.click(self.column_update_commit_btn)
        time.sleep(3)

    # 删除最新创建的目录
    def delete_column(self):
        """
        删除最新创建的栏目
        :return:
        """
        self.click(self.column_select)
        time.sleep(3)
        self.click(self.column_more_btn)
        time.sleep(2)
        self.click(self.column_delete_btn)
        self.click(self.column_delete_commit_btn)
        time.sleep(1)

    def release_article(self, location):
        """
        上版稿件，版面或组件
        :param location: 0-版面 1-组件
        :return:
        """
        # self.click(self.article_more_select)
        time.sleep(1)
        self.click(self.column_select)  # 点击新建的目录
        self.click(self.article_title)  # 点击标题进入详情页
        time.sleep(2)
        self.click(self.column_release)  # 点击上版
        time.sleep(1)
        if location == 0:
            # self.click(self.layout_select_btn)
            # self.click(self.layout_auto_module)
            self.click(self.layout_auto_channel)  # 上版至指定频道
        elif location == 1:
            self.click(self.zujian_select_btn)
            self.click(self.zujian_auto_module)
            self.click(self.zujian_auto_unit)  # 上版至指定组件
        self.click(self.release_commit_btn)  # 点击确定上版
        time.sleep(1)

    def lineoff_article(self):
        """
        下版稿件
        :return:
        """
        self.click(self.column_select)  # 点击新建的栏目
        time.sleep(1)
        self.click(self.article_more_select)  # 点击更多选项
        time.sleep(1)
        self.click(self.lineoff_article_btn)  # 点击下线按钮
        time.sleep(1)
        self.click(self.lineoff_commit_btn)  # 确定下线
        time.sleep(2)

    def delete_article(self):
        """
        删除最新创建的稿件
        :return:
        """
        self.click(self.column_select)
        self.click(self.article_title)  # 点击标题进入详情页
        time.sleep(1)
        self.click(self.delete_article_btn)  # 点击删稿
        time.sleep(1)
        self.click(self.delete_commit_btn)  # 确定删除
        time.sleep(5)
        self.click(self.article_more_select)  # 点击更多选项
        self.click(self.delete_completely)  # 彻底删除
        self.click(self.delete_commit_btn)  # 确定彻底删除
        time.sleep(1)
