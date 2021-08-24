# -*- coding: utf-8 -*-
# @Time : 2021-08-01 14:09
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : gui_back.py
# @Software: PyCharm
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import gui_front
import question
import os
import usr.usr as usr
import pandas as pd
import numpy as np
import random
import draw

userInfo = dict()
userDirectory = "./usr/"
user = None


class MyWindow(QMainWindow, gui_front.Ui_MainWindow):
    chooseNum = 50
    judgeNum = 50
    answerNum = 10

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None
        self.questionWhole = None
        self.answerDict = dict()
        self.answerV = False

        # drawGraph: binding QGraphView with draw.Figure_Bar
        width = self.stateGraph.width()
        height = self.stateGraph.height()
        self.myImage = draw.Figure_Bar(width / 90, height / 220)
        self.myGraphyScene = QGraphicsScene()
        self.stateGraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stateGraph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene.addWidget(self.myImage)
        self.stateGraph.setScene(self.myGraphyScene)

    # buildQuestions from dataBase to make `loadedQuestions` `questionWhole` used later
    def buildQuestions(self, typ: dict, difficulty: int) -> dict:
        self.loadedQuestions = None
        self.questionWhole = None
        self.answerDict = dict()
        self.answerV = False
        global user
        user = userInfo[self.username.text()]
        progresses = user.progress

        # load question and userInformation from .csv
        chooseProcess = np.array(progresses[progresses["type"] == "choose"]).tolist()
        judgeProcess = np.array(progresses[progresses["type"] == "judge"]).tolist()
        answerProcess = np.array(progresses[progresses["type"] == "answer"]).tolist()
        chooseData = pd.read_csv("./bank/chooseQuestions.csv")
        chooseData = np.array(chooseData).tolist()
        chooseData_u = []
        for i in range(len(chooseData)):
            chooseData_u.append(chooseProcess[i] + chooseData[i])
        judgeData = pd.read_csv("./bank/judgeQuestions.csv")
        judgeData = np.array(judgeData).tolist()
        judgeData_u = []
        for i in range(len(judgeData)):
            judgeData_u.append(judgeProcess[i] + judgeData[i])
        answerData = pd.read_csv("./bank/answerQuestions.csv")
        answerData = np.array(answerData).tolist()
        answerData_u = []
        for i in range(len(answerData)):
            answerData_u.append(answerProcess[i] + answerData[i])
        self.Data_u = answerData_u
        questions = sorted(answerData_u, key=lambda x: x[3] - x[2])[: typ["answer"]] + \
                    sorted(judgeData_u, key=lambda x: x[3] - x[2])[: typ["judge"]] + \
                    sorted(chooseData_u, key=lambda x: x[3] - x[2])[: typ["choose"]]
        random.shuffle(questions)
        self.questionWhole = questions
        res = dict()
        for i in range(len(questions)):
            if questions[i][1] == "choose":
                res[str(i + 1)] = question.ChoiceQuestion(statement=questions[i][5], correct_answer=questions[i][6])
            elif questions[i][1] == "judge":
                res[str(i + 1)] = question.JudgmentQuestion(statement=questions[i][5], correct_answer=questions[i][6])
            elif questions[i][1] == "answer":
                res[str(i + 1)] = question.ShortAnswerQuestion(statement=questions[i][5],
                                                               standard_answer=questions[i][6])
            else:
                self.loginfo("loadWrongType answer!")
        self.load_questions(res)
        return res

    def load_questions(self, questions: dict) -> None:
        self.loadedQuestions = questions
        self.questionList.clear()
        for num in self.loadedQuestions.keys():
            item = QtWidgets.QListWidgetItem()
            item.setText(num + " *")
            self.questionList.addItem(item)

    def plotQuestionInfo(self, correctTimes: int, AnswerTimes: int):
        self.myImage.ShowImage1(correctTimes, AnswerTimes)
        return

    # each time the Question list changed, this function will be called due to binding
    def changeQuestion(self):
        answered = False
        if len(self.questionList.currentItem().text().split(" ")) == 1 \
                or self.questionList.currentItem().text().split(" ")[1] != "*":
            answered = True
        if not self.loadedQuestions[str(self.questionList.currentItem().text().split(" ")[0])]:
            self.loginfo.print("This question doesn't exist!")
            return
        curQuestion = self.loadedQuestions[str(self.questionList.currentItem().text().split(" ")[0])]
        self.textBrowser.setText(curQuestion.show()[2:] + ("\n" + curQuestion.answer() if self.answerV else ""))
        type_of_question = type(curQuestion)
        if type_of_question == question.ChoiceQuestion:
            self.choiceE.setChecked(True)
            self.choiceQuestion.show()
            self.judgeQuestion.hide()
            self.answerQuestion.hide()
            if answered:
                qNum = str(self.questionList.currentItem().text().split(" ")[0])
                if self.answerDict[qNum] == "A":
                    self.choiceA.setChecked(True)
                elif self.answerDict[qNum] == "B":
                    self.choiceB.setChecked(True)
                elif self.answerDict[qNum] == "C":
                    self.choiceC.setChecked(True)
                elif self.answerDict[qNum] == "D":
                    self.choiceD.setChecked(True)
                elif self.answerDict[qNum] == "E":
                    self.choiceE.setChecked(True)
        elif type_of_question == question.JudgmentQuestion:
            self.choiceQuestion.hide()
            self.judgeQuestion.show()
            self.nullButton.setChecked(True)
            self.answerQuestion.hide()
            if answered:
                qNum = str(self.questionList.currentItem().text().split(" ")[0])
                if self.answerDict[qNum] == "y":
                    self.trueButton.setChecked(True)
                elif self.answerDict[qNum] == "n":
                    self.falseButton.setChecked(True)
                elif self.answerDict[qNum] == "":
                    self.nullButton.setChecked(True)
        elif type_of_question == question.ShortAnswerQuestion:
            self.choiceQuestion.hide()
            self.judgeQuestion.hide()
            self.answerQuestion.show()
            self.anserBlank.setText("")
            if answered:
                answer = str(self.questionList.currentItem().text().split(" ")[0])
                self.anserBlank.setText(self.answerDict[answer])
        else:
            self.loginfo.print("Wrong question type when changing current Question")
        number = int(self.questionList.currentItem().text().split(" ")[0]) - 1
        self.plotQuestionInfo(self.questionWhole[number][3], self.questionWhole[number][2])

    def confirmAnswer(self):
        num = str(self.questionList.currentItem().text().split(" ")[0])
        userAns = ""
        # checkAnswer
        if self.questionWhole[int(num) - 1][1] == "choose":
            if self.choiceA.isChecked():
                userAns = "A"
            elif self.choiceB.isChecked():
                userAns = "B"
            elif self.choiceC.isChecked():
                userAns = "C"
            elif self.choiceD.isChecked():
                userAns = "D"
        elif self.questionWhole[int(num) - 1][1] == "judge":
            if self.trueButton.isChecked():
                userAns = "y"
            else:
                userAns = "n"
        elif self.questionWhole[int(num) - 1][1] == "answer":
            userAns = self.anserBlank.text()
        else:
            self.loginfo.print("wrong QuestionType")
        self.answerDict[num] = userAns
        self.questionList.currentItem().setText(num)
        self.questionList.setCurrentItem(self.questionList.item(int(num) if int(num) < len(self.questionWhole) else 0))
        self.progressBar.setProperty("value", int(100 * len(self.answerDict) / len(self.questionWhole)))
        return

    def gotoNext(self):
        num = str(self.questionList.currentItem().text().split(" ")[0])
        self.questionList.setCurrentItem(self.questionList.item(int(num) if int(num) < len(self.questionWhole) else 0))
        return

    def gotoPre(self):
        num = int(self.questionList.currentItem().text().split(" ")[0]) - 1
        self.questionList.setCurrentItem(self.questionList.item(num - 1 if num > 0 else len(self.questionWhole) - 1))
        return

    def openRegister(self):
        myReg = MyRegister(myWin)
        myReg.exec_()

    def openBankSelection(self):
        global user
        user = userInfo[self.username.text()]
        progresses = user.getProgressNum()
        progresses = [int(progresses[0] * 100 / MyWindow.chooseNum),
                      int(progresses[1] * 100 / MyWindow.judgeNum),
                      int(progresses[2] * 100 / MyWindow.answerNum)]
        myBankWin = MyBankChoose(mainWindow=myWin, progressShow=progresses)
        myBankWin.exec_()

    def submitAnswer(self):
        correct_cnt = 0
        for key, answer in self.answerDict.items():
            originText = self.questionList.item(int(key) - 1).text()
            if type(self.loadedQuestions[key]) == question.ShortAnswerQuestion or \
                    self.loadedQuestions[key].check_correctness(answer):
                self.questionWhole[int(key)-1][3] += 1
                correct_cnt += 1
                self.questionList.item(int(key)-1).setText(originText + " ✔")
            else:
                self.questionList.item(int(key)-1).setText(originText + " ✘")
            self.questionWhole[int(key) - 1][2] += 1
        self.quesionNumber.setProperty("value", correct_cnt*100/len(self.questionWhole))
        self.answerV = True
        self.saveHistory()

    def saveHistory(self):
        global user
        user = userInfo[self.username.text()]
        for table in self.questionWhole:
            user.progress.loc[table[0], "correctTimes"] = table[3]
            user.progress.loc[table[0], "answerTimes"] = table[2]
        tmp = user.progress
        user.progress = user.progress.drop(labels="Unnamed: 0", axis=1)
        user.save()
        user.progress = tmp

    def openScore(self):
        mySc = MyScore(myWin)
        mySc.exec_()


class MyLogin(gui_front.Ui_login):
    def __init__(self, parent=None, mainWin=None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None
        self.mainWin = mainWin

    def accept_logInfo(self):
        global user
        if not self.userNameLine.text() in userInfo.keys():
            self.userNameLine.setText("")
            self.passwordLine.setText("")
            return False
        if not userInfo[self.userNameLine.text()].password == self.passwordLine.text():
            self.passwordLine.setText("")
            return False
        user = userInfo[self.userNameLine.text()]
        self.mainWin.username.setText(user.name)
        self.accept()

    def loginExit(self):
        sys.exit()


def loadUserInformation():
    for f_name in os.listdir(userDirectory):
        if f_name != "__pycache__" and f_name != "usr.py" and f_name[-3:] != "csv":
            userInfo[f_name.split(".")[0]] = usr.UserInformation(f_name)


class MyBankChoose(gui_front.Ui_chooseBank):
    def __init__(self, parent=None, mainWindow=None, progressShow=None):
        super(MyBankChoose, self).__init__(parent)
        self.setupUi(self)
        if progressShow and len(progressShow) == 3:
            self.chooseProgressBar.setProperty("value", progressShow[0])
            self.judgeProgressBar.setProperty("value", progressShow[1])
            self.answerProgressBar.setProperty("value", progressShow[2])
        self.loadedQuestions = None
        self.mainWin = mainWindow

    def buildInfo(self):
        questions_type = set()
        if self.chooseCheckBox.checkState() == 2:
            questions_type.add("choose")
        if self.judgeCheckBox.checkState() == 2:
            questions_type.add("judge")
        if self.answerCheckBox.checkState() == 2:
            questions_type.add("answer")
        num = self.numberSlider.value()
        typ = dict()
        # set each type number
        typ["choose"] = int(num / len(questions_type))
        typ["judge"] = int(num / len(questions_type))
        typ["answer"] = num - typ["choose"] - typ["judge"] if num - typ["choose"] - typ["judge"] < 10 else 10
        self.mainWin.buildQuestions(typ, self.difficultySlider.value())
        self.accept()
        return


class MyRegister(gui_front.Ui_registerDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(MyRegister, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None
        self.mainWin = mainWindow

    def register(self):
        name = self.userNameLineEdit.text()
        if os.path.exists(userDirectory + name + ".txt"):
            self.feedBackBrowser.setText("same username already exist!")
            self.userNameLineEdit.setText("")
            self.passwordLineEdit.setText("")
            return
        usr.UserInformation.register(self.userNameLineEdit.text(), self.passwordLineEdit.text())
        self.accept()
        return


class MyScore(gui_front.Ui_Score):
    def __init__(self, parent=None, mainWindow=None):
        super(MyScore, self).__init__(parent)
        self.setupUi(self)
        self.loadedQuestions = None
        self.mainWin = mainWindow
        global user
        global userInfo
        history = user.getHistory()
        lis_radar = user.getRadar()
        lis_pie = user.getPie()
        # drawGraph1
        width = self.radarView.width()
        height = self.radarView.height()
        self.myImage1 = draw.Figure_Bar(width / 90, height / 90)
        self.myGraphyScene1 = QGraphicsScene()
        self.radarView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.radarView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene1.addWidget(self.myImage1)
        self.radarView.setScene(self.myGraphyScene1)
        self.myImage1.ShowImage0(lis_radar)

        # drawGraph2
        width = self.pieView.width()
        height = self.pieView.height()
        self.myImage2 = draw.Figure_Bar(width / 90, height / 90)
        self.myGraphyScene2 = QGraphicsScene()
        self.pieView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pieView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene2.addWidget(self.myImage2)
        self.pieView.setScene(self.myGraphyScene2)
        self.myImage2.ShowImage2(lis_pie)

        # drawGraph3
        width = self.historyView.width()
        height = self.historyView.height()
        self.myImage3 = draw.Figure_Bar(width / 90, height / 90)
        self.myGraphyScene3 = QGraphicsScene()
        self.historyView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.historyView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene3.addWidget(self.myImage3)
        self.historyView.setScene(self.myGraphyScene3)
        self.myImage3.ShowImage3(history)
        self.correctNumber.setProperty("value", lis_radar[0]*100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    loadUserInformation()
    myLoginWin = MyLogin(mainWin=myWin)
    myLoginWin.exec_()
    if not user:
        sys.exit()
    myWin.show()
    myWin.plotQuestionInfo(0, 0)
    sys.exit(app.exec_())
