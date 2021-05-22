from  tkinter import *
from tkinter.messagebox import showinfo, showerror, askokcancel
from Bank.DbUtils.DbUtils import *
class exitFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        #  pady：设置控件周围垂直方向空白区域保留大小；
        Label(self, text='管理员: ', font=('华文行楷', 15)).grid(row=10, stick=W, pady=10)
        Entry(self, font=('华文行楷', 15),textvariable=self.username).grid(row=10, column=1, stick=E)
        Label(self, text='密码: ', font=('华文行楷', 15)).grid(row=11, stick=W, pady=10)
        Entry(self, font=('华文行楷', 15),textvariable=self.password, show='*').grid(row=11, column=1, stick=E)
        Button(self, text='退出', font=('华文行楷', 15), command=self.exit).grid(row=12, column=1, stick=E)
    def exit(self):
        username = self.username.get()
        password = self.password.get()
        sql = "select AdminName,AdminPassword from admin where AdminName='%s' and AdminPassword='%s'" % (
            username, password)
        connection = DbUtils.getConnection(self)
        cursor = connection.cursor()
        execute = cursor.execute(sql)
        connection.commit()
        if execute != 0:
            # 销毁登录界面
            a = askokcancel('退出', '确认关闭系统吗?')
            if a==True:
             self.quit()
        else:
            showerror(title='错误', message='账号或密码错误,请联系管理员')