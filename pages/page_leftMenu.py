# -*-coding:utf-8-*-
# @FileName  :page_leftMenu.py
# @Time      :2024/4/10 下午3:59
# @Author    :leisijun

"""
左侧菜单页面文件，包含左侧菜单的元素定位和操作方法
"""
from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class LeftMenuPage(BasePage):
    """
    左侧菜单页面
    """
    workbench = (By.XPATH, '//span[text()="工作台"]')  # 工作台
    approval_waited_rep = (By.XPATH, '//span[text()="待审稿库"]')  # 待审稿库
    submission_rep = (By.XPATH, '//span[text()="稿件库"]')  # 稿件库
    suck_manage = (By.XPATH,
                   '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[5]/div/span[2]/span[1]/span/span')
    suck_all = (By.XPATH, '//span[text()="根目录"]')
    suck_mine = (By.XPATH, '//div[text()="我上传的"]')
    suck_zhuanma = (By.XPATH, '//div[text()="素材入库"]')
    suck_Neizhi = (By.XPATH, '//div[text()="内置素材"]')
    suck_inZujian = (By.XPATH, '//div[text()="组件icon"]')
    suck_inPinxuan = (By.XPATH, '//div[text()="品宣icon"]')
    suck_inBackground = (By.XPATH, '//div[text()="客户端导航背景"]')
    suck_inDaohang = (By.XPATH, '//div[text()="客户端导航icon"]')
    suck_inLive = (By.XPATH, '//div[text()="直播背景图"]')
    zujian_manage = (By.XPATH,
                     '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[6]/div/span[2]/span[1]/span/span')  # 组件管理
    banmian_manage = (By.XPATH,
                      '//span[text()="版面管理"]')  # 版面管理
    push_manage = (By.XPATH,
                   '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[7]/div[2]/div[2]/div/span[2]/span[1]/span/span')  # 推送管理
    conf_manage = (By.XPATH,
                   '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[7]/div[2]/div[3]/div/span[2]/span[1]/span/span')  # 配置中心
    wapconf_manage = (By.XPATH,
                      '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[7]/div[2]/div[4]/div/span[2]/span[1]/span/span')  # H5配置中心
    update_manage = (By.XPATH,
                     '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[7]/div[2]/div[5]/div/span[2]/span[1]/span/span')  # 更新版本
    PC_manage = (By.XPATH,
                 '//span[text()="PC 网站"]')  # PC网站
    PCdh_manage = (By.XPATH,
                   '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[8]/div[2]/div[1]/div/span[2]/span[1]/span/span')  # PC网站-导航管理
    PCmb_manage = (By.XPATH,
                   '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[8]/div[2]/div[2]/div/span[2]/span[1]/span/span')  # PC网站-模版管理
    PCconf_manage = (By.XPATH,
                     '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[8]/div[2]/div[3]/div/span[2]/span[1]/span/span')  # PC网站-配置中心
    recycle_manage = (By.XPATH,
                      '//*[@id="app"]/div[1]/section/section/aside/div/div[1]/div[1]/div/div/div[10]/div/span[2]/span[1]/span/span')  # 回收站
    system_settings_menu = (By.XPATH, '//span[text()="系统设置"]')  # 系统设置菜单栏

    # 左侧菜单点击操作

    def click_workbench(self):
        self.click(self.workbench)

    def click_zujian_manage(self):
        self.click(self.zujian_manage)

    def click_suck_manage(self):
        self.click(self.suck_manage)

    def click_banmian_manage(self):
        self.click(self.banmian_manage)

    def click_push_manage(self):
        self.click(self.push_manage)

    def click_conf_manage(self):
        self.click(self.conf_manage)

    def click_wapconf_manage(self):
        self.click(self.wapconf_manage)

    def click_update_manage(self):
        self.click(self.update_manage)

    def click_PC_manage(self):
        self.click(self.PC_manage)

    def click_PCdh_manage(self):
        self.click(self.PCdh_manage)

    def click_PCmb_manage(self):
        self.click(self.PCmb_manage)

    def click_PCconf_manage(self):
        self.click(self.PCconf_manage)

    def click_recycle_manage(self):
        self.click(self.recycle_manage)

    def click_suck_all(self):
        self.click(self.suck_all)

    def click_suck_mine(self):
        self.click(self.suck_mine)

    def click_suck_zhuanma(self):
        self.click(self.suck_zhuanma)

    def click_suck_Neizhi(self):
        self.click(self.suck_Neizhi)

    def click_suck_inZujian(self):
        self.click(self.suck_inZujian)

    def click_suck_inPinxuan(self):
        self.click(self.suck_inPinxuan)

    def click_suck_inBackground(self):
        self.click(self.suck_inBackground)

    def click_suck_inDaohang(self):
        self.click(self.suck_inDaohang)

    def click_suck_inLive(self):
        self.click(self.suck_inLive)
