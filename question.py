# -*- coding: utf-8 -*-
# @Time : 2021-07-31 19:34
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : question.py
# @Software: PyCharm
class Question(object):
    def __init__(self, statement: str):
        self.statement = statement

    def show(self):
        return "None"

    def check_correctness(self, answer: str) -> bool:
        return True


class ChoiceQuestion(Question):
    def __init__(self, statement: str, correct_answer: set):
        super().__init__(statement)
        self.correct_answer = correct_answer

    def show(self):
        return self.statement

    def check_correctness(self, answer: set) -> bool:
        if answer == self.correct_answer:
            return True
        else:
            return False

    def answer(self):
        return self.correct_answer


class JudgmentQuestion(Question):
    def __init__(self, statement: str, correct_answer: str):
        super().__init__(statement)
        self.correct_answer = correct_answer

    def show(self):
        return self.statement

    def check_correctness(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
        else:
            return False

    def answer(self):
        if self.correct_answer == "n":
            return "False"
        else:
            return "True"


class ShortAnswerQuestion(Question):
    def __init__(self, statement: str, standard_answer: str):
        super().__init__(statement)
        self.correct_answer = standard_answer

    def show(self):
        return self.statement

    def check_correctness(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
        else:
            return False

    def answer(self):
        return self.correct_answer
