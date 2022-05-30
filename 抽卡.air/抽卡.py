# -*- encoding=utf8 -*-
__author__ = "Leopzb"

from airtest.core.api import *

auto_setup(__file__,logdir=True)

from airtest.report.report import LogToHtml, simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 自动配置运行环境，如果当前没有连接设备，默认尝试连接Android设备
auto_setup(__file__,logdir=True)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 图片地址可以填写绝对路径
touch(Template(r"D:\Airtest\haidao\抽卡.air\tpl1653811110876.png"))

#sleep(5.0)
#poco(text="我的").click()
sleep(5.0)

#poco(text="任务中心").click()

#poco(text="开始游戏").click()

# 测试报告
# rp = LogToHtml(script_root=r"D:\Airtest\haidao\抽卡.air",log_root=r"D:\Airtest\haidao\log", export_dir=r'D:\Airtest\export',logfile=r'D:\Airtest\haidao\log\log.txt', lang='zh',  plugins=["poco.utils.airtest.report"])
# rp.report(output_file=r"test.html")


#打印测试报告
simple_report(__file__,logpath=True,output=r"D:\Airtest\export\log.html")



















