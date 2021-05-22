from  tkinter import *
from Bank.Function.GetMoney import GetMoney
class GetFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.IdNumber = StringVar()
        self. password= StringVar()
        self.money=DoubleVar()
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='银行卡号: ', font=('华文行楷', 15)).grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.IdNumber, font=('华文行楷', 15)).grid(row=1, column=1, stick=E)
        Label(self, text='密码: ', font=('华文行楷', 15)).grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.password,show="*", font=('华文行楷', 15)).grid(row=2, column=1, stick=E)
        Label(self, text='取款金额: ', font=('华文行楷', 15)).grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.money, font=('华文行楷', 15)).grid(row=3, column=1, stick=E)
        Button(self, text='取款', font=('华文行楷', 15),command=self.get).grid(row=6, column=1, stick=E, pady=10)
    count = 3
    def get(self):
        # 局部变量
        global count
        Idnumber = self.IdNumber.get()
        password = self.password.get()
        money = self.money.get()
        get = GetMoney(Idnumber, password, money)
        count1 = get.get(self.count)
        if count1 == 0:
            self.count = 3
        else:
            self.count = count1
            GetFrame()