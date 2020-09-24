# 整个工具的入口
#以下代码都是固定的

import unittest
from utils.HTMLTestRunner import HTMLTestRunner

#1,自动查找所有的case用例
testcase = unittest.defaultTestLoader.discover('case','test_*.py')

#2,使用htmlTestrunner工具来帮助自动运行所有的测试case和生成测试报告
title = "第一次"
descr = "unittest"
filepath = "./report/report.html"
with open(filepath,"wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testcase)