# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2000, 1500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleFrame = QtWidgets.QFrame(self.centralwidget)
        self.titleFrame.setGeometry(QtCore.QRect(190, 190, 1671, 271))
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.textBrowser = QtWidgets.QTextBrowser(self.titleFrame)
        self.textBrowser.setGeometry(QtCore.QRect(60, 10, 1581, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.ctrlButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.ctrlButtonFrame.setGeometry(QtCore.QRect(1410, 510, 481, 121))
        self.ctrlButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ctrlButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ctrlButtonFrame.setObjectName("ctrlButtonFrame")
        self.last = QtWidgets.QPushButton(self.ctrlButtonFrame)
        self.last.setGeometry(QtCore.QRect(300, 20, 121, 71))
        self.last.setObjectName("last")
        self.confirm = QtWidgets.QPushButton(self.ctrlButtonFrame)
        self.confirm.setGeometry(QtCore.QRect(10, 20, 131, 71))
        self.confirm.setObjectName("confirm")
        self.next = QtWidgets.QPushButton(self.ctrlButtonFrame)
        self.next.setGeometry(QtCore.QRect(160, 20, 121, 71))
        self.next.setObjectName("next")
        self.quesionNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.quesionNumber.setGeometry(QtCore.QRect(250, 140, 171, 51))
        self.quesionNumber.setObjectName("quesionNumber")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(500, 140, 291, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.upBaseLine = QtWidgets.QFrame(self.centralwidget)
        self.upBaseLine.setGeometry(QtCore.QRect(20, 60, 1971, 21))
        self.upBaseLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.upBaseLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.upBaseLine.setObjectName("upBaseLine")
        self.bottomBaseLine = QtWidgets.QFrame(self.centralwidget)
        self.bottomBaseLine.setGeometry(QtCore.QRect(30, 630, 1971, 16))
        self.bottomBaseLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomBaseLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottomBaseLine.setObjectName("bottomBaseLine")



        self.cur_process = QtWidgets.QLabel(self.centralwidget)
        self.cur_process.setGeometry(QtCore.QRect(500, 110, 251, 20))
        self.cur_process.setObjectName("cur_process")
        self.cur_score = QtWidgets.QLabel(self.centralwidget)
        self.cur_score.setGeometry(QtCore.QRect(250, 110, 181, 20))
        self.cur_score.setObjectName("cur_score")
        self.questions_block = QtWidgets.QLabel(self.centralwidget)
        self.questions_block.setGeometry(QtCore.QRect(20, 110, 191, 16))
        self.questions_block.setObjectName("questions_block")
        self.questionList = QtWidgets.QListWidget(self.centralwidget)
        self.questionList.setGeometry(QtCore.QRect(20, 130, 191, 491))
        self.questionList.setObjectName("questionList")

        # stateGraph
        self.stateGraph = QtWidgets.QGraphicsView(self.centralwidget)
        self.stateGraph.setGeometry(QtCore.QRect(20, 690, 1051, 731))
        self.stateGraph.setObjectName("stateGraph")

        # user information frame
        self.user_info = QtWidgets.QFrame(self.centralwidget)
        self.user_info.setGeometry(QtCore.QRect(10, 0, 241, 61))
        self.user_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_info.setObjectName("user_info")
        self.widget = QtWidgets.QWidget(self.user_info)
        self.widget.setGeometry(QtCore.QRect(10, 20, 211, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user = QtWidgets.QLabel(self.widget)
        self.user.setObjectName("user")
        self.horizontalLayout.addWidget(self.user)
        self.username = QtWidgets.QLabel(self.widget)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)

        # choose question frame
        self.choiceQuestion = QtWidgets.QFrame(self.centralwidget)
        self.choiceQuestion.setGeometry(QtCore.QRect(250, 450, 641, 171))
        self.choiceQuestion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choiceQuestion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choiceQuestion.setObjectName("choiceQuestion")
        self.answerBlock_2 = QtWidgets.QLabel(self.choiceQuestion)
        self.answerBlock_2.setGeometry(QtCore.QRect(10, 0, 151, 51))
        self.answerBlock_2.setObjectName("answerBlock_2")
        self.layoutWidget = QtWidgets.QWidget(self.choiceQuestion)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 376, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.choices = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.choices.setContentsMargins(0, 0, 0, 0)
        self.choices.setObjectName("choices")
        self.choiceA = QtWidgets.QRadioButton(self.layoutWidget)
        self.choiceA.setObjectName("choiceA")
        self.choices.addWidget(self.choiceA)
        self.choiceB = QtWidgets.QRadioButton(self.layoutWidget)
        self.choiceB.setObjectName("choiceB")
        self.choices.addWidget(self.choiceB)
        self.choiceC = QtWidgets.QRadioButton(self.layoutWidget)
        self.choiceC.setObjectName("choiceC")
        self.choices.addWidget(self.choiceC)
        self.choiceD = QtWidgets.QRadioButton(self.layoutWidget)
        self.choiceD.setObjectName("choiceD")
        self.choices.addWidget(self.choiceD)

        # judge question frame
        self.judgeQuestion = QtWidgets.QFrame(self.centralwidget)
        self.judgeQuestion.setGeometry(QtCore.QRect(250, 450, 641, 171))
        self.judgeQuestion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.judgeQuestion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.judgeQuestion.setObjectName("ansJudgeFrame")
        self.falseButton = QtWidgets.QRadioButton(self.judgeQuestion)
        self.falseButton.setGeometry(QtCore.QRect(150, 60, 131, 91))
        self.falseButton.setObjectName("falseButton")
        self.trueButton = QtWidgets.QRadioButton(self.judgeQuestion)
        self.trueButton.setGeometry(QtCore.QRect(10, 60, 131, 91))
        self.trueButton.setObjectName("trueButton")
        self.answerBlock = QtWidgets.QLabel(self.judgeQuestion)
        self.answerBlock.setGeometry(QtCore.QRect(10, 0, 151, 51))
        self.answerBlock.setObjectName("answerBlock")

        # answer question frame
        self.answerQuestion = QtWidgets.QFrame(self.centralwidget)
        self.answerQuestion.setGeometry(QtCore.QRect(250, 450, 641, 171))
        self.answerQuestion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answerQuestion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answerQuestion.setObjectName("answerQuestion")
        self.answerBlock_3 = QtWidgets.QLabel(self.answerQuestion)
        self.answerBlock_3.setGeometry(QtCore.QRect(10, 0, 151, 51))
        self.answerBlock_3.setObjectName("answerBlock_3")
        self.anserBlank = QtWidgets.QTextBrowser(self.answerQuestion)
        self.anserBlank.setGeometry(QtCore.QRect(20, 60, 561, 101))
        self.anserBlank.setObjectName("anserBlank")

        # login information
        self.loginfo = QtWidgets.QTextEdit(self.centralwidget)
        self.loginfo.setGeometry(QtCore.QRect(1170, 690, 631, 731))
        self.loginfo.setObjectName("loginfo")
        MainWindow.setCentralWidget(self.centralwidget)

        # menu
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 2000, 22))
        self.menuBar.setObjectName("menuBar")
        self.bank = QtWidgets.QMenu(self.menuBar)
        self.bank.setObjectName("bank")
        self.userSettings = QtWidgets.QMenu(self.menuBar)
        self.userSettings.setObjectName("userSettings")
        self.menusecurity = QtWidgets.QMenu(self.userSettings)
        self.menusecurity.setObjectName("menusecurity")
        self.settings = QtWidgets.QMenu(self.menuBar)
        self.settings.setObjectName("settings")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actiontype_selection = QtWidgets.QAction(MainWindow)
        self.actiontype_selection.setObjectName("actiontype_selection")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionexport = QtWidgets.QAction(MainWindow)
        self.actionexport.setObjectName("actionexport")
        self.actionscore = QtWidgets.QAction(MainWindow)
        self.actionscore.setObjectName("actionscore")
        self.actionchangepassword = QtWidgets.QAction(MainWindow)
        self.actionchangepassword.setObjectName("actionchangepassword")
        self.bank.addAction(self.actiontype_selection)
        self.bank.addAction(self.actionImport)
        self.bank.addAction(self.actionexport)
        self.menusecurity.addAction(self.actionchangepassword)
        self.userSettings.addAction(self.actionscore)
        self.userSettings.addAction(self.menusecurity.menuAction())
        self.menuBar.addAction(self.bank.menuAction())
        self.menuBar.addAction(self.userSettings.menuAction())
        self.menuBar.addAction(self.settings.menuAction())

        self.retranslateUi(MainWindow)
        self.confirm.clicked.connect(self.progressBar.reset)
        self.questionList.currentRowChanged['int'].connect(MainWindow.changeQuestion)
        self.confirm.clicked.connect(self.questionList.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.last.setText(_translate("MainWindow", "last"))
        self.confirm.setText(_translate("MainWindow", "confirm"))
        self.next.setText(_translate("MainWindow", "next"))
        self.falseButton.setText(_translate("MainWindow", "False"))
        self.trueButton.setText(_translate("MainWindow", "True"))
        self.answerBlock.setText(_translate("MainWindow", "anser_block"))
        self.cur_process.setText(_translate("MainWindow", "current_process"))
        self.cur_score.setText(_translate("MainWindow", "current_score"))
        self.questions_block.setText(_translate("MainWindow", "questions_block"))
        __sortingEnabled = self.questionList.isSortingEnabled()
        self.questionList.setSortingEnabled(False)
        self.questionList.setSortingEnabled(__sortingEnabled)
        self.user.setText(_translate("MainWindow", "user: "))
        self.username.setText(_translate("MainWindow", "TextLabel"))
        self.answerBlock_2.setText(_translate("MainWindow", "anser_block"))
        self.choiceA.setText(_translate("MainWindow", "A"))
        self.choiceB.setText(_translate("MainWindow", "B"))
        self.choiceC.setText(_translate("MainWindow", "C"))
        self.choiceD.setText(_translate("MainWindow", "D"))
        self.answerBlock_3.setText(_translate("MainWindow", "anser_block"))
        self.bank.setTitle(_translate("MainWindow", "题库"))
        self.userSettings.setTitle(_translate("MainWindow", "用户"))
        self.menusecurity.setTitle(_translate("MainWindow", "security"))
        self.settings.setTitle(_translate("MainWindow", "设置"))
        self.action.setText(_translate("MainWindow", "daorutiku"))
        self.actiontype_selection.setText(_translate("MainWindow", "type selection"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionexport.setText(_translate("MainWindow", "export"))
        self.actionscore.setText(_translate("MainWindow", "score"))
        self.actionchangepassword.setText(_translate("MainWindow", "password"))


class Ui_login(QDialog):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(600, 450)
        self.userNameLine = QtWidgets.QLineEdit(login)
        self.userNameLine.setGeometry(QtCore.QRect(200, 100, 311, 31))
        self.userNameLine.setObjectName("userNameLine")
        self.usernameLabel = QtWidgets.QLabel(login)
        self.usernameLabel.setGeometry(QtCore.QRect(70, 90, 121, 41))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(login)
        self.passwordLabel.setGeometry(QtCore.QRect(70, 160, 131, 41))
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLine = QtWidgets.QLineEdit(login)
        self.passwordLine.setGeometry(QtCore.QRect(200, 170, 311, 31))
        self.passwordLine.setObjectName("passwordLine")
        self.frame = QtWidgets.QFrame(login)
        self.frame.setGeometry(QtCore.QRect(30, 260, 521, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.forgot_passwordButton = QtWidgets.QPushButton(self.frame)
        self.forgot_passwordButton.setGeometry(QtCore.QRect(0, 20, 201, 61))
        self.forgot_passwordButton.setObjectName("forgot_passwordButton")
        self.enterButton = QtWidgets.QPushButton(self.frame)
        self.enterButton.setGeometry(QtCore.QRect(240, 20, 121, 61))
        self.enterButton.setObjectName("enterButton")
        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(380, 20, 121, 61))
        self.exitButton.setObjectName("exitButton")


        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        self.enterButton.clicked.connect(login.accept_logInfo)
        self.exitButton.clicked.connect(login.loginExit)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.usernameLabel.setText(_translate("login", "username:"))
        self.passwordLabel.setText(_translate("login", "password:"))
        self.forgot_passwordButton.setText(_translate("login", "forgot_password?"))
        self.enterButton.setText(_translate("login", "enter"))
        self.exitButton.setText(_translate("login", "exit"))

