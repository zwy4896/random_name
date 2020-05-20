#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   random_name.py
@Time    :   2020/05/20 17:23:08
@Author  :   Zhang Wuyang
@Version :   1.0
'''

# here put the import lib

import os
import sys
import random as rd
import re
from tkinter import *

def read_txt(txtFile):
    txt = []
    with open(txtFile, 'r', encoding='utf8') as f:
        for line in f:
            if '注释' not in line:
                # print(line)
                line_re = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。；;·:：？、~@#￥%……&*（）]+', "", line)
                txt.append(line_re.strip())
            else:
                continue
    return txt

def all_random(nameList, lastName, number):
    random_name_list = []
    random_name = [lastName]
    name_str = ''.join(nameList)
    name = ''
    str_len = len(name_str)
    for num in (range(number)):
        word_number = rd.randint(1, 3)
        for n in range(word_number):
            random_pos = rd.randint(0, str_len)
            random_name.append(name_str[random_pos])
        name = ''.join(random_name)
        random_name = [lastName]
        random_name_list.append(name)
    return random_name_list

def half_random(nameList):
    lastName = last_name.get()
    number = int(total_number.get())
    random_name_list = []
    random_name = [lastName]
    name_str = ''.join(nameList)
    name = ''
    str_len = len(name_str)
    for num in (range(number)):
        random_pos = rd.randint(0, str_len)
        word_number = rd.randint(1, 3)
        for n in range(word_number):
            try:
                random_name.append(name_str[random_pos + n - 1])
            except IndexError:
                continue
        name = ''.join(random_name)
        random_name = [lastName]
        random_name_list.append(name)
    for each in random_name_list:
        text.insert(END, each)
        text.see(END)
        text.update()
    return random_name_list

def main(txt_file):
    global last_name, total_number, text
    root = Tk()
    root.title("'科学'起名")
    root.geometry('550x420+398+279')
	#Label
    text = ['宝宝姓氏', '生成数量']
    row = 0
    for t in text:
        Label(root,text=t,font=("微软雅黑", 20),fg='black').grid(row=row, column=0)
        row += 1
    last_name = Entry(root,font=("微软雅黑",15))
    last_name.grid(row=0, column=1)
    total_number = Entry(root,font=("微软雅黑",15))
    total_number.grid(row=1, column=1)
    text=Listbox(root,font=('微软雅黑',15),width=45,height=10)
    text.grid(row=2,columnspan=2)
    button =Button(root,text='开始生成',font=("微软雅黑",15),command=lambda: half_random(txt_file)).grid(row=3,column=0,sticky=W)
    button =Button(root,text='退出',font=("微软雅黑",15),command=root.quit).grid(row=3,column=1,sticky=E)
    mainloop()
if __name__ == '__main__':
    # rd.seed(12345)
    # global txt_file
    txt_file = './shijing.txt'
    txt = read_txt(txt_file)
    main(txt)

    # txt = read_txt(txt_file)
    # # test = all_random(txt, '张', 100)
    # test = half_random(txt, '张', 10)
    # for name in test:
    #     print(name)