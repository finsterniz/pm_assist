#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14.05.23 11:31 pm
# @Author  : Hao
# @File    : chatPDF.py

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
    x_coord, _, _, _ = my_tool.find_and_click(gpt_cpy_button, region=(x1, y1, width, height))

    # print(x_coord)

    # 如果没找到，则向上滚动一点，点击， 再向下滚回去
    if x_coord == -1:
        pyautogui.moveTo(785, 500)
        pyautogui.sleep(0.2)
        pyautogui.scroll(15)
        pyautogui.sleep(0.6)
        my_tool.find_and_click(gpt_cpy_button, region=(x1, y1, width, height))
        pyautogui.click()
        pyautogui.sleep(0.2)
        pyautogui.scroll(-60)
        pyautogui.sleep(0.2)
    else:
        pyautogui.click()


# def gpt_copy():
#     # 检测的区域
#     x1, y1 = 100, 250
#     x2, y2 = 1235, 800
#     width = x2 - x1
#     height = y2 - y1
#     my_tool.find_and_click(gpt_copy_button, region=(x1, y1, width, height))
#     pyautogui.click()


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

def extract_redesign(text):
    pattern = r'(<Output Redesign>:\s*\n.*?)(?=\n---)'
    result = re.search(pattern, text, re.DOTALL)
    return result.group(1) if result else None

def generate_question(sentence, i):
    global use_example
    example3 = """
---
EXAMPLE
INPUT:
<Output Redesign>:
1. Implement an IVR (Interactive Voice Response) system at the beginning of the call which can sort the calls based on their nature - customer calls, call dispatching, or technician calls. This reduces the manual effort needed to identify and document the call nature.

2. Train the support service staff to handle all types of calls to eliminate the need for transferring calls, thus reducing call wait times and improving customer service.

3. Utilize AI-powered call routing systems to automatically transfer dispatching and technician calls to the correct business product unit, without the need for a manual transfer.

4. Introduce a digital ticketing system where customers, technicians, or dispatching services can log their concerns or issues. This reduces the reliance on call centers and improves documentation.

5. Consider introducing chatbots or automated online customer service platforms to handle common queries and reduce the volume of calls.

6. Use data analytics to identify peak call times and ensure adequate staffing during these periods to reduce call wait times.

7. Invest in training programs to improve the efficiency and accuracy of the call center staff in identifying and documenting the nature of calls.

OUTPUT:
<heuristics>
For the redesign options proposed, the following heuristics were used:

1. **4.6.1 Task Automation**: Utilizing an IVR system, AI-powered call routing, and automated online customer service platforms to perform tasks that were previously done manually.

2. **4.1.2 Flexible Assignment**: Training the support service staff to handle all types of calls provides more flexibility in task assignment and resource allocation.

3. **4.6.2 Integral Technology**: Applying new technology such as digital ticketing systems, data analytics, and automated customer service platforms to streamline the process and enhance service quality.

4. **1.1 Control Relocation**: By introducing a digital ticketing system, control and input of information is moved from the support staff to the customers, technicians, or dispatch services.

5. **4.2.2 Empower**: By training the support staff to handle a variety of calls, they are given more authority to resolve issues without the need for transferring calls, hence making decision-making more efficient.
   
6. **4.1.6 Numerical Involvement**: By training support staff to handle a variety of calls and reducing the reliance on call centers through automated systems, the number of departments or individuals involved in resolving a query is minimized. This reduces the amount of time spent coordinating tasks and responsibilities among a large number of people or departments.
---\n
"""

    context = f"""\
{extract_redesign(sentence)}
---\n
"""
    task = f"""\
TASK:
1 Please read this pdf to know heuristics in redesign: https://drive.google.com/file/d/19wrt-rl0lBahhJ9yPbyCNoCJSR1WvTZS/view?usp=sharing 
2 Please refer to the EXAMPLE, and tell me what HEURISTICS were used in <Output Redesign>.
3 Please follow the template in EXAMPLE.
"""

    prompt = context + task

    if use_api:
        pass
    elif use_example and i % 9 == 0:  # 每9次发送一次example
        prompt = example3 + prompt

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
    time.sleep(180)
    # 检测生成是否停止
    # wait_for_output()
    # if use_gpt:
    #     gpt_copy()
    # else:
    #     # 复制gpt的回答
    #     y = get_max_y()
    #     my_tool.moveto_and_click(1234, y, delay=0.2)
    #     pyautogui.dragTo(1234, 955, button='left', duration=0.3)
    #     press_keys('command', 'c')
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
    len_shortPara = 1  # 定义短段落的长度，比这个短就直接翻译

    # use_example = False
    use_example = True
    # 刷的个数
    times = 20

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

        # press_keys('command', 'v')
        pyautogui.sleep(1)
        press_keys("down")
        pyautogui.sleep(0.3)

        remain = times - i - 1
        print(f'剩余: {remain}条')
        j += 1
