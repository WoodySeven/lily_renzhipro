#!/usr/bin/env python
"""
小工具的函数库
"""
import os
import shutil
import time


def capture_screen(driver, file_name=None):
    """对浏览器内部截图
    如果成功，返回路径，如果不成功，返回None
    """
    pic_path = "./screenshots/mypic_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")
    if file_name is None:
        driver.get_screenshot_as_file(pic_path)
    else:
        driver.get_screenshot_as_file(file_name)
        pic_path = file_name
    if os.path.exists(pic_path):
        return pic_path

