# -*- coding: utf-8 -*-
# @Time : 2021-08-01 21:14
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : usr.py
# @Software: PyCharm
import gui_back
import pandas as pd


class UserInformation:
    def __init__(self, f_name: str):
        with open(gui_back.userDirectory + f_name) as f:
            self.name = f_name.split(".")[0]
            self.password = f.readline()[:-1]
            self.progress = pd.read_csv(gui_back.userDirectory + self.name + ".csv")

    @staticmethod
    def register(name: str, password: str) -> None:
        with open(gui_back.userDirectory + name+".txt", "w+") as f:
            f.write(password + "\n")
        typ = ["choose" for _ in range(gui_back.MyWindow.chooseNum)] + \
              ["judge" for _ in range(gui_back.MyWindow.judgeNum)] + \
              ["answer" for _ in range(gui_back.MyWindow.answerNum)]
        answerTimes = [0] * len(typ)
        correctTimes = [0] * len(typ)
        progress = pd.DataFrame({"type": typ, "answerTimes": answerTimes, "correctTimes": correctTimes}, index=range(110))
        progress.to_csv(gui_back.userDirectory + name+".csv")

    def getProgressNum(self) -> list:
        res = []
        cnt = 0
        tmp = self.progress[self.progress["type"] == "choose"]
        for x in tmp.loc[:, "answerTimes"]:
            cnt += 1 if int(x) > 0 else 0
        res.append(cnt)
        cnt = 0
        tmp = self.progress[self.progress["type"] == "judge"]
        for x in tmp.loc[:, "answerTimes"]:
            cnt += 1 if int(x) > 0 else 0
        res.append(cnt)
        cnt = 0
        tmp = self.progress[self.progress["type"] == "answer"]
        print(tmp.loc[:, "answerTimes"])
        for x in tmp.loc[:, "answerTimes"]:
            cnt += 1 if int(x) > 0 else 0
        res.append(cnt)
        return res

    # save information back to .csv
    def save(self):
        self.progress.to_csv(gui_back.userDirectory + self.name + ".csv")

    def getHistory(self):
        with open(gui_back.userDirectory + self.name + ".txt", "r") as f:
            f.readline()
            return [float(x) for x in f.readline()[:-1].split(" ")]

    def getRadar(self):
        ans = self.progress["answerTimes"].sum()
        cor = self.progress["correctTimes"].sum()
        cnt = 0
        for x in self.progress.loc[:, "answerTimes"]:
            cnt += 1 if int(x) > 0 else 0
        correctRate = int(cor*100/(ans if ans != 0 else 0))
        return [correctRate/100, ans/300, cor/200, cnt/110]

    def getPie(self):
        ans_a = self.progress[self.progress["type"] == "answer"]["answerTimes"].sum()
        cor_a = self.progress[self.progress["type"] == "answer"]["correctTimes"].sum()
        ans_j = self.progress[self.progress["type"] == "judge"]["answerTimes"].sum()
        cor_j = self.progress[self.progress["type"] == "judge"]["correctTimes"].sum()
        ans_c = self.progress[self.progress["type"] == "choose"]["answerTimes"].sum()
        cor_c = self.progress[self.progress["type"] == "choose"]["correctTimes"].sum()
        return [int(cor_a*100/(ans_a if ans_a != 0 else 0)),
                int(cor_j*100/(ans_j if ans_j != 0 else 0)),
                int(cor_c*100/(ans_c if ans_c != 0 else 0))]
