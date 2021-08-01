# -*- coding: utf-8 -*-
# @Time : 2021-08-01 21:14
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : usr.py
# @Software: PyCharm
import os
class UserInformation:
    def __init__(self, f_name: str):
        with open(f_name) as f:
            self.name = f_name.split(".")[0]
            self.password = f.readline()
            self.process = f.readline()
