# -*- coding: utf-8 -*-
# @Time : 2021-08-01 23:01
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : read.py
# @Software: PyCharm
import pandas as pd


def judge_read():
    with open("judge.txt", "r", encoding='utf-8') as f:
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
        ques = pd.Series(statements[1:])
        print(ques[2])
    with open("answer.txt", "r", encoding='utf-8') as f:
        a = f.readline()
        answers = []
        explanations = []
        while a != "":
            words = a.split(" ")
            if len(words) == 1:
                answer = True if words[0] == 'y' else False
                explanation = ""
            else:
                answer = words[0]
                explanation = words[1]
            answers.append(answer)
            explanations.append(explanation)
            a = f.readline()
        questions = pd.DataFrame({'quesion': ques, "answer": answers, "explanation": explanations})
        print(questions.iloc[2, 1])
        # questions = pd.DataFrame({'quesion': a, 'answer': an})
        # print(questions)
        # print(questions.iloc[2, 0])
        questions.to_csv("./bank/judgeQuestions.csv")


def readAnswer():
    with open("answerQuestions.txt", "r", encoding="utf-8") as f:
        a = f.readline()
        questions = []
        answers = []
        answer = ""
        while a != "":
            if len(a) > 2 and a[0] in "1234567890" and (a[2] == " " or a[2] == "."):
                if answer != "":
                    print(answer)
                    answers.append(answer)
                    answer = ""
                questions.append(a)
            else:
                answer += a
            a = f.readline()
        print(answer)
        answers.append(answer)
        print(len(questions))
        print(len(answers))
        questions = pd.DataFrame({'quesion': questions, "answer": answers})
        questions.to_csv("./bank/answerQuestions.csv")

readAnswer()