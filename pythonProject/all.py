"""run.py文件"""

import os
from time import sleep
import json
import pytest


# 测试报告文案获取的文件地址
title_filepath = r"C:\Users\Administrator\PycharmProjects\pythonProject\reports\widgets\summary.json"
# 这里主要是去拿到你的HTML测试报告的绝对路径【记得换成你自己的】
report_title_filepath = r"C:\Users\Administrator\PycharmProjects\pythonProject\reports\index.html"


# 设置报告窗口的标题
def set_windows_title(new_title):
    """
    设置打开的 Allure 报告的浏览器窗口标题文案
    """
    # 定义为只读模型，并定义名称为: f
    with open(report_title_filepath, 'r+', encoding="utf-8") as f:
        # 读取当前文件的所有内容
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        # 循环遍历每一行的内容，将 "Allure Report" 全部替换为 → new_title(新文案)
        for line in all_the_lines:
            f.write(line.replace("Allure Report", new_title))


# 获取 summary.json 文件的数据内容
def get_json_data(name):
    # 定义为只读模型，并定义名称为f
    with open(title_filepath, 'rb') as f:
        # 加载json文件中的内容给params
        params = json.load(f)
        # 修改内容
        params['reportName'] = name
        # 将修改后的内容保存在dict中
        dict1 = params

    # 返回dict字典内容
    return dict1


# 写入json文件
def write_json_data(dict1):
    # 定义为写模式，名称定义为r
    with open(title_filepath, 'w', encoding="utf-8") as r:
        # 将dict写入名称为r的文件中
        json.dump(dict1, r, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./reports --clean")
    sleep(3)
    # 自定义测试报告标题
    set_windows_title("自动化测试")
    # 自定义测试报告标题
    report_title = get_json_data("自动化测试报告")
    write_json_data(report_title)

