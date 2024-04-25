# -*-coding:utf-8-*-
# @FileName  :test_approval.py
# @Time      :2024/4/18 15:51
# @Author    :lusong
"""
使用审核流进行审批
"""
import time

import allure
from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from pages.page_leftMenu import LeftMenuPage
from pages.page_textNews import TextNewsPage
from pages.page_submissionRep import SubmissionRepPage
from pages.page_approvalManage import ApprovalManagePage
from pages.page_login import LoginPage
import pytest


@pytest.mark.usefixtures('begin_to_end')
class TestApprovalApply:
    @allure.title("测试应用在栏目中的审核流是否奏效")
    def test_applyApproval(self, begin_to_end):
        """
        测试应用在栏目中的审核流是否奏效
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        """
        创建审批流程（选择负责人审批） =》 新建栏目（使用刚创建的审批流） =》 
        新建文章稿件发布至刚创建的栏目 =》 判断：在待审稿库带我审核中是否有刚刚
        发布的稿件，并审核同意；在稿件库栏目中是否可以看见刚刚审核通过的稿件
        """
        """创建审批流"""
        lm = LeftMenuPage(self.driver)
        time.sleep(1)
        lm.click(lm.system_settings_menu)  # 进入系统设置
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 句柄切换到最新窗口
        approval_btn = self.driver.find_element(By.XPATH, '//div[text()="审批管理"]')
        approval_btn.click()  # 进入审批管理
        amp = ApprovalManagePage(self.driver)
        amp.add_approval('自动化测试审批流')  # 添加审批流
        amp.close_and_return()  # 关闭返回首页
        """新建审核栏目"""
        lm.click(lm.submission_rep)  # 进入稿件库新建审核栏目
        srp = SubmissionRepPage(self.driver)
        srp.create_column('自动化栏目', True)
        time.sleep(2)
        """新建文章并选择刚刚创建的栏目"""
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
        # 填充必要稿签
        tnp.select_send_to(0)  # 选择发布栏目
        time.sleep(4)
        tnp.fill_required_tag("自动化测试文章标题", "自动化测试来源")
        # 填充文章内容
        tnp.fill_article_content("自动化测试文章内容")
        if tnp.is_element_exist(tnp.zmzl_close_btn):
            tnp.click(tnp.zmzl_close_btn)
        tnp.finish_publish(2)  # 发布
        time.sleep(2)
        tnp.close_and_return()  # 回到首页
        lp = LoginPage(self.driver)
        lp.click(lp.cancel_btn)  # 取消去审核
        lm.click(lm.approval_waited_rep)  # 进入待审稿库
        title = self.driver.find_element(By.XPATH,
                                         '//div[@class="approval-table-container"]//span[text()="自动化测试文章标题"]')
        title.click()  # 点击标题
        approval_agree_btn = self.driver.find_element(By.XPATH,
                                                      '//div[@class="option-view top-border-line"]/div/button[1]')
        approval_agree_btn.click()  # 审核同意
        approval_opinion_input = self.driver.find_element(By.XPATH, '//textarea[@placeholder="请填写审核意见"]')
        approval_opinion_input.send_keys("同意")  # 输入审核意见
        agree_commit = self.driver.find_element(By.XPATH, '//span[text()="确定同意"]')
        agree_commit.click()  # 确定同意
        # TODO 判断操作成功的断言也可以封装在底层
        success_tips = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/h2')
        # assert success_tips.text == "成功"
        lm.click(lm.submission_rep)
        assert srp.is_element_exist(srp.article_title)  # 存在刚刚发布的文章标题
        srp.delete_article()
        srp.update_column_approval()  # 先修改栏目审核流为无需审核
        srp.delete_column()
        lm.click(lm.system_settings_menu)  # 进入系统设置
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 句柄切换到最新窗口
        approval_btn = self.driver.find_element(By.XPATH, '//div[text()="审批管理"]')
        approval_btn.click()  # 进入审批管理
        amp.delete_approval()  # 删除审核流
        amp.close_and_return()
