# -*-coding:utf-8-*-
# @FileName  :page_app.py
# @Time      :2024/4/10 下午4:54
# @Author    :leisijun
"""
应用中心页面，包含应用中心的元素定位和操作方法
"""
from selenium.webdriver.common.by import By
from base.BasePage import BasePage

class AppPage(BasePage):
    study_app = (By.XPATH,
                 '//div[@class="item"]//div[text()="课程学习"]')  # 课程学习
    TV_app = (By.XPATH,
              '//div[@class="item"]//div[text()="电视广播"]')  # 电视广播
    reprint_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="稿件转载"]')  # 稿件转载
    points_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="积分商城"]')  # 积分商城
    form_app = (By.XPATH,
                '//div[@class="item"]//div[text()="表单管理"]')  # 表单管理
    lottery_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="抽奖管理"]')  # 抽奖管理
    baoliao_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="报料管理"]')  # 报料管理
    quanzi_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="圈子管理"]')  # 圈子管理
    wenzheng_app = (By.XPATH,
                    '//div[@class="item"]//div[text()="问政管理"]')  # 问政管理
    vip_app = (By.XPATH,
               '//div[@class="item"]//div[text()="会员管理"]')  # 会员管理
    yunying_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="互动运营"]')  # 互动运营
    live_app = (By.XPATH,
                '//div[@class="item"]//div[text()="互动直播"]')  # 互动直播
    tongji_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="统计分析"]')  # 统计分析
    lawhelp_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="法律援助"]')  # 法律援助
    public_account_app = (By.XPATH,
                          '//div[@class="item"]//div[text()="公众号管理"]')  # 公众号管理
    server_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="服务管理"]')  # 服务管理
    ad_app = (By.XPATH,
              '//div[@class="item"]//div[text()="广告管理"]')  # 广告管理
    zhengqing_app = (By.XPATH,
                     '//div[@class="item"]//div[text()="政情管理"]')  # 政情管理
    notice_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="系统公告"]')  # 系统公告
    hotword_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="热词搜索"]')  # 热词搜索
    user_app = (By.XPATH,
                '//div[@class="item"]//div[text()="用户标签"]')  # 用户标签
    comment_app = (By.XPATH,
                   '//div[@class="item"]//div[text()="评论列表"]')  # 评论列表
    report_app = (By.XPATH,
                  '//div[@class="item"]//div[text()="举报列表"]')  # 举报列表
    feedback_app = (By.XPATH,
                    '//div[@class="item"]//div[text()="反馈管理"]')  # 反馈管理

    def click_study_app(self):
        self.click(self.study_app)

    def click_TV_app(self):
        self.click(self.TV_app)

    def click_reprint_app(self):
        self.click(self.reprint_app)

    def click_points_app(self):
        self.click(self.points_app)

    def click_form_app(self):
        self.click(self.form_app)

    def click_lottery_app(self):
        self.click(self.lottery_app)

    def click_baoliao_app(self):
        self.click(self.baoliao_app)

    def click_quanzi_app(self):
        self.click(self.quanzi_app)

    def click_wenzheng_app(self):
        self.click(self.wenzheng_app)

    def click_vip_app(self):
        self.click(self.vip_app)

    def click_yunying_app(self):
        self.click(self.yunying_app)

    def click_live_app(self):
        self.click(self.live_app)

    def click_tongji_app(self):
        self.click(self.tongji_app)

    def click_lawhelp_app(self):
        self.click(self.lawhelp_app)

    def click_public_account_app(self):
        self.click(self.public_account_app)

    def click_server_app(self):
        self.click(self.server_app)

    def click_ad_app(self):
        self.click(self.ad_app)

    def click_zhengqing_app(self):
        self.click(self.zhengqing_app)

    def click_notice_app(self):
        self.click(self.notice_app)

    def click_hotword_app(self):
        self.click(self.hotword_app)

    def click_user_app(self):
        self.click(self.user_app)

    def click_comment_app(self):
        self.click(self.comment_app)

    def click_report_app(self):
        self.click(self.report_app)

    def click_feedback_app(self):
        self.click(self.feedback_app)

