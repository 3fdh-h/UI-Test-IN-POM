# -*-coding:utf-8-*-
# @FileName  :config.py
# @Time      :2024/4/8 14:42
# @Author    :lusong

"""
基础页面，是所有页面的父级页面，定义了页面的基础方法，错误抛出、保存图片等
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 访问页面
    def get(self, url):
        self.driver.get(url)

    # 定位元素
    def locate_element(self, args):
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(args), '没找到元素')
        return self.driver.find_element(*args)

    # 设置元素等待
    def element_wait(self, args, secs=10):
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(args), '没找到元素')

    # 设置值
    def send_keys(self, args, value):
        self.locate_element(args).send_keys(value)

    # 点击元素
    def click(self, args):
        self.locate_element(args).click()

    def is_element_exist(self, args):
        flag = True
        try:
            self.locate_element(args)
            return flag
        except:
            flag = False
            return flag

    # 关闭当前页面并回到首页（建立在句柄已在当前页面的情况）
    def close_and_return(self):
        """
        如果只是测试页面点击是否正常，那么将句柄切换到新建的页面这个动作可以封装进来
        如果需要在新建的页面进行操作，那么需要在执行关闭并返回之前就切到新建的页面
        :return:
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

#     def wait_ele_visible(self, loc, img_desc, timeout=20, frequency=0.5):
#         """等待元素可见"""
#         try:
#             WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
#             log.info("等待:{} - 元素{}可见成功。".format(img_desc, loc))
#         except:
#             log.exception("等待:{} - 元素{}可见失败！".format(img_desc, loc))
#             self.save_img(img_desc)
#             raise
#
#     def get_element(self, loc, img_desc):
#         """查找元素"""
#         try:
#             ele = self.driver.find_element(*loc)
#         except:
#             log.exception("查找:{} - 元素{}失败！".format(img_desc, loc))
#             self.save_img(img_desc)
#             raise
#         else:
#             log.info("查找:{} - 元素{}成功".format(img_desc, loc))
#             return ele
#
#     def click_element(self, loc, img_desc, timeout=20, frequency=0.5):
#         """点击元素"""
#         self.wait_ele_visible(loc, img_desc, timeout, frequency)
#         ele = self.get_element(loc, img_desc)
#         try:
#             ele.click()
#             log.info("点击:{} - 元素{}成功".format(img_desc, loc))
#         except:
#             log.exception("点击:{} - 元素{}失败！".format(img_desc, loc))
#             self.save_img(img_desc)
#             raise
#
#     def input_text(self, loc, value, img_desc, timeout=20, frequency=0.5):
#         """在元素中输入文本"""
#         self.wait_ele_visible(loc, img_desc, timeout, frequency)
#         ele = self.get_element(loc, img_desc)
#         try:
#             ele.send_keys(value)
#             log.info("输入：在{} - 元素{}输入文本值({})成功".format(img_desc, loc, value))
#         except:
#             log.exception("输入：在{} - 元素{}输入文本值({})失败！".format(img_desc, loc, value))
#             self.save_img(img_desc)
#             raise
#
#     def save_img(self, img_description):
#         """保存异常截图"""
#         now = time.strftime("%Y-%m-%d %H-%M-%S ", time.localtime())
#         img_path = os.path.join(IMG_DIR, now + img_description + '.png')
#         try:
#             self.driver.save_screenshot(img_path)
#         except:
#             log.exception("异常截图失败！")
#         else:
#             log.info("异常截图成功，截图存放在{}".format(img_path))
