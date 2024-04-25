# -*-coding:utf-8-*-
# @FileName  :test_app.py
# @Time      :2024/4/10 下午6:03
# @Author    :leisijun
import time
from telnetlib import EC

import allure
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_app import AppPage


@pytest.mark.usefixtures("begin_to_end")
class TestApp:

    @allure.title("课程学习应用")
    def test_click_study_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_study_app()  # 点击应用操作
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/section/section/section/section/main/div/div/div[1]/button'  # 订阅需要验证的元素的XPath
            study_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert study_btn.text == "创建课程"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("电视广播应用")
    def test_click_TV_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_TV_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div[1]/button'  # 订阅需要验证的元素的XPath
            TV_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert TV_btn.text == "创建频道"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("稿件转载应用")
    def test_click_reprint_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_reprint_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="manuscript"]/div[2]/div[1]/div[1]/div[1]/div[1]/button'  # 订阅需要验证的元素的XPath
            reprint_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert reprint_btn.text == "保存视图"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("积分商城应用")
    def test_click_points_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_points_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div[1]/button'  # 订阅需要验证的元素的XPath
            point_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert point_btn.text == "新建商品"
        except NoSuchElementException or TimeoutException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("表单管理应用")
    def test_click_form_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_form_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/section/section/main/section/div/div[1]/div[2]/div[2]/button'  # 订阅需要验证的元素的XPath
            form_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert form_btn.text == "新建"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("抽奖管理应用")
    def test_click_lottery_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_lottery_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/section/section/aside/div/div[1]/div/ul/div[2]/a/li/span'  # 订阅需要验证的元素的XPath
            lot_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert lot_btn.text == "抽奖列表"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("报料管理应用")
    def test_click_baoliao_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_baoliao_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/div/div/div[1]/div/ul/div[1]/a/li/span'  # 订阅需要验证的元素的XPath
            bl_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert bl_btn.text == "报料管理"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("圈子管理应用")
    def test_click_quanzi_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_quanzi_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div[1]/button'  # 订阅需要验证的元素的XPath
            qz_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert qz_btn.text == "添加动态"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("问政管理应用")
    def test_click_wenzheng_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_wenzheng_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="pane-0"]/div[1]/div[2]/button[2]'  # 订阅需要验证的元素的XPath
            wz_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert wz_btn.text == "导出表格"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("会员管理应用")
    def test_click_vip_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_vip_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[1]/button'  # 订阅需要验证的元素的XPath
            vip_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert vip_btn.text == "搜索"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("互动运营应用")
    def test_click_yunying_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_yunying_app()
        try:
            self.driver.switch_to_window(self.driver.window_handles[-1])
            time.sleep(10)
            assert self.driver.title == "系统通知-云点"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("互动直播应用")
    def test_click_live_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_live_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/section/section/section/section/main/div/div/div/div[1]/div/div[2]/div/div[1]/button'  # 订阅需要验证的元素的XPath
            live_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert live_btn.text == "创建直播"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("统计分析应用")
    def test_click_tongji_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_tongji_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="mainScrollbar"]/section/div[1]/div[1]/button'  # 订阅需要验证的元素的XPath
            tj_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert tj_btn.text == "截图分享"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("法律援助应用")
    def test_click_lawhelp_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_lawhelp_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/div/div/div[1]/div/ul/div[1]/a/li'  # 订阅需要验证的元素的XPath
            lawhelp_text = self.driver.find_element(By.XPATH, element_xpath)
            assert lawhelp_text.text == "问题管理"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("公众号管理应用")
    def test_click_public_account_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_public_account_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div[1]/div/div/div/div[1]/div/ul/div[2]/li/div'  # 订阅需要验证的元素的XPath
            account_text = self.driver.find_element(By.XPATH, element_xpath)
            assert account_text.text == "审核管理"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("服务管理应用")
    def test_click_server_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_server_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div/button'  # 订阅需要验证的元素的XPath
            serv_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert serv_btn.text == "保存"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("广告管理应用")
    def test_click_ad_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_ad_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div[1]/div/section/div/div[1]/div[2]/button'  # 订阅需要验证的元素的XPath
            ad_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert ad_btn.text == "新建广告计划"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("政情管理应用")
    def test_click_zhengqing_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_zhengqing_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/section/div/div[1]/div[2]/button'  # 订阅需要验证的元素的XPath
            zq_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert zq_btn.text == "添加政情人员"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("系统公告应用")
    def test_click_notice_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_notice_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/section/section/section/div[1]'  # 订阅需要验证的元素的XPath
            nt_btn = self.driver.find_element(By.XPATH, element_xpath)
            assert nt_btn.text == "新建公告"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("热词搜索应用")
    def test_click_hotword_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_hotword_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/div/div[1]/span[1]'  # 订阅需要验证的元素的XPath
            hot_text = self.driver.find_element(By.XPATH, element_xpath)
            assert hot_text.text == "热词设置"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("用户标签应用")
    def test_click_user_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_user_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/div/h3/span'  # 订阅需要验证的元素的XPath
            user_text = self.driver.find_element(By.XPATH, element_xpath)
            assert user_text.text == "用户标签"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("评论列表应用")
    def test_click_comment_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_comment_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/header/div/div[1]/div[1]/span[2]'  # 订阅需要验证的元素的XPath
            com_text = self.driver.find_element(By.XPATH, element_xpath)
            assert com_text.text == "评论列表"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("举报列表应用")
    def test_click_report_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_report_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/header/div/div[1]/div[1]/span[2]'  # 订阅需要验证的元素的XPath
            repr_title = self.driver.find_element(By.XPATH, element_xpath)
            assert repr_title.text == "举报列表"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()

    @allure.title("反馈管理应用")
    def test_click_feedback_app(self, begin_to_end):
        self.driver = begin_to_end
        ap = AppPage(self.driver)
        ap.click_feedback_app()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(5)
        try:
            element_xpath = '//*[@id="app"]/div/div/header/div/div[1]/div[1]/span[2]'  # 订阅需要验证的元素的XPath
            fdb_title = self.driver.find_element(By.XPATH, element_xpath)
            assert fdb_title.text == "反馈管理"
        except NoSuchElementException:
            pytest.fail("加载失败，未发现页面元素")
        finally:
            ap.close_and_return()
