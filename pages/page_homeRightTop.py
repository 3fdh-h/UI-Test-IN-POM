# -*-coding:utf-8-*-
# @FileName  :page_homeRightTop.py
# @Time      :2024/4/9 18:54
# @Author    :lusong

"""
系统首页右上角的功能模块，包括访问其他端的页面、开发者服务中心、应用中心、通知、用户头像等
"""
from selenium.webdriver.common.by import By
from base.BasePage import BasePage
import config


class RightTopPage(BasePage):
    phone_and_pc = (By.XPATH, '//*[@id="app"]/div[1]/section/header/div/div/div[2]/section[4]/div/div/i')  # 跳转其他端的按钮
    # 悬浮在图标上面弹出的气泡
    download_app = (By.XPATH, '/html/body/ul/li[1]/div')  # 下载手机APP链接按钮
    visit_pc = (By.XPATH, '/html/body/ul/li[2]/div')  # 访问PC网站链接
    visit_wap = (By.XPATH, '/html/body/ul/li[3]/div')  # 访问手机网站链接
