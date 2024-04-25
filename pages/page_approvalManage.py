# -*-coding:utf-8-*-
# @FileName  :page_approvalManage.py
# @Time      :2024/4/18 16:05
# @Author    :lusong
"""
审批管理的页面文件，包含审批创建和管理过程中的各种元素和方法
"""
import time

from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class ApprovalManagePage(BasePage):
    add_approval_btn = (By.XPATH, '//i[@class="iconfont icon-zengjia-"]')  # 新增审批管理按钮
    approval_name_input = (By.XPATH, '//form/div[1]//input')  # 审批名称输入框
    approval_group_input = (By.XPATH, '//form/div[2]/div/span/span/div/div/div[1]/input')  # 审批组输入框
    text_approval_select = (By.XPATH, '//span[text()="文稿审批"]')  # 文稿审批选择
    second_step = (By.XPATH, '//div[text()=2]')  # 切换到第二个步骤的圆点
    approval_pub_btn = (By.XPATH, '//span[text()="发布"]')  # 发布审核流按钮
    success_tips = (By.XPATH, '//div[@role="alert"]//h2[contains(text(), "成功")]')  # 发布成功后的提示信息

    disable_approval_btn = (By.XPATH, '//div[@class="item clearfix"][1]/div[3]/i[2]')  # 禁用审核流按钮
    delete_approval_btn = (By.XPATH, '//div[@class="disable"]/div/div[3]/i[3]')  # 删除审核流按钮
    disable_commit_btn = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')  # 确定禁用/删除按钮，每一次弹窗确定定位似乎一样

    def add_approval(self, name):
        """
        添加审核流程
        :param name: 审核流名称
        :return:
        """
        self.click(self.add_approval_btn)  # 点击新建进入新建页面
        self.send_keys(self.approval_name_input, name)
        self.click(self.approval_group_input)  # 输入审核名称、审核组
        self.click(self.text_approval_select)  # 选择文章审核组
        time.sleep(1)
        self.click(self.second_step)
        self.click(self.approval_pub_btn)  # 点击发布审核流按钮
        time.sleep(1)
        # assert self.locate_element(self.success_tips).text == '成功'  无需判断

    def delete_approval(self):
        """
        删除第一条审核流
        :return:
        """
        # TODO 删除栏目之前需要将审核流改成无需审核
        self.click(self.disable_approval_btn)  # 点击禁用按钮
        time.sleep(1)
        self.click(self.disable_commit_btn)  # 确定禁用
        self.click(self.delete_approval_btn)  # 点击删除按钮
        time.sleep(1)
        self.click(self.disable_commit_btn)  # 确定删除
