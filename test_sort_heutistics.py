#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 25.06.23 12:54 am
# @Author  : Hao
# @File    : test_sort_heutistics.py
text = """
1.1 Control Relocation-8
1.2 Contact reduction-2
1.3 Integration-3
2.2 Task Elimination-13
2.3 Order-based work-1
2.5 Task composition or decomposition-3
3.2 Knock-out-3
3.3 Parallelism-1
4.1.2 Flexible Assignment-4
4.1.3 Centralization-23
4.1.4 Split responsibilities-2
4.1.5 Customer Teams-3
4.1.6 Numerical Involvement-2
4.1.7 Case Manager-6
4.2 Extra Resources-17
4.2.1.1 Specialist or 4.2.1.2 Generalist-53
4.2.2 Empower-2
4.2.4 Triage-7
4.3.1 Resequencing-6
4.3.4 Exception-1
4.4.1 Order assignment-2
4.5.1 Control Addition-32
4.5.2 Buffering-5
4.6.1 Task Automation-56
4.6.2 Integral Technology-96
4.7.1 Trusted Party-5
4.7.2 Outsourcing-2
4.7.3 Interfacing-22
8.1 Workload Management-7
8.2 Process Standardization-6
8.3 Continuous Improvement-12
8.4 Advocacy Management-2
8.6 Cross-functional Collaboration-3

"""

lines = text.strip().split("\n")  # splits the input text into lines
lines.sort(key=lambda line: int(line.rsplit("-", 1)[1]))

for line in lines:
    print(line)
