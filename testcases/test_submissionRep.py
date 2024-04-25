# -*-coding:utf-8-*-
# @FileName  :test_submissionRep.py
# @Time      :2024/4/12 下午3:43
# @Author    :luoqingrong
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.page_submissionRep import SubmissionRepPage
import time

from pages.page_textNews import TextNewsPage
from pages.page_submissionRep import SubmissionRepPage
from pages.page_layout import LayoutPage
from pages.page_leftMenu import LeftMenuPage


@pytest.mark.usefixtures('begin_to_end')
class TestSubmissionRep:
    @allure.title("在稿件库创建栏目并删除")
    def test_createColumn(self, begin_to_end):
        """
        新建栏目
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        sbr = SubmissionRepPage(self.driver)
        sbr.create_column('自动化栏目', False)
        time.sleep(2)
        sbr.delete_column()
        time.sleep(2)

    @allure.title("修改栏目并删除")
    def test_updateColumn(self, begin_to_end):
        """
        修改栏目
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        sbr = SubmissionRepPage(self.driver)
        sbr.create_column('自动化栏目', False)
        time.sleep(1)
        sbr.update_column()
        time.sleep(2)
        sbr.delete_column()
        time.sleep(2)

    @allure.title("上版文章至版面")
    def test_column_artice_release(self, begin_to_end):
        """
        上版文章，稿件库新建栏目 ==》 新建文章稿件，选择发布到刚刚的栏目 ==》 版面管理新建一个模块和频道 ==》 回到稿件库，上版至版面管理的频道 ==》
        稿件库下架文章稿件 ==》 删除版面管理的新建模块和频道 ==》 删除文章稿件 ==》 彻底删除 ==》 删除栏目
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        """新建栏目"""
        srp = SubmissionRepPage(self.driver)
        srp.create_column('自动化栏目', False)
        time.sleep(1)
        self.driver = begin_to_end
        # TODO 发布文章封装成可被其他测试用例调用的函数
        """新建文章稿件"""
        add_icon = self.driver.find_element(By.XPATH, '//i[@class="iconfont-icon-tianjia1"]')  # 加号添加
        add_icon.click()  # 点击加号
        time.sleep(1)
        add_textNews = self.driver.find_element(By.XPATH, '//span[text()="文章稿件"]')  # 文章稿件
        add_textNews.click()
        time.sleep(2)
        # 切换标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        # 如果弹出智媒助理，则点击关闭
        # TODO 智媒助理弹窗存在问题
        # 即使没有弹出，也会定位到
        # if tnp.is_element_exist(tnp.zmzl_close_btn):
        #     tnp.click(tnp.zmzl_close_btn)
        zmgj = self.driver.find_element(By.XPATH, '//div[@class="sider-close"]')  # 智能助理X号
        zmgj.click()
        # 填充文稿
        tnp = TextNewsPage(self.driver)
        # 填充必要稿签
        tnp.select_send_to(0)  # 选择发布栏目
        time.sleep(4)
        tnp.fill_required_tag("自动化测试文章标题", "自动化测试来源")
        # 填充文章内容
        tnp.fill_article_content("自动化测试文章内容")
        tnp.finish_publish(2)  # 发布
        time.sleep(2)
        el = self.driver.find_element(By.XPATH, '//p[text()="内容提交成功"]').text == "内容提交成功"
        tnp.close_and_return()
        """到版面管理新建一个模块和频道"""
        lop = LayoutPage(self.driver)
        lop.create_module()
        lop.create_channel()
        """回到稿件库并上版稿件至版面管理的频道"""
        lm = LeftMenuPage(self.driver)
        lm.click(lm.submission_rep)  # 回到稿件库
        time.sleep(2)
        srp.release_article(0)  # 上版至栏目
        time.sleep(1)
        # exp_el = srp.locate_element(srp.success_tips)
        # assert exp_el.text == "成功"
        lm.click(lm.submission_rep)  # 点击稿件库退出详情
        """下架文章稿件"""
        srp.lineoff_article()
        """删除版面管理中的新建模块和频道"""
        # 删除频道
        lm.click(lm.banmian_manage)  # 回到版面管理
        lop.delete_channel()
        # 删除模块
        lop.delete_module()
        """删除文章稿件（彻底删除）"""
        lm.click(lm.submission_rep)  # 回到稿件库
        srp.delete_article()  # 删除最新稿件，包含彻底删除
        """删除栏目"""
        srp.delete_column()  # 删除栏目
        lm.click(lm.workbench)  # 回到工作台
