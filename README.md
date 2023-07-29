# User Manual for Process Mining Assistant 1.1
PM Assistant is structured based on this [repository](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/main). Authorization has been obtained from the author of Mr. Ranedeer.

---

## Table of content
- [Why PM Assistant](#why-pm-assistant)
- [Quick Start Guide](#quick-start-guide)
- [Core Commands](#core-commands)
  - [Generate solution for a case](#1-generate-solution-for-a-case)
  - [Use Heuristics to solve a case](#2-use-heuristics-to-solve-a-case)
  - [Implements the selected solution](#3-implements-the-selected-solution-identified-by-its-number)
  - [Predicts the potential outcome of a solution](#4-predicts-the-potential-outcome-of-a-solution)
- [Other Commands](#other-commands)
  - [Generate some questions](#5-generate-some-questions)
  - [Ask a question](#6-ask-a-question)
  - [Manage context](#7-manage-context)
  - [Edit configurations](#8edit-configurations)
  - [Change language](#9-change-language)
- [Feedback](#feedback)
- [Function Display](#function-display)

---
![begin](data/begin1_1.png)
![analyze](data/analyze1_1.png)
---
## Why Process Mining Assistant

Process Mining Assistant is designed to assist the redesign part of process mining.

It could empower you in several ways:

1. **Operational Support in Process Mining:** For specified improvement opportunities, the Assistant can provide operational support for the software you use, helping you to discover them using the software.

2. **Solution Generation:** For improvement opportunities identified in process mining, PM Assistant allows you to rapidly generate multiple solutions.

3. **Actionable Steps:** Based on these solutions, the tool is capable of generating concrete implementation steps.

4. **Cost-Benefit Analysis and Visualization:** The Assistant can calculate the estimated costs and potential returns for a detailed implementation plan, and use visualization to help you understand the results.

An exciting discovery we've made is that PM Assistant is not only capable of supporting the redesigning needs in process mining, but it can also provide practical solutions, implementation steps, and thoughtful trade-offs for everyday problems you might encounter in life. PM Assistant - a tool designed for process mining, but its utility extends well beyond!

### Example from life:

![daily_example](data/daily_example.png)
---

## Quick Start Guide

1. Click **[this link](https://chat.openai.com/share/daa2ec0e-c650-412f-aa25-e07b74ac4921)** (**MUST HAVE CHATGPT PLUS**)(Deutsch Version click **[hier](https://chat.openai.com/share/eb717e12-0d0f-4765-87d2-9fbe5fd869b3)**)
2. Press the "Continue this conversation" button
3. Use /choose + [Number] to get operational support to mine specified opportunity, or /solve + [A Case] to start analysing.

## 5-minute Video-Tutorial in Youtube: https://youtu.be/4IoIFEKXiGs 

Click [here](https://chat.openai.com/share/b7d99083-add1-4f61-b61d-c2678b53bfe9) to see  a detailed example of how to use PM Assistant ([Deutsch Beispiel hier](https://chat.openai.com/share/aee36a56-4bf2-4c72-abe6-6cc6fc21b9d8)). Please note that the dialogue starts in the middle of the page.

Not have chatGPT-Plus? Never mind, click [here](https://github.com/finsterniz/pm_assist/blob/main/prompt_set.md) to run PM assistant without it. 

---
## Core-Commands

### 1. Operational Support in Process Mining
**/choose + [Number of Improvement Opportunity]**

You can also use /cho

Example: let GPT give you the guidance to find 5.1 Rework
```
/choose 5.1
```

### 2. Generate solution for a case
**/solve + [Case]**

Offers solutions for a specific case.

You can also use /sol

Example:
```bash
/solve
In the loan application process, after the client submits their loan application, the clerk performs three checks in a random order: identity check, verification, and creditworthiness check. If any of these checks fail, the application is rejected. However, since there is no predefined order for conducting the checks, it leads to an issue of overprocessing.
```

---
### 3. Use Heuristics to solve a case
**/heuristic + [List of Heuristics]**

Utilizes lesser-used GPT heuristics to generate solutions from alternate viewpoints.

You can also use /heu

Example and set of heuristics:

https://raw.githubusercontent.com/boiltaimn/pm_assist/main/heuristics.txt

---
### 4. Implements the selected solution, identified by its number.
**/implement + [number]**

You can also use /imp

Example: implement the second solution
```bash
/implement 2
```

---
### 5. Cost-Benefit Analysis and Visualization
**/analyze + [some context]**

You can also use /ana

Example 1: Analyse without providing initial context
```bash
/analyze
```
Example 2: Analyse with some initial context
```bash
/analyze  The company has 200 employees, and I estimate that this solution involves 20 of them. Their average salary is 3,500 euros per month.
```
## Other commands

### 5. Generate some questions
**/suggestion**

Invite GPT to suggest next command or questions based on the current conversation.

You can also use /sug

Example:
```bash
/suggestion
```

---
### 6. Ask a question
**/question + [...]**

Presents a question. Questions can also be asked without using the command, but it's recommended to use the command as GPT might occasionally lose its personality without it.

You can also use /que

Example:
```bash
/question How about adding missing system functionalities for this case?
```

---
### 7. Manage context 
**/goto + [number i]**

Each round of conversation gets assigned a number. Using this command, you can return to a specific conversation and continue from there. This command enables GPT to forget the conversation that happened after the i-th conversation.

Example: # Go to the third conversation and implement the first solution
```bash
/goto 3 
/imp 1
```

---
### 8.Edit configurations
**/config + [configuration]**

Used to set configurations.

Example: 
```bash
/config Tone Style = Humorous
```
---
### 9. Change language
**/language + [your language]**

Used to switch languages.d

Tip: PM Assistant performs best when using English.

Example: 
```bash
/language Deutsch
```
---

## Feedback
I would be very grateful if you could help me fill out the survey:

**[Questionnaire for LinkedIn](https://forms.gle/Jjv9kkHqVhyHmr559)**

---
## Functions Display
### /choose Function
![solve](data/support1_1.png)
### /solve Function
![solve](data/solve1_1.png)
### /heuristic Function
![solve](data/heuristic.png)
### /implement Function
![implement](data/implement.png)
### /analyze Function
![analyze](data/analyze1_1.png)
### Guide map Function
![map](data/map1_1.png)
