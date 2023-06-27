#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15.06.23 1:23 am
# @Author  : Hao
# @File    : thesis_gen_redesign01.py
# 使用api生成gpt对案例的回答

import numpy as np
import pyautogui
import time
import my_tool
from PIL import ImageGrab
import pyperclip
import os
import sys
import re
from gpt_basic_api import ask_gpt


def gpt_copy():
    gpt_cpy_button = '/Users/a/PycharmProjects/pythonProject/pyautogui项目/截图/gpt_click.png'
    # 检测的区域
    x1, y1 = 1062, 0
    x2, y2 = 1235, 777
    width = x2 - x1
    height = y2 - y1
    my_tool.find_and_click(gpt_cpy_button, region=(x1, y1, width, height))
    pyautogui.click()



# 定义一个执行按键操作的函数
def press_keys(*keys):
    for key in keys:
        pyautogui.keyDown(key)
    for key in reversed(keys):
        pyautogui.keyUp(key)


def is_single_word(text):
    words = text.split()
    return len(words) == 1


# 定义一个函数，用于检查两个颜色是否在公差范围内匹配
def color_matches(color1, color2, tolerance):
    return all(abs(a - b) <= tolerance for a, b in zip(color1, color2))


def get_max_y():
    # 定义屏幕区域和目标颜色
    x1, y1 = 1234, 250
    x2, y2 = 1235, 888
    # target_color = (1, 52, 132)
    target_color = (37, 61, 98)
    tolerance = 3

    # 捕获屏幕截图
    screenshot = pyautogui.screenshot()

    # 裁剪指定区域的图像
    region = screenshot.crop((x1, y1, x2, y2))

    # 初始化变量以记录y坐标最大的像素点
    max_y = -1

    # 遍历指定区域内的像素点
    for y in range(region.height - 1, -1, -1):  # 逆序遍历
        # 获取当前像素点的颜色
        pixel_color = region.getpixel((0, y))

        # print(pixel_color)
        # print(target_color)

        # 如果颜色与目标颜色匹配
        if color_matches(pixel_color, target_color, tolerance):
            # 更新y坐标最大的像素点
            max_y = max(max_y, y)
            break

    # 计算在屏幕坐标系中的y坐标
    max_y += y1
    return max_y


def monitor_area(left, top, right, bottom, pause=3.0, sample_size=1):
    last_screen = None
    while True:
        # Grab the screen
        screen = ImageGrab.grab(bbox=(left, top, right, bottom))

        # Downsample the screen
        width, height = screen.size
        pixels = screen.load()
        current_screen = [[pixels[x, y] for x in range(0, width, sample_size)] for y in range(0, height, sample_size)]
        current_screen = np.array(current_screen)

        if last_screen is not None:
            if np.all(current_screen == last_screen):
                return True
        last_screen = current_screen
        time.sleep(pause)


def find_character(input_string, character):
    if character in input_string:
        index = input_string.index(character)
        return index
    else:
        return 0


def generate_question(sentence, i):
    global use_example
    example3 = """
You are a process mining expert, your task is to give some possible redesign Output based on Input Case, please follow the EXAMPLE below, and give a redesign Output for the <Input Case> I gave.
---
EXAMPLE
<Input Case>: 
In a university registrar’s office processes, employee manually enters students’ data into the system. Which lead to long processing times.
<Output Redesign>: 
1 Hire more staff to handle the process.
2 The students are to enter their personal data into the system themselves. 
3 The data entry activities can be automated, for instance performed automatically by the system itself.
---\n
"""

    prompt = f"""\
<Input Case>: 
{sentence}
"""

    if use_api:
        pass
    elif use_example and i % 6 == 0:  # 每9次发送一次example
        prompt = example3 + prompt
        # use_example = False

    return prompt


def reset_chat_pdf():
    my_tool.moveto_and_click(1198, 118, 0.1)
    pyautogui.click()


def click_mn():
    my_tool.moveto_and_click(1298, 481, 0.1)
    # my_tool.moveto_and_click(3240, 481, 0.1)


def template_patter():
    pyautogui.sleep(0.1)

    click_mn()  # 最后总要切回mn


def edit_mode():
    # my_tool.moveto_and_click(495, 1026, 0.5)
    if use_gpt:
        my_tool.moveto_and_click(495, 985, 0.5)
    else:
        my_tool.moveto_and_click(495, 1000, 0.5)

    pyautogui.click()


def restart_script():
    os.execv(sys.executable, ['python'] + sys.argv)


# 提取出gpt的回答作为content进行返回
def extract_contents(text):
    pattern = r'1\s*"([^"]*)"\s*2\s*(.*)}'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        content1 = match.group(1)
        content2 = match.group(2)
        return content1, content2
    else:
        return None, None


def wait_for_output(max_wait_time=30):
    start_time = time.time()  # 记录开始时间

    while True:
        if monitor_area(412, 300, 1208, 953):
            break
        elif time.time() - start_time >= max_wait_time:
            restart_script()
            # reset()  # 调用 reset() 函数
            break


def contains_chinese(s):
    # 正则表达式匹配任何中文字符
    return re.search(r'[\u4e00-\u9fa5]', s)


def contain_substring(ziel_str, substr_list):
    # 对于每个子字符串，检查它是否在原字符串中
    for substr in substr_list:
        if substr in ziel_str:
            return True
    # 如果没有子字符串在原字符串中，返回False
    return False


def set_title():
    pyautogui.sleep(0.3)
    pyautogui.hotkey('command', 'enter')
    pyautogui.sleep(0.3)
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("esc")


def open_translate():
    # open translate
    pyautogui.moveTo(3600, 200, 0.2)
    pyautogui.click()
    pyautogui.click()


def translate_in_deepl():
    press_keys('command', 'a')
    pyautogui.sleep(0.2)
    press_keys('command', 'v')
    pyautogui.sleep(3)
    # 复制
    copy_translation()
    # 添加分隔符


def copy_translation():
    pyautogui.moveTo(3770, 942, 0.2)
    pyautogui.click()
    pyautogui.sleep(0.2)
    pyautogui.click()
    pyautogui.sleep(0.1)
    temp4 = pyperclip.paste()
    if not temp4.endswith('------------------'):
        temp4 += "\n------------------"
    pyperclip.copy(temp4)
    pyautogui.sleep(0.1)


def past():
    press_keys('command', 'v')
    pyautogui.sleep(0.2)


def extract_text(article):
    # 如果在文本中找不到"}"，则提取从"1: "到文本结尾的所有内容
    # 否则，提取从"1: "到"}"的内容
    pattern = '(1: .*)' if '}' not in article else '(1: .*?)(?=})'

    # 在文章中查找模式
    result = re.search(pattern, article, re.S)

    rs = result.group(1).strip()
    if not contains_chinese(rs):
        return ''

    # 如果找到了匹配的文本，返回该文本，否则返回空字符串
    return rs if result else ''


def use_client():
    pyperclip.copy(chars)
    edit_mode()
    wait_for_output()
    press_keys('command', 'v')
    pyautogui.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(5)
    # 检测生成是否停止
    wait_for_output()
    if use_gpt:
        gpt_copy()
    else:
        # 复制gpt的回答
        y = get_max_y()
        my_tool.moveto_and_click(1234, y, delay=0.2)
        pyautogui.dragTo(1234, 955, button='left', duration=0.3)
        press_keys('command', 'c')
    pyautogui.sleep(0.5)
    cur_content = pyperclip.paste()
    cur_content += "\n------------------"

    pyperclip.copy(cur_content)


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    use_gpt = True  # 使用gpt客户端而不是chatPDF

    # use_api = True  # 使用gpt的api
    use_api = False  # 使用客户端

    model = "gpt-4"
    # model = "gpt-3.5-turbo"

    # len_shortPara = 666  # 定义短段落的长度，比这个短就直接翻译
    # len_shortPara = 100  # 定义短段落的长度，比这个短就直接翻译

    # len_shortPara = 1  # 纯生成
    len_shortPara = 100000  # 纯翻译


    # use_example = False
    use_example = True
    # 刷的个数
    times = 5

    pyautogui.sleep(3)

    if use_api:
        click_mn()
    else:
        template_patter()

    times_unmatch = 0

    # i是总数， j是提问gpt的数目
    j = 0
    # while i < times:
    for i in range(times):
        press_keys('command', 'c')

        pyautogui.sleep(0.5)

        # 读取剪贴板的内容
        clipboard_content = pyperclip.paste()

        pyautogui.sleep(0.2)

        # 若长度太短，段落就不翻译了
        if len(clipboard_content) < len_shortPara:
            print("短段落, 进行翻译")
            open_translate()
            translate_in_deepl()
            click_mn()
            # set_title()
            past()
            pyautogui.sleep(1)
            pyautogui.press("down")
            pyautogui.sleep(0.2)
            continue

        pyautogui.sleep(0.2)

        # # 将新的内容保存到剪贴板
        chars = generate_question(clipboard_content, j)

        if use_api:
            usr_msg = chars
            sys_msg = """\
You are an AI text transformation specialist, your task is to convert complex scientific or technical PARAGRAPH into a more understandable form. Here is a PARAGRAPH that needs your transformation. Please follow the EXAMPLE. In your response, please try to do the following TASK as much as possible:
---
EXAMPLE
Input: PARAGRAPH
Output: 
主题: SUBHEADING
1. LIST OF SUMMARY
---
"""
            ans_api = ask_gpt(usr_msg=usr_msg, sys_msg=sys_msg, model=model)
            print(usr_msg)
            print(sys_msg)
            ans_api += "\n------------------"
            pyperclip.copy(ans_api)
        else:
            use_client()
            click_mn()

        press_keys('command', 'v')
        pyautogui.sleep(1)
        press_keys("down")
        pyautogui.sleep(0.3)

        remain = times - i - 1
        print(f'剩余: {remain}条')
        j += 1
