#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 20.06.23 1:16 pm
# @Author  : Hao
# @File    : test_re_find_outputredesign.py
text = """
In an airport transportation scheduling process, forecasted arrivals and departures schedule was produced by means of several tools including the franchise reservation system and the sales system, using historical data from prior weeks and months, and input from various department heads. The actual occupancy often exceeded the forecast because of the failure of the sales system to accurately report actual group rooms expected. Hence, the system produced incorrect results - expected schedules with low accuracy.

<Output Redesign>: 

1. System Upgrade: Consider upgrading the current sales system to a more reliable and accurate one. This can ensure the accurate reporting of actual group rooms expected, thereby increasing the accuracy of the forecast.

2. Integrative Forecasting System: Develop or implement an integrative forecasting system that pulls data from all relevant tools and departments. This system should be designed to handle variations and inconsistencies in data, thereby improving forecast accuracy.

3. Machine Learning Algorithms: Employ advanced machine learning algorithms for predicting arrivals and departures. These algorithms can learn from past inaccuracies and improve future predictions.

4. Real-time Updates: Implement a system that allows for real-time updates of occupancy data. This can help in adjusting the forecast dynamically as the actual data changes.

5. Training: Ensure that the department heads and staff members who input data into the system are properly trained. This can help in reducing errors and improving the accuracy of the forecast.

6. Regular Auditing: Conduct regular audits of the forecasting process to identify and rectify any systematic errors or inefficiencies.
------------------

在一个机场运输调度过程中，预测的到达和离开时间表是通过几个工具产生的，包括特许预订系统和销售系统，使用前几周和几个月的历史数据，以及各部门负责人的输入。由于销售系统未能准确报告预期的实际团体房间，实际入住率经常超过预测。因此，该系统产生了不正确的结果--准确率低的预期时间表。

<输出重新设计>： 

1. 系统升级： 考虑将目前的销售系统升级为更可靠和准确的系统。这可以确保准确报告实际组室的预期，从而提高预测的准确性。

2. 2.综合预测系统： 开发或实施一个综合预测系统，从所有相关的工具和部门提取数据。这个系统应该被设计成能够处理数据的变化和不一致，从而提高预测的准确性。

3. 3.机器学习算法： 采用先进的机器学习算法来预测到达和离开的情况。这些算法可以从过去的不准确中学习，改善未来的预测。

4. 4. 实时更新： 实施一个允许实时更新入住率数据的系统。这可以帮助在实际数据变化时动态调整预测。

5. 5.培训： 确保将数据输入系统的部门主管和工作人员都经过适当的培训。这可以帮助减少错误，提高预测的准确性。

6. 定期审计： 对预测过程进行定期审计，以确定并纠正任何系统性错误或低效率。
<Output>
<Output Redesign>: 

1. System Upgrade: Consider upgrading the current sales system to a more reliable and accurate one. This can ensure the accurate reporting of actual group rooms expected, thereby increasing the accuracy of the forecast.

2. Integrative Forecasting System: Develop or implement an integrative forecasting system that pulls data from all relevant tools and departments. This system should be designed to handle variations and inconsistencies in data, thereby improving forecast accuracy.

3. Machine Learning Algorithms: Employ advanced machine learning algorithms for predicting arrivals and departures. These algorithms can learn from past inaccuracies and improve future predictions.

4. Real-time Updates: Implement a system that allows for real-time updates of occupancy data. This can help in adjusting the forecast dynamically as the actual data changes.

5. Training: Ensure that the department heads and staff members who input data into the system are properly trained. This can help in reducing errors and improving the accuracy of the forecast.

6. Regular Auditing: Conduct regular audits of the forecasting process to identify and rectify any systematic errors or inefficiencies.
"""

import re

def extract_redesign(text):
    pattern = r'(<Output Redesign>:\s*\n.*?)(?=\n---)'
    result = re.search(pattern, text, re.DOTALL)
    return result.group(1) if result else None

ziel = extract_redesign(text)

print(ziel)