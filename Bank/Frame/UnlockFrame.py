from  tkinter import *

from Bank.Function.UnlockCard import UnlockCard


class UnlockFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.IdNumber = StringVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='银行卡号: ', font=('华文行楷', 15)).grid(row=1, stick=W, pady=10)
        Entry(self, font=('华文行楷', 15),textvariable=self.IdNumber).grid(row=1, column=1, stick=E)
        Label(self, text='密码: ', font=('华文行楷', 15)).grid(row=2, stick=W, pady=10)
        Entry(self,font=('华文行楷', 15), show="*",textvariable=self.password).grid(row=2, column=1, stick=E)
        Button(self, text='解锁银行卡', font=('华文行楷', 15),command=self.unlock).grid(row=6, column=1, stick=E, pady=10)
    def unlock(self):
        Idnumber = self.IdNumber.get()
        password = self.password.get()
        unlock = UnlockCard(Idnumber, password)
        unlock.UnLock()