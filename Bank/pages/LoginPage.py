from tkinter import *
from tkinter.messagebox import showerror
from Bank.pages.MainPage import *
from Bank.pages.MainPage import MainPage


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        # stick=w右对齐,N/S/E/W，分别代表上对齐/下对齐/左对齐/右对齐，
        Label(self.page).grid(row=0, stick=W)
        #  pady：设置控件周围垂直方向空白区域保留大小；
        Label(self.page, text='管理员: ',font = ('华文行楷' , 15)).grid(row=1, stick=W, pady=10)
        Entry(self.page,font=('华文行楷', 15), textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ',font = ('华文行楷' , 15)).grid(row=2, stick=W, pady=10)
        Entry(self.page, font=('华文行楷', 15),textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', font = ('华文行楷' , 15),command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', font = ('华文行楷' , 15),command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        username = self.username.get()
        password = self.password.get()
        sql = "select AdminName,AdminPassword from admin where AdminName='%s' and AdminPassword='%s'" % (
        username, password)
        connection = DbUtils.getConnection(self)
        cursor = connection.cursor()
        execute = cursor.execute(sql)
        connection.commit()
        if execute!=0:
            #销毁登录界面
            self.page.destroy()
            MainPage(self.root)
        else:
            showerror(title='输入错误', message='账号或密码错误！')
