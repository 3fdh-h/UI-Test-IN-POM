# -*-coding:utf-8-*-
# @FileName  :config.py
# @Time      :2024/4/8 14:42
# @Author    :lusong

import os
import shutil
import time
import pytest

if __name__ == '__main__':
    shutil.rmtree('./result', ignore_errors=True)  # 运行前删掉之前的测试结果
    time.sleep(3)
    pytest.main(['-vs', './testcases', '--alluredir=./result'])
    time.sleep(5)
    # # pytest.main(['-vs', './TestCase', '--alluredir=./result', '-n=5', '--reruns=2'])
    # # split = 'allure' + ' generate' + ' ./report/result' + ' -o' + ' ./report/html' + ' --clean'
    # os.system('allure generate ./result -o ./report/html --clean')
    # time.sleep(1)
    # os.system('allure serve ./result/html')
