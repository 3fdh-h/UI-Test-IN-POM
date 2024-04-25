# -*-coding:utf-8-*-
# @FileName  :page_layout.py
# @Time      :2024/4/14 下午5:34
# @Author    :luoqingrong

"""
版面管理页面
"""
import time

from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class LayoutPage(BasePage):
    layout_management = (By.XPATH, '//span[text()="版面管理"]')  #
    # 获取版面管理模块的定位
    create_module_btn = (
        By.XPATH, '//div[@class="group-tree-container"]//button//span[text()="新建模块"]')  # 新建模块元素定位

    moduleName_input = (
        By.XPATH, '//div[@aria-label="新建模块"]//div[last()-1]/form/div[1]/div/div/div/input')  # 获取输入模块元素定位
    create_commit_btn = (By.XPATH, '//div[@aria-label="新建模块"]/div[last()]//span/button[last()]/span')  # 获取确定按钮
    newest_module_btn = (By.XPATH, '//span[text()="自动化模块"]')  # 点击模块
    newest_module_more_btn = (By.XPATH, '//i[@class="iconfont icon-gengduo"]')  # 点击more按钮
    add_channel_btn = (By.XPATH, '//span[text()="添加频道"]')  # 添加频道按钮
    channel_name_input = (By.XPATH, '//input[@placeholder="填写频道名称"]')  # 频道名称输入框
    channel_commit_btn = (By.XPATH, '//span[text()="完成"]')  # 完成按钮
    newest_channel_btn = (By.XPATH, '//span[text()="自动化频道"]')  # 新创建自动化频道
    newest_module_delete_btn = (By.XPATH, '/html/body/div[last()]/div/button[6]')  # 删除新创建的模块按钮
    newest_channel_more_btn = (By.XPATH, '//div[@role="group"]//i[@class="iconfont icon-gengduo"]')  # 最新创建的频道的更多按钮
    newest_channel_delete_btn = (By.XPATH, '/html/body/div[last()]/div/button[6]/span')  # 删除最新创建的频道
    channel_delete_commit_btn = (
        By.XPATH, '//div[@class="el-message-box"]/div[3]/button[2]')  # 确定删除频道/模块按钮，确定删除的按钮定位是一样的

    # TODO 后期可以考虑将弹窗确定封装在base层作为方法调用（如果可以确定每次弹窗都在同意定位或者可以一个表达式确定的定位的话）

    # 进入版面管理并新建模块
    def create_module(self):
        """
        新建模块
        :return:
        """
        self.click(self.layout_management)
        self.click(self.create_module_btn)
        time.sleep(1)
        self.send_keys(self.moduleName_input, '自动化模块')
        self.click(self.create_commit_btn)

    def create_channel(self):
        """
        新建频道
        :return:
        """
        self.click(self.newest_module_btn)  # 点击要新增的模块
        self.click(self.newest_module_more_btn)  # 点击更多
        self.click(self.add_channel_btn)  # 新增频道
        self.send_keys(self.channel_name_input, '自动化频道')
        time.sleep(1)
        self.click(self.channel_commit_btn)
        time.sleep(1)

    def delete_channel(self):
        """
        删除最新创建的频道
        :return: 
        """
        self.click(self.newest_channel_btn)  # 点击频道使更多按钮展示出来
        self.click(self.newest_channel_more_btn)  # 点击更多按钮
        self.click(self.newest_channel_delete_btn)  # 点击删除按钮
        self.click(self.channel_delete_commit_btn)

    def delete_module(self):
        """
        删除最新创建的模块
        :return:
        """
        self.click(self.newest_module_btn)  # 点击最新建的模块
        self.click(self.newest_module_more_btn)  # 点击更多
        self.click(self.newest_module_delete_btn)  # 点击删除
        self.click(self.channel_delete_commit_btn)
