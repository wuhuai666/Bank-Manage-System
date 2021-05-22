from Bank.pages.LoginPage import *
from Bank.Function.CreateUsers import *
from tkinter.messagebox import showinfo, showerror


class CreateFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.IdCard = StringVar()
        self.phoneNumber = StringVar()
        self.savaMoney = DoubleVar()
        self.password = StringVar()
        self.repwd = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='姓名: ',font=('华文行楷', 15)).grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.username,font=('华文行楷', 15)).grid(row=1, column=1, stick=E)
        Label(self, text='身份证号码: ',font=('华文行楷', 15)).grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.IdCard,font=('华文行楷', 15)).grid(row=2, column=1, stick=E)
        Label(self, text='手机号码: ',font=('华文行楷', 15)).grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.phoneNumber,font=('华文行楷', 15)).grid(row=3, column=1, stick=E)
        Label(self, text='预存金额: ',font=('华文行楷', 15)).grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.savaMoney,font=('华文行楷', 15)).grid(row=4, column=1, stick=E)
        Label(self, text='密码: ',font=('华文行楷', 15)).grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.password,show='*',font=('华文行楷', 15)).grid(row=5, column=1, stick=E)
        Label(self, text='确认密码: ',font=('华文行楷', 15)).grid(row=6, stick=W, pady=10)
        Entry(self, show='*',textvariable=self.repwd,font=('华文行楷', 15)).grid(row=6, column=1, stick=E)
        Button(self, text='开户',font=('华文行楷', 15),command=self.createUser).grid(row=7, column=1, stick=E, pady=10)

    def createUser(self):
         username = self.username.get()
         Idcard =self.IdCard.get()
         phoneNumber= self.phoneNumber.get()
         savaMoney= self.savaMoney.get()
         password=self.password.get()
         repwd=self.repwd.get()
         if username == "" or Idcard == "" or phoneNumber == "" or savaMoney == "":
             showerror(title='信息不全', message='请输入完整的信息！')
         elif password == "" or repwd == "":
             showerror(title='确认密码', message='请输入密码两次！')
             self.password.set("")
             self.repwd.set("")
         elif (password != repwd):
             showerror(title='密码不一致', message='两次密码输入不一致！')
             self.password.set("")
             self.repwd.set("")
         else:
             users = CreateUsers(username, Idcard, phoneNumber, savaMoney, password, repwd)
             card = users.creatUser()
             self.username.set("")
             self.savaMoney.set(0.0)
             self.password.set("")
             self.repwd.set("")
             self.IdCard.set("")
             self.phoneNumber.set("")
             showinfo(title='成功',message='你的银行卡号码为:' + card + '！')

