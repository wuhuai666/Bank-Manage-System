from tkinter import *
from tkinter.messagebox import askokcancel

from Bank.Function.TransferMoney import TransferMoney


class TransferFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.IdNumber1 = StringVar()
        self.IdNumber2 = StringVar()
        self.money = DoubleVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='转出银行卡号: ', font=('华文行楷', 15)).grid(row=1, stick=W, pady=10)
        Entry(self,font=('华文行楷', 15), textvariable=self.IdNumber1).grid(row=1, column=1, stick=E)
        Label(self, text='转入银行卡号: ', font=('华文行楷', 15)).grid(row=2, stick=W, pady=10)
        Entry(self, font=('华文行楷', 15),textvariable=self.IdNumber2).grid(row=2, column=1, stick=E)
        Label(self, text='转账金额: ', font=('华文行楷', 15)).grid(row=3, stick=W, pady=10)
        Entry(self, font=('华文行楷', 15),textvariable=self.money).grid(row=3, column=1, stick=E)
        Label(self, text='密码: ', font=('华文行楷', 15)).grid(row=4, stick=W, pady=10)
        Entry(self, show="*",font=('华文行楷', 15),textvariable=self.password).grid(row=4, column=1, stick=E)
        Button(self, text='转账', font=('华文行楷', 15),command=self.transfer).grid(row=6, column=1, stick=E, pady=10)
    count=3
    def transfer(self):
        global count
        # 自己的银行卡
        Id1=self.IdNumber1.get()
        # 别人的银行卡
        Id2=self.IdNumber2.get()
        money = self.money.get()
        password = self.password.get()
        trans= TransferMoney(Id1, Id2, password, money)
        count1 = trans.transferMoney(self.count)
        if count1 == 0:
            self.count = 3
        else:
            self.count = count1
            TransferFrame()

