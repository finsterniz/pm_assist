#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22.06.23 12:49 am
# @Author  : Hao
# @File    : temp_heuristic翻译矫正.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12.05.23 11:27 am
# @Author  : Hao
# @File    : ferman笔记本.py

import pyautogui
import pyperclip
import my_tool
import datetime
import json
import os
from chatPDF import wait_for_output, get_max_y, gpt_copy
import re


def generate_sum(sentence):
    example3 = """
You are an AI text transformation specialist, your task is to convert complex scientific or technical PARAGRAPH into a more understandable form. Here is a PARAGRAPH that needs your transformation. Please follow the EXAMPLE. In your response, please try to do the following TASK as much as possible:
---
EXAMPLE
Input: Response Variation: In the context of human-bot con-versational dialogs, ChatGPT may produce varied responses for exact same queries. For example, we observed that a query such as ‘... what architectural style can be best suited to CampusBike system’ may yield varied responses, such as microservices, layered, client-server etc. architecture can be best suited for the system. This and alike variation in recom-mendations or scripted artifacts (UML script, ASR specifica-tion etc.) can impact the consistency of architecting process and ultimately varied analysis, synthesis, and evaluation of the architecture. One of the solutions to minimize response variations is an iterative dialog with ChatGPT to refine its output and architects’ oversight to ensure that the architectural artifacts being produced are consistent and coherent.
Output: 
主题：ChatGPT的回答不稳定性及其影响
1. ChatGPT的回答不稳定性：
在人机对话的场景中，ChatGPT可能会对完全相同的查询产生不同的回答。例如，当问到“…最适合CampusBike系统的架构风格是什么？”时，它可能会提供微服务、分层、客户端-服务器等不同的架构风格作为最适合的答案。

2. 应对不稳定性的影响：
这种不稳定性会影响到架构设计过程的一致性，最终导致对架构的分析、综合和评价结果不同。而且，这种不稳定性还可能影响到脚本工件（如UML脚本、ASR规范等）的推荐和编制。

3. 解决方案：
为了降低回答不稳定性，我们可以通过反复与ChatGPT对话来改进其输出，同时由架构师进行监督，确保生成的架构工件保持一致和连贯。

总结: ChatGPT的回应具有不稳定性，即对相同问题产生不同回答，可能影响回应的质量。可以通过多次生成回应和校验确保架构工件的一致性。
---\n
"""

    prompt = f"""\
PARAGRAPH
{sentence}
---
TASK:
1. Break down complex processes into simple steps
2. Use subheadings to organize content
3. Present a clear structure, ideally in list format
4. Simplify complex concepts and sentences
5. Use plain, understandable language
6. Conclude the PARAGRAPH as few words as possible at the end, as in the EXAMPLE.
7. Output in Chinese(用中文输出)
"""

    prompt = example3 + prompt

    return prompt


def open_translate():
    # open translate
    pyautogui.moveTo(3600, 200, 0.1)
    pyautogui.click()
    pyautogui.click()


def preprocess_input(text):
    return text.replace('\n', ' ')


def load_statistics():
    if not os.path.exists("../pyautogui项目/statistic.json"):
        return {"date": None, "count": 0}
    with open("../pyautogui项目/statistic.json", "r") as f:
        return json.load(f)


def save_statistics(data):
    with open("../pyautogui项目/statistic.json", "w") as f:
        json.dump(data, f)


def read_statistics():
    today = datetime.date.today().strftime("%Y-%m-%d")
    stats = load_statistics()
    if stats["date"] != today:
        stats["date"] = today
        stats["count"] = 0
    return stats["count"]


def incre_statistics():  # 自增并返回当前统计
    today = datetime.date.today().strftime("%Y-%m-%d")
    stats = load_statistics()
    if stats["date"] != today:
        stats["date"] = today
        stats["count"] = 0
    stats["count"] += 1
    save_statistics(stats)
    return stats["count"]


def decre_statistics():  # 自减并返回当前统计
    today = datetime.date.today().strftime("%Y-%m-%d")
    stats = load_statistics()
    if stats["date"] != today:
        stats["date"] = today
        stats["count"] = 0
    stats["count"] -= 1
    save_statistics(stats)
    return stats["count"]


def open_terminal():
    x = 1286
    y = 815
    # pyautogui.moveTo(3230, 815, 0.1)
    pyautogui.moveTo(x, y, 0.1)
    pyautogui.click()


def open_mn():
    x = 3240
    y = 815
    pyautogui.moveTo(x, y, 0.1)
    pyautogui.click()


def edit_mode():
    pyautogui.moveTo(777, 977, 0.1)
    # pyautogui.moveTo(546, 984, 0.1)
    pyautogui.click()
    pyautogui.click()


def set_title():
    pyautogui.sleep(0.1)
    pyautogui.hotkey('command', 'enter')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('command', 'a')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('command', 'v')
    pyautogui.sleep(0.3)
    pyautogui.press("esc")
    pyautogui.sleep(0.2)


def copy_translation():
    pyautogui.moveTo(3770, 942, 0.2)
    pyautogui.click()
    pyautogui.sleep(0.2)
    pyautogui.click()
    pyautogui.sleep(0.1)
    temp4 = pyperclip.paste()
    temp4 += "\n------------------"
    pyperclip.copy(temp4)
    pyautogui.sleep(0.2)
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    pyautogui.sleep(0.2)
    open_terminal()
    pyautogui.press("enter")
    print("已粘贴翻译")
    print_seperator()


def jump():
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.press("down")
    pyautogui.sleep(0.1)
    pyautogui.press("down")
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    mn_quick_edit()
    open_terminal()
    pyautogui.press("enter")
    print("已跳过 2 个")
    print_seperator()


def press_keys(*keys):
    for key in keys:
        pyautogui.keyDown(key)
        pyautogui.sleep(0.1)
    for key in reversed(keys):
        pyautogui.keyUp(key)
        pyautogui.sleep(0.1)


def move_prev():
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.press("up")
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    open_terminal()
    pyautogui.press("enter")
    print("移动至上段")
    print_seperator()


def move_next():
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.press("down")
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    mn_quick_edit()
    open_terminal()
    pyautogui.press("enter")
    print("移动至下段")
    print_seperator()


# 重新总结
def undo():
    # decre_statistics()  # 因为引入gpt的答案，所以经常decre也正常，没必要减
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'z')
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'z')
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    open_terminal()
    pyautogui.sleep(0.5)
    pyautogui.press("enter")
    print("请重新总结")
    print_seperator()


# I am going to provide a template for your output. Everything in all caps is a placeholder. Any time that you generate text, you should try to fit it into one of the placeholders that I list. Please preserve the formatting and overall Template that I provide here:
def input_prompt_template():
    global prompt_chinese
    prompt = """\
I am going to provide a template for your evaluation. Everything in all caps is a placeholder. Your answer cannot exceed the scope of the template.:
---
Template:
{
1: EVALUATION,
2: EXPLANATION
3: YOUR SUMMARY     
}
---
Are you ready?
"""
    # prompt_chinese = "From now on, please answer in chinese, understand?"
    reset()
    input_to_gpt(prompt)
    wait_for_output()
    input_to_gpt(prompt_chinese)
    copy_text_back()
    print("已经重新输入template")
    print_seperator()


def generate_question(begin_para, my_smr):
    if gpt_mode:  # gpt模式，不用考虑文章长度，而是全部复制
        question_for_gpt = f'''\
In the following are a paragraph and my summary to it.
---
PARAGRAPH
{begin_para}
---
SUMMARY
{my_smr}
---
YOUR TASK:
# (请用中文回答和使用Template)
1 Evaluation: Evaluation to my summary (if cover the main points?).
2 Correct: Explain what is correct.
3 Missed: Explain what is missed.
4 Summarize: Summarize the entire paragraph as few words as possible.
'''
    # 请用中文回答,使用Template,answer in as few words as possible.)
    # (请用中文回答和使用Template)
    # Explain in detail what is correct.

    else:
        question_for_gpt = f'''\
In the following are the beginning of a paragraph and my summary to it.
---
PARAGRAPH
{begin_para[:188]} ...
---
SUMMARY
{my_smr}
---
YOUR TASK:
(请用中文回答和使用Template)
1 Evaluation(essentially correct/incorrect) to my summary of the core idea of this entire paragraph.
2 Explain in detail what is correct.
3 Explain in detail what is missed.
4 Summarize the entire paragraph as few words as possible.
'''
    return question_for_gpt


def ask_context(cur_con, cur_quest):
    complete_question = f"""\
PARAGRAPH
{cur_con}
---
QUESTION
{cur_quest}
"""
    input_to_gpt(complete_question)
    copy_text_back()
    print("已针对这一段进行提问")
    print_seperator()


def ask(ctxt):
    complete_question = generate_sum(ctxt)

    input_to_gpt(complete_question)
    copy_text_back()
    print("已针对这一段进行提问")
    print_seperator()


def select_current():
    copy_text_back()
    print("已经选中当前")
    print_seperator()


def reset():
    my_tool.moveto_and_click(1198, 118, 0.1)
    pyautogui.click()
    pyautogui.click()


# def reset():
#     global prompt_chinese
#     my_tool.moveto_and_click(1198, 118, 0.1)
#     pyautogui.click()
#     pyautogui.click()
#     input_to_gpt(prompt_chinese)
#     pyautogui.sleep(0.1)

def input_to_gpt(temp_content):
    pyperclip.copy(temp_content)
    edit_mode()
    pyautogui.hotkey('command', 'v')
    # 按下回车键
    pyautogui.press('enter')


# 用于去除标题后的英文字母
def remove_trailing_letter(s):
    # 使用正则表达式检查字符串末尾是否包含英文字母
    if re.search('[a-zA-Z]$', s):
        # 如果有，则删除最后的英文字母
        return s[:-1]
    else:
        # 如果没有，则返回原字符串
        return s


def t_set_title(input_text):  # 使用terminal来设置标题
    temp1 = remove_trailing_letter(input_text)
    pyperclip.copy(temp1)
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'enter')
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("esc")
    pyautogui.press("down")
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')

    mn_quick_edit()

    open_terminal()
    pyautogui.sleep(0.2)
    pyautogui.press("enter")
    print(f"标题已经设定为:  \n {temp1}")
    print_seperator()


# 把text打碎成列表， 用于翻译
def text_to_list(text):
    sentences = text.split('. ')
    sentences_list = []
    output_text = ""
    for i, sentence in enumerate(sentences):
        if sentence.strip():  # this will ignore empty sentences
            # sentences_list.append(str(i + 1) + ' ' + sentence.strip())
            output_text += (str(i + 1) + '. ' + sentence.strip() + "\n")
    return output_text


def print_seperator():
    print("\n-----------------------------------------------------------------------------\n")


def reset_chatPDF():
    reset()
    input_to_gpt(prompt_chinese)
    copy_text_back()
    print("已经重置chatPDF")
    print_seperator()


def wen(input_content):  # 直接食用terminal进行提问
    input_question = input_content[:-1]
    complete_question = f"{input_question}"
    input_to_gpt(complete_question)

    copy_text_back()
    print("提问完成")
    print_seperator()


def copy_text_back():
    open_mn()
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    mn_quick_edit()
    open_terminal()
    pyautogui.sleep(0.2)
    pyautogui.press("enter")


def remove_leading_number(input_string):
    output_string = re.sub("^\d+\.?\d*\s", "", input_string)
    return output_string


def special_input(input_content, context, study):
    global prompt_chinese
    global is_next
    if len(input_content.strip()) == 0:  # 若内容为空, 直接跳转到下一个
        move_next()
        is_next = True
        return True
    elif input_content.endswith("p"):  # 翻播放内容
        play_sound_and_copy()
        return True
    elif input_content.endswith("s"):  # 翻译
        temp_context = remove_leading_number(context)
        translate_context(temp_context)
        return True
    elif input_content.endswith("j"):  # 跳到下下个, 用于跳过不用总结的内容如标题
        jump()
        return True
    elif input_content.endswith("w"):  # 直接使用terminal进行提问
        wen(input_content)
        return True
    elif input_content.endswith("r") or input_content.endswith("u"):  # 重新总结, reverse
        undo()
        return True
    elif input_content.endswith("e"):  # 移动到上一段
        move_prev()
        return True
    elif input_content.endswith("a"):  # 直接问这里的内容
        if len(input_content) == 1:
            ask(context)
        else:
            # 对当前上下文进行提问
            ask_context(context, input_content[:-1])

        return True
    elif input_content.endswith("f"):  # 把gpt回答的最后一点粘贴回去
        if study:
            mn_past_answer3()
            return True
        else:
            print("非复习模式, f键用来设置标题")
            t_set_title(input_content)
        return True
    elif input_content.endswith("d"):  # 设置标题
        incre_statistics()
        t_set_title(input_content)
        is_next = True
        return True
    elif input_content.endswith("x"):  # 把翻译复制到mn
        copy_translation()
        return True
    elif input_content.endswith("k"):  # 选中当前
        select_current()
        return True
    elif input_content.endswith("g"):  # 把input设为标题，再把gpt回答复制到mn
        mn_title = "ID: " + remove_trailing_letter(input_content)
        mn_new_item(mn_title)
        press_keys("tab")
        mn_past_answer()
        return True
    elif input_content.endswith("q"):  # 添加评论
        mn_comment = remove_trailing_letter(input_content)
        pyperclip.copy(mn_comment)
        pyautogui.sleep(0.1)
        open_mn()
        press_keys('command', 'v')
        print("添加评论成功")
        pyautogui.sleep(0.1)
        open_terminal()
        pyautogui.press("enter")
        print_seperator()
        return True
    elif input_content.endswith("v"):  # 把gpt回答复制到mn
        mn_past_answer()
        return True
    elif input_content.endswith("c"):  # 把gpt回答复制到mn
        mn_past_answer3()
        return True
    else:
        return False


def extract_text(article):
    # 找到4以后的
    last_instance = article.rfind('\n4')
    # If "4:" is not found, return an empty string
    if last_instance == -1:
        return ''

    # text_after4 = article[:last_instance]

    # 以前是rfind(':'), 有bug再回来改
    last_instance_bias = article[last_instance:].find(':')
    if last_instance_bias != -1:  # 存在英文冒号
        last_instance += last_instance_bias

    last_instance_bias = article[last_instance:].find('：')
    if last_instance_bias != -1:  # 存在中文冒号
        last_instance += last_instance_bias

    text_after_last_instance = article[last_instance + 1:]
    # Find the position of the first "}" character
    end_position = text_after_last_instance.find('}')
    # If "}" is not found, return all text after the last "4:"
    if end_position == -1:
        return text_after_last_instance.strip()
    # Return the text between the last "3:" and the first "}" after it
    return text_after_last_instance[:end_position].strip()


def translate_context(context):
    text_list = text_to_list(context)
    pyperclip.copy(text_list)
    pyautogui.sleep(0.2)
    open_translate()
    press_keys('command', 'a')
    pyautogui.sleep(0.2)
    press_keys('command', 'v')
    print("已翻译")
    print_seperator()
    open_terminal()
    pyautogui.press("enter")
    pyautogui.sleep(0.1)
    pyautogui.moveTo(3769, 867)


def auto_translate(context):
    # text_list = text_to_list(context)
    pyperclip.copy(context)
    pyautogui.sleep(0.2)
    open_translate()
    press_keys('command', 'a')
    pyautogui.sleep(0.2)
    press_keys('command', 'v')
    print("已翻译")
    print_seperator()
    open_terminal()
    pyautogui.sleep(0.1)
    pyautogui.moveTo(3333, 760)
    pyautogui.scroll(15)


def mn_new_item(mn_title):
    pyperclip.copy(mn_title)
    open_mn()
    pyautogui.sleep(0.1)
    pyautogui.press("enter")
    pyautogui.sleep(0.1)
    press_keys('command', 'v')
    pyautogui.sleep(0.1)
    pyautogui.press("esc")
    pyautogui.sleep(0.1)
    print(f'已在mn创建title:\n  "{mn_title}"')


def not_mn(s):
    pattern = r'\n\n'
    matches = re.findall(pattern, s)
    return len(matches) == 0


def contains_chinese(s):
    if re.search(r'[\u4e00-\u9fff]+', s):
        return True
    else:
        return False


# def re_get_content(note):  # 获取内容
#     # if '\n\n' not in clipboard_content:  # 检测是否包含两个换行，不包含说明不是margin note的笔记，则直接复制
#     if not_mn(clipboard_content):  # 检测是否包含两个换行，不包含说明不是margin note的笔记，则直接复制
#         return note
#     else:
#         # 遍历直到找到不包含中文的部分，也就是英文原文
#         contents = note.split("\n\n")
#         for ct in contents:
#             if contains_chinese(ct):
#                 continue
#             else:
#                 return ct
#
#         return "all contains chinese"

def extract_heuristics(text):
    # 使用"<heuristics>"和"<heuristics>"字符串的索引来定位要提取的文本部分
    start = text.find("<heuristics>")
    # 找不到"<heuristics>"标签时返回空字符串
    if start == -1:
        return ""
    # 将开始索引移动到"<heuristics>"标签后
    start += len("<heuristics>")
    # 返回从"<heuristics>"标签后到文本末尾的部分
    return text[start:].strip()


def re_get_content(note):  # 获取内容
    chinese_sum = ""  # 中文的总结
    english_ct = extract_heuristics(note)

    if note:
        contents = note.split("\n\n")
    else:
        return "为空", "为空"

    for ct in contents:
        if contains_chinese(ct):
            chinese_sum += (ct + "\n\n  ")

    return chinese_sum, english_ct


def mn_quick_edit():
    pyautogui.hotkey('command', 'enter')
    pyautogui.sleep(0.5)
    pyautogui.press("esc")


def copy_next():
    pyautogui.press("down")
    pyautogui.sleep(0.2)
    pyautogui.hotkey('command', 'c')
    pyautogui.sleep(0.2)
    pyautogui.press("up")  # 因为复习一般用不到仔细看，所以不up


def process_input(input_type):
    # 使用while循环来重新输入
    while True:
        text = input(f"请输入{input_type}: \n  ")
        if text.endswith("p"):  # 用于停止播放语音
            click_sound()
            print("已暂停播放")
        elif not text.endswith('l'):
            return text
        else:  # 重置
            temp = text[:-5]
            pyperclip.copy(temp)  # 回退3个字符
            print("已重置，请重新输入 \n")


# 把gpt的回答粘贴到marginnote
def mn_past_answer():
    if gpt_mode:
        gpt_copy()
    else:
        # 复制gpt的回答
        y = get_max_y()
        my_tool.moveto_and_click(1234, y, delay=0.1)
        pyautogui.dragTo(1234, 955, button='left', duration=0.2)
        press_keys('command', 'c')

    pyautogui.sleep(0.1)
    gpt_answer = "---gpt---\n" + pyperclip.paste()
    pyperclip.copy(gpt_answer)
    open_mn()
    pyautogui.sleep(0.1)
    press_keys('command', 'v')
    pyautogui.sleep(0.1)
    pyautogui.hotkey('command', 'c')
    pyautogui.sleep(0.1)
    open_terminal()
    pyautogui.press("enter")
    print("已将gpt回答粘贴到mn")
    print_seperator()


# 把gpt的回答的3:后的内容粘贴到mn
def mn_past_answer3():
    if gpt_mode:
        gpt_copy()
    else:
        # 复制gpt的回答
        y = get_max_y()
        my_tool.moveto_and_click(1234, y, delay=0.1)
        pyautogui.dragTo(1234, 955, button='left', duration=0.2)
        press_keys('command', 'c')

    temp_text = pyperclip.paste()
    answer3 = extract_text(temp_text)
    pyautogui.sleep(0.1)
    gpt_answer = "gpt总结/补充:\n  " + answer3
    pyperclip.copy(gpt_answer)
    open_mn()
    pyautogui.sleep(0.1)
    press_keys('command', 'v')
    pyautogui.sleep(0.1)
    pyautogui.hotkey('command', 'c')
    pyautogui.sleep(0.1)
    open_terminal()
    pyautogui.press("enter")
    print("已将gpt回答3粘贴到mn")
    print_seperator()


def play_sound():
    global is_next
    past_and_play()
    is_next = False
    open_terminal()


def click_sound():
    pyautogui.moveTo(3300, 940)
    pyautogui.sleep(0.2)
    pyautogui.click()
    pyautogui.click()
    pyautogui.sleep(0.2)
    open_terminal()


def play_sound_and_copy():
    past_and_play()
    content = ch_sum + "\n\n" + context_text
    pyperclip.copy(content)
    open_terminal()
    pyautogui.press("enter")
    print("已播放声音")
    print_seperator()


def past_and_play():
    pyperclip.copy(ch_sum)
    pyautogui.sleep(0.2)
    pyautogui.moveTo(3300, 600)
    pyautogui.sleep(0.1)
    pyautogui.click()
    pyautogui.click()
    press_keys('command', 'a')
    pyautogui.sleep(0.2)
    press_keys('command', 'v')
    pyautogui.sleep(0.2)
    pyautogui.moveTo(3300, 940)
    pyautogui.sleep(0.2)
    pyautogui.click()


if __name__ == '__main__':
    input_text = ""  # 笔记
    last_input = ""  # 记录最后的输入
    understanding_to_check = ""  # 用来问gpt的问题
    input_title = ""  # 输入的标题
    ch_sum = ""  # 保存中文翻译和总结

    study_mode = True  # 学习模式开启，则自动添加题目和评论
    # study_mode = False  # 注释掉这句话开启学习模式
    first_run = True
    gpt_mode = True
    # need_title = True
    not_ask = False

    # play_voice = True
    play_voice = False

    is_next = True

    prompt_chinese = "以下所有问题, 请你用中文回答, 明白了吗？"

    if study_mode:
        need_title = True
    else:
        need_title = False

    if study_mode:
        print("当前为 学习 模式")
    else:
        print("复习中")

    while True:
        count = read_statistics()  # Load statistics
        my_tool.declare_time(count)

        # 记录用户第1次在terminal的输入A
        if first_run:
            input("复制原文后回车：\n")
            first_run = False
        else:
            input()

        clipboard_content = pyperclip.paste()
        ch_sum, context_text = re_get_content(clipboard_content)

        print(f"当前段落: \n  {context_text[:64]} ...\n")
        print(f"\033[1;35;40m翻译 & gpt总结: \n\n  {ch_sum} \033[0m")

        auto_translate(context_text)

        # pyperclip.copy(input_text)
        pyperclip.copy(last_input)

        input_text = process_input("总结")

        # if special_input(input_text, context_text, last_input, study_mode):
        if special_input(input_text, context_text, study_mode):
            continue

        if input_text.endswith("."):
            input_text = input_title[:-1]  # 删掉.号
            print("已经移除了总结末尾的'.'号")

        last_input = input_text  # 保存上次的input用于设定标题等

        if study_mode:  # 学习模式需要添加title
            input_title = process_input("标题")
            if input_title.endswith("."):
                input_title = input_title[:-1]  # 删掉.号
                print("已经移除了标题末尾的'.'号")
            elif input_title.endswith("k"):  # crash重来
                copy_text_back()
                print("重来当前的内容")
                print_seperator()
                continue
            elif input_title.endswith("d"):  # 只编辑mn, 不询问gpt
                input_title = input_title[:-1]
                print("不询问gpt, 只编辑mn")
                is_next = True
                not_ask = True

        title_is_null = (len(input_title.strip()) == 0)
        if need_title and not title_is_null:
            understanding_to_check = "标题: " + input_title + "\n内容: " + input_text
        else:
            understanding_to_check = input_text

        # 生成给gpt的最终问题
        content_to_ask = generate_question(context_text, understanding_to_check)

        # 粘贴C
        if not_ask:
            not_ask = False
        else:
            input_to_gpt(content_to_ask)

        # 把总结粘贴到笔记
        open_mn()
        pyautogui.sleep(0.3)

        # 学习模式, 则添加评论和标题
        if study_mode:
            my_summary = "ms: " + input_text  # my summary
            pyperclip.copy(my_summary)  # 把B复制到剪贴板
            pyautogui.sleep(0.2)
            pyautogui.hotkey('command', 'v')
            pyautogui.sleep(0.3)

            # 生成标题, 用if是因为暂时觉得比较麻烦
            if need_title:
                # 生成标题
                if len(input_title.strip()) == 0:  # 标题为空, 则不添加标题
                    input_title = input_text + ">"  # 加入>符号可以防止生成字典
                    print("标题为空，使用总结作为标题")
                else:
                    input_title = input_title + "> " + input_text

                pyperclip.copy(input_title)
                pyautogui.sleep(0.2)
                set_title()

        pyperclip.copy(context_text)

        # 使标题总是可见，防止看不到一整条笔记
        # mn_quick_edit()

        # 切回terminal并缓冲下一条
        pyautogui.sleep(0.2)
        open_terminal()
        pyautogui.press("enter")  # 有了这个enter就可以跳过复制内容的步骤

        incre_statistics()

        print_seperator()
