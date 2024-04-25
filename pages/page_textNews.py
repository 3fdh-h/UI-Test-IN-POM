# -*-coding:utf-8-*-
# @FileName  :page_textNews.py
# @Time      :2024/4/10 16:31
# @Author    :lusong
"""
本文件是文章稿件编辑页面的page文件，包含文章稿件编辑页面的元素定位，操作方法
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class TextNewsPage(BasePage):
    main_title_input = (By.XPATH, '//textarea[@placeholder="填写主标题"]')  # 主标题
    send_to_select = (By.XPATH, '//div[@class="form-view"]/div[3]')  # 发布至
    body_text_input = (By.XPATH, '/html/body/div[1]/div/div[1]/section/div/div[1]/div[2]')
    source_name_input = (By.CSS_SELECTOR,
                         'input[placeholder="请选择来源名称"]')  # 来源名称

    # 选择发布至栏目的元素位置
    send_to_wenzhang = (By.XPATH,
                        '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div/span[2]/i')  # 发布至文章栏目
    send_to_tuji = (By.XPATH,
                    '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div')  # 发布至图集栏目
    send_to_shipin = (By.XPATH,
                      '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div')  # 发布至视频栏目
    send_to_yinpin = (By.XPATH,
                      '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[4]/div/div')  # 发布至音频栏目
    send_to_shipinSet = (By.XPATH,
                         '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div/div')  # 发布至视频合集栏目
    send_to_yinpinSet = (By.XPATH,
                         '/html/body/div[1]/div/div[1]/section/div/div[6]/div[1]/div/div[1]/div/div/div[3]/span/div/div[1]/div[2]/div/div[1]/div/div[1]/div[6]/div/div')  # 发布至音频合集栏目

    # 内容填充完后的操作按钮
    preview_btn = (By.XPATH, '//*[@id="app"]/div/header/div[2]/div[1]/div/div[2]/div[1]/button[1]/span')  # 预览按钮
    publish_btn = (By.XPATH, '//*[@id="app"]/div/header/div[2]/div[1]/div/div[2]/div[1]/button[2]/span')  # 发布按钮
    draft_save_btn = (By.XPATH, '//*[@id="app"]/div/header/div[2]/div[1]/div/div[2]/div[1]/button[3]/span')  # 草稿保存按钮

    preview_back_btn = (By.XPATH, '//div[@class="v_nav_l"]/i')  # 预览后返回按钮

    # 选择封面
    single_img_btn = (By.XPATH, '//span[text()="单图"]')  # 单图按钮
    three_img_btn = (By.XPATH, '//span[text()="三图"]')  # 三图按钮
    big_img_btn = (By.XPATH, '//span[text()="大图"]')  # 大图按钮
    add_icon1 = (By.XPATH, '//div[@id="thumb-card-0"]/div/i')  # 第一个添加图片按钮，三图模式会有三个
    add_icon2 = (By.XPATH, '//div[@id="thumb-card-1"]/div/i')  # 三图的第二个添加图片按钮
    add_icon3 = (By.XPATH, '//div[@id="thumb-card-2"]/div/i')  # 三图的第三个添加图片按钮
    all_resource_tab = (By.XPATH, '//div[@class="el-dialog__body"]//div[text()="全部素材"]')  # 切换到全部素材tab
    upload_resource_btn = (By.XPATH, '//div[@class="el-dialog__body"]//div[@id="upload-scope"]')  # 点击上传素材按钮
    first_pic = (By.XPATH,
                 '/html/body/div[10]/div/div[2]/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]')  # 所有素材中的第一张图片
    first_pic_title = (By.XPATH,
                       '/html/body/div[8]/div/div[2]/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/div[1]/div/h4/span')  # 获取第一个图片元素的title
    dialog_upload_file_input = (
    By.XPATH, '//div[@class="el-dialog__body"]//input[@class="file_input_file"]')  # 从弹出的选择素材对话框中的上传资源文件输入框

    # 智媒助理弹窗关闭，偶尔会弹出来，是一个bug
    zmzl_close_btn = (By.XPATH, '//div[@class="sider-close"]')
    # 填充必要稿签: 主标题、来源名称等
    def fill_required_tag(self, main_title, source_name):
        self.click(self.main_title_input)
        self.send_keys(self.main_title_input, main_title)  # 填写主标题
        # 填写来源名称
        self.click(self.source_name_input)
        self.send_keys(self.source_name_input, source_name)
        self.send_keys(self.source_name_input, Keys.DOWN)
        self.send_keys(self.source_name_input, Keys.ENTER)

    # 填充文章内容
    def fill_article_content(self, content):
        self.send_keys(self.body_text_input, content)

    # 选择发布至指定栏目；因为发布栏目是下拉框，需要先点击下拉框，再选择栏目
    # 因为这个方法可以复用，后续可以将其放在一个统一的文件中
    def select_send_to(self, column):
        """
        :param column: 0-文章，1-图集，2-视频，3-音频，4-视频合集，5-音频合集
        :return:
        """
        self.click(self.send_to_select)  # 点击"发布至"
        if column == 0:
            # 点击"文章栏目"
            self.click(self.send_to_wenzhang)
        elif column == 1:
            self.click(self.send_to_tuji)  # 点击"图集栏目"
        elif column == 2:
            self.click(self.send_to_shipin)  # 点击"视频栏目"
        elif column == 3:
            self.click(self.send_to_yinpin)  # 点击"音频栏目"
        elif column == 4:
            self.click(self.send_to_shipinSet)  # 点击"视频合集栏目"
        elif column == 5:
            self.click(self.send_to_yinpinSet)  # 点击"音频合集栏目"

    def finish_publish(self, opt):
        """
        完成发布操作
        :param opt: 1-预览；2-发布；3-草稿保存
        :return:
        """
        if opt == 1:
            self.click(self.preview_btn)
        elif opt == 2:
            self.click(self.publish_btn)
        elif opt == 3:
            self.click(self.draft_save_btn)

    def choose_pic(self, add_icon):
        """
        选择封面图
        :param add_icon: 上传按钮的元素位置
        :return:
        """
        self.click(add_icon)  # 点击上传封面icon
        self.click(self.all_resource_tab)  # 进入全部素材tab
        actions = ActionChains(self.driver)  # 使用ActionChains实现悬浮和移动光标
        actions.move_to_element(self.first_pic).perform()  # 移入第一张图片
        actions.move_by_offset(20, 0).perform()  # 向右偏移20像素
        actions.click().perform()  # 点击

    def choose_cover_style(self, style):
        """
        选择封面图样式：无图、单图、三图、大图
        :param style: 0-无图，1-单图，2-三图，3-大图
        :return:
        """
        if style == 0:
            pass  # 默认无图，无需操作
        elif style == 1:
            self.click(self.single_img_btn)
            self.choose_pic(self.add_icon1)
        elif style == 2:
            self.click(self.three_img_btn)
            self.choose_pic(self.add_icon1)
            self.choose_pic(self.add_icon2)
            self.choose_pic(self.add_icon3)
        elif style == 3:
            self.click(self.big_img_btn)
            self.choose_pic(self.add_icon1)
