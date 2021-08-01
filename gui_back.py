# -*- coding: utf-8 -*-
# @Time : 2021-08-01 14:09
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : gui_back.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import gui_front
import question
import os
import usr.usr as usr
import pandas as pd

userInfo = dict()
userDirectory = "./usr/"
user = None


class MyWindow(QMainWindow, gui_front.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None

    def buildQuestions(self, typ: str, difficulty: int) -> dict:
        res = dict()
        if typ == "ChoiceOnly":
            data = pd.read_csv("./bank/chooseQuestions.csv")
            # print(data.shape[0])
            for i in range(data.shape[0]):
                res[str(i+1)] = question.ChoiceQuestion(statement=data.iloc[i, 1], correct_answer=data.iloc[i, 2])
                print(data.iloc[i, 1])
        return res

    def load_questions(self, questions: dict) -> None:
        # self.loadedQuestions = {"1": question.ChoiceQuestion(statement="how are you?", correct_answer=set("D")),
        #              "2": question.JudgmentQuestion(statement="hahahhahhhah", correct_answer="False"),
        #              "3": question.ShortAnswerQuestion(statement="??????", standard_answer="yes")}
        self.loadedQuestions = questions
        self.questionList.clear()
        for num in self.loadedQuestions.keys():
            item = QtWidgets.QListWidgetItem()
            item.setText(num)
            self.questionList.addItem(item)

    def changeQuestion(self):
        if not self.loadedQuestions[str(self.questionList.currentItem().text())]:
            self.loginfo.print("This question doesn't exist!")
            return
        curQuestion = self.loadedQuestions[str(self.questionList.currentItem().text())]
        self.textBrowser.setText(curQuestion.show())
        type_of_question = type(curQuestion)
        if type_of_question == question.ChoiceQuestion:
            self.choiceQuestion.show()
            self.judgeQuestion.hide()
            self.answerQuestion.hide()
        elif type_of_question == question.JudgmentQuestion:
            self.choiceQuestion.hide()
            self.judgeQuestion.show()
            self.answerQuestion.hide()
        elif type_of_question == question.ShortAnswerQuestion:
            self.choiceQuestion.hide()
            self.judgeQuestion.hide()
            self.answerQuestion.show()
        else:
            self.loginfo.print("Wrong question type when changing current Question")


class MyLogin(gui_front.Ui_login):
    def __init__(self, parent=None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None

    def accept_logInfo(self):
        global user
        if not self.userNameLine.text() in userInfo.keys():
            print("username doesn't exist!")
            self.userNameLine.setText("")
            self.passwordLine.setText("")
            return False
        if not userInfo[self.userNameLine.text()].password == self.passwordLine.text():
            print(self.passwordLine.text())
            print("password not correct!")
            self.passwordLine.setText("")
            return False
        user = userInfo[self.userNameLine.text()]
        self.accept()

    def loginExit(self):
        sys.exit()


def loadUserInformation():
    for f_name in os.listdir(userDirectory):
        if f_name != "__pycache__" and f_name != "usr.py":
            userInfo[f_name.split(".")[0]] = usr.UserInformation(userDirectory + f_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myLoginWin = MyLogin()
    myWin.show()
    # myWin.load_questions({})
    loadUserInformation()
    print(userInfo)
    # myLoginWin.show()
    print(myWin.buildQuestions(typ="ChoiceOnly", difficulty=0))
    myWin.load_questions(myWin.buildQuestions(typ="ChoiceOnly", difficulty=0))
    sys.exit(app.exec_())
