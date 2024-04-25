# -*-coding:utf-8-*-
# @FileName  :page_resourceLibrary.py
# @Time      :2024/4/10 下午5:15
# @Author    :luoqingrong

# -*-coding:utf-8-*-
# @FileName  :page_home.py
# @Time      :2024/4/9 18:54
# @Author    :lusong

"""
素材库页面
"""
import time
import os
import pyautogui
from selenium.webdriver.common.by import By

import config
from base.BasePage import BasePage


class LibraryPage(BasePage):
    library = (
        By.XPATH,
        '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[5]/div/span[2]/span[1]')  #
    # 获取素材库模块的定位
    create_directory_btn = (
        By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div[1]/div[2]/div[1]/div/div/div[2]/button')  # 新建目录元素定位

    directoryName_input = (By.XPATH, '//input[@placeholder="请输入名称0-50个字符"]')  # 获取输入目录元素定位
    create_commit_btn = (By.XPATH, '//div[@aria-label="新建目录"]/div[last()]/span/button[2]/span')  # 获取确定按钮
    directory_more_btn = (By.XPATH,
                          '//*[@id="app"]/div[1]/section/section/main/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div[1]/div[@class="drag-item drop-item grid-item file-move-item"][last()]//div/div/div/div[2]/span/span/button/i')  # 获取新建目录后的更多元素
    directory_delete_btn = (By.XPATH,
                            '/html/body/div[contains(@role, "tooltip") and contains(@class, "table-option-popper")]/div[@class="option-view card-option"]/button[3]/span')  # 点击删除
    delete_commit_btn = (By.XPATH, '//div[(@class= "el-message-box")]/div[3]/button[2]')  # 删除确定
    upload_btn = (By.XPATH, '//span[text()="上传资源"]')  # 上传资源按钮
    upload_commit_btn = (By.XPATH, '//div[@aria-label="上传配置"]/div[3]/span/button[2]')  # 上传资源确定按钮
    expect_element = (By.XPATH, '//div[@class="upload_header"]/div[1]')  # 上传资源成功后的提示元素
    success_close_btn = (By.XPATH, '//div[@class="upload_pannel_bar"]/span[3]')  # 处理完成弹窗关闭按钮
    file_upload_input = (By.XPATH, '//input[@class="file_input_file"]')  # 文件上传输入框
    # dialog_upload_file_input = (By.XPATH, '//div[@class="el-dialog__body"]//input[@class="file_input_file"]')  # 从弹出的选择素材对话框中的上传资源文件输入框

    resources_more_btn = (By.XPATH,
                          '//div[@class="file-list"]/div[2]/div[1]//div[@class="el-card__body"]//span[1]/span[1]/button')  # 第一个素材的更多按钮
    resources_delete_btn = (By.XPATH, 'html/body/div[last()]/div[1]/button[last()]')  # 删除按钮

    # 进入素材库并新建目录
    def create_directory(self):
        self.click(self.library)
        self.click(self.create_directory_btn)
        time.sleep(1)
        self.send_keys(self.directoryName_input, '自动化目录')
        self.click(self.create_commit_btn)

    # 删除最新创建的目录
    def delete_newDirectory(self):
        self.click(self.directory_more_btn)
        time.sleep(1)
        self.click(self.directory_delete_btn)
        time.sleep(1)
        self.click(self.delete_commit_btn)

    def upload_resources(self, file_path):
        """
        素材库中上传资源
        :param file_path: 资源在项目中的相对路径
        :return:
        """
        time.sleep(1)  # 素材库进入后需要等待一下
        # 使用os库函数将传入的相对路径转换为绝对路径
        absolute_route = os.path.abspath(file_path)
        self.send_keys(self.file_upload_input, absolute_route)
        self.click(self.upload_commit_btn)

    def delete_resources(self):
        """
        删除最新上传的资源
        :return:
        """
        time.sleep(1)
        self.click(self.resources_more_btn)  # 点击更多
        time.sleep(1)
        self.click(self.resources_delete_btn)  # 点击删除
        time.sleep(1)
        self.click(self.delete_commit_btn)  # 确定删除
        time.sleep(1)
