# -*- coding: utf-8 -*-
# @Time : 2021-08-01 23:01
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : read.py
# @Software: PyCharm
import re
import question
import pandas as pd

re.compile("A (.?)B")
with open("choose.txt", "r", encoding='utf-8') as f:
    a = f.readline()
    a = f.readline()
    statements = []
    string = ""
    while a != "":
        if a[0] in "1234567890":
            statements.append(string)
            string = a
        else:
            string += a
        a = f.readline()
    statements.append(string)
    answer = list("CCACDBBBDBACDCADAACCBBAABCABCAACCDAAABCADADCCACDCA")
    a = pd.Series(statements[1:])
    an = pd.Series(answer)
    questions = pd.DataFrame({'quesion': a, 'answer': an})
    print(questions)
    print(questions.iloc[2, 0])
    questions.to_csv("./bank/chooseQuestions.csv")
