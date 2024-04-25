# -*-coding:utf-8-*-
# @FileName  :test_leftMenu.py
# @Time      :2024/4/10 下午4:08
# @Author    :leisijun
import time

import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.page_leftMenu import LeftMenuPage


@pytest.mark.usefixtures("begin_to_end")
class TestLeftMenu:
    @allure.title("PC网站-配置中心")
    def test_click_PCconf_manage(self, begin_to_end):
        """
        测试PC配置管理能否进入
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_PCconf_manage()
        time.sleep(10)
        # # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("pcConfig")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "基础配置" in html_content
        except NoSuchElementException:
            pytest.fail("未找到页面元素，用例未通过")
        finally:
            self.driver.switch_to.default_content()
            time.sleep(10)

    @allure.title("测试素材库管理")
    def test_click_suck_manage(self, begin_to_end):
        """
        测试素材库管理能否点击进入
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_manage()
        time.sleep(3)
        element_xpath = '//span[text()="根目录"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "根目录"

    @allure.title("测试素材库-我上传的")
    def test_click_suck_mine(self, begin_to_end):
        """
        测试我的素材库
        :param begin_to_end:
        :return:
        """
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_mine()
        time.sleep(3)
        element_xpath = '//span[text()="根目录"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "根目录"

    @allure.title("测试素材库-素材入库")
    def test_click_suck_zhuanma(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_zhuanma()
        time.sleep(3)
        element_xpath = '//div[text()="素材转码"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "素材转码"

    @allure.title("测试素材库-内置素材")
    def test_click_suck_Neizhi(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_Neizhi()
        time.sleep(3)
        element_xpath = '//span[text()="24节气"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "24节气"

    @allure.title("测试素材库-组件icon")
    def test_click_suck_inZujian(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_inZujian()
        time.sleep(3)
        element_xpath = '//span[text()="组件icon"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "组件icon"

    @allure.title("测试素材库-内置素材-品宣icon")
    def test_click_suck_inPinxuan(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_inPinxuan()
        time.sleep(3)
        element_xpath = '//span[text()="品宣"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "品宣"

    @allure.title("测试素材库-内置素材-客户端导航背景")
    def test_click_suck_inBackground(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_inBackground()
        time.sleep(3)
        element_xpath = '//span[text()="个人中心背景"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "个人中心背景"

    @allure.title("测试素材库-内置素材-客户端导航icon")
    def test_click_suck_inDaohang(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_inDaohang()
        time.sleep(3)
        element_xpath = '//span[text()="线性图标-红色"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "线性图标-红色"

    @allure.title("测试素材库-内置素材-直播背景图")
    def test_click_suck_inLive(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_suck_inLive()
        time.sleep(3)
        element_xpath = '//span[text()="红色背景图"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "红色背景图"

    @allure.title("测试组件管理")
    def test_click_zujian_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_zujian_manage()
        time.sleep(3)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("compoManagement")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "搜索组件" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(3)

    @allure.title("测试版面管理")
    def test_click_banmian_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_banmian_manage()
        time.sleep(3)
        element_xpath = '//*[@id="app"]/div[1]/section/section/main/div[1]/div[1]/div[1]/button'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "新建模块"

    @allure.title("测试推送管理")
    def test_click_push_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_push_manage()
        time.sleep(3)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("pushManagement")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "预览并推送" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(3)

    @allure.title("测试配置中心")
    def test_click_conf_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_conf_manage()
        time.sleep(3)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("cathi")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "发布" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(3)

    @allure.title("PC网站-配置中心")
    def test_click_wapconf_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_wapconf_manage()
        time.sleep(5)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("wapConfig")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "基础配置" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(15)

    @allure.title("手机客户端-更新版本")
    def test_click_update_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_update_manage()
        time.sleep(5)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("appManagement")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "更新版本" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(3)

    @allure.title("PC网站-模板管理")
    def test_click_PCmb_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_PCmb_manage()
        time.sleep(3)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("templateManagement")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "创建模板" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(10)

    @allure.title("PC网站-导航管理")
    def test_click_PCdh_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_PCdh_manage()
        time.sleep(5)
        # 使用JavaScript在shadowRoot中查找元素
        try:
            iframe = self.driver.find_element_by_name("pcNavManagement")
            self.driver.switch_to.frame(iframe)
            html_content = self.driver.page_source
            assert "搜索导航" in html_content
        except NoSuchElementException:
            print("这条用例没有执行通过需要进行排查：", e)
        finally:
            self.driver.switch_to.default_content()
            time.sleep(10)

    @allure.title("回收站")
    def test_click_recycle_manage(self, begin_to_end):
        self.driver = begin_to_end
        lm = LeftMenuPage(self.driver)
        lm.click_recycle_manage()
        time.sleep(3)
        element_xpath = '//*[@id="tab-myTrash"]'
        sck_tab = self.driver.find_element(By.XPATH, element_xpath)
        assert sck_tab.text == "素材回收"
        time.sleep(3)
