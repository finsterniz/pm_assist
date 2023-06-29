# User Manual for PM Assistant 1.0
PM Assistant is structured based on the repository: https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/main. Authorization has been obtained from the author of Mr. Ranedeer.

## Quick Start Guide

1. Click [this link](https://chat.openai.com/share/76f03aad-d9d2-45a5-88d7-3387366572f6) (**MUST HAVE CHATGPT PLUS**)(Deutsch Version click [hier](https://chat.openai.com/share/76f03aad-d9d2-45a5-88d7-3387366572f6))
2. Press the "Continue this conversation" button
3. Configure your preferences
4. Start analysing

## Commands
---
###Solve a case
**/solve [Case]**: Offers solutions for a specific case.

You can also use /sol

Example:
```bash
/solve
In the loan application process, after the client submits their loan application, the clerk performs three checks in a random order: identity check, verification, and creditworthiness check. If any of these checks fail, the application is rejected. However, since there is no predefined order for conducting the checks, it leads to an issue of overprocessing.
```

---
**/heuristic <List of Heuristics>**: Utilizes lesser-used GPT heuristics to generate solutions from alternate viewpoints.

You can also use /heu

Example:
https://raw.githubusercontent.com/boiltaimn/pma_data/main/test_txt.txt


---
**/implement <number>**: Implements the selected solution, identified by its number.

You can also use /imp

Example:
```bash
/implement 2
```

---
**/predict <number or solution>**: Predicts the potential outcome of a solution.

You can also use /pre

Example:
```bash
/predict # Predict the outcome of the current solution
```
```bash
/predict 2 # Predict the solution with number 2
```
```bash
/predict Process Standardization # Predict the result of "Process Standardization"
```

---
**/suggestion**: Invites GPT to suggest questions based on the current conversation.

You can also use /sug

Example:
```bash
/suggestion
```

---
**/question <question>**: Presents a question. Questions can also be asked without using the command, but it's recommended to use the command as GPT might occasionally lose its personality without it.

You can also use /que

Example:
```bash
/question How about adding missing system functionalities for this case?
```

---
**/goto <number i>**: Each round of conversation gets assigned a number. Using this command, you can return to a specific conversation and continue from there. This command enables GPT to forget the conversation that happened after the i-th conversation.

Example: # Go to the third conversation and implement the first solution
```bash
/goto 3 
/imp 1
```

---
**/config <configuration>**: Used to set configurations.

Example: 
```bash
/config Tone Style = Humorous
```

**/language**: Used to switch languages.

Tip: PM Assistant performs best when using English.

Example: 
```bash
/language Deutsch
```
