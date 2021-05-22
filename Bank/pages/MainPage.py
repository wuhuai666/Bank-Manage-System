from Bank.Frame.GetFrame import GetFrame
from Bank.Frame.LockFrame import LockFrame
from Bank.Frame.QueryFrame import QueryFrame
from Bank.Frame.SaveFrame import SaveFrame
from Bank.Frame.TransferFrame import TransferFrame
from Bank.Frame.UnlockFrame import UnlockFrame
from Bank.Frame.exitFrame import exitFrame
from Bank.pages.view import *  # 菜单栏对应的各个子页面
class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (800, 500))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.CreatePage = CreateFrame(self.root)  # 创建不同Frame
        self.QueryPage = QueryFrame(self.root)
        self.GetPage = GetFrame(self.root)
        self.SavePage = SaveFrame(self.root)
        self.TransferPage = TransferFrame(self.root)
        self.LockPage = LockFrame(self.root)
        self.UnlockPage = UnlockFrame(self.root)
        self.exitPage = exitFrame(self.root)
        self.CreatePage.pack()  # 默认显示开户界面
        # 创建顶部菜单栏
        menubar = Menu(self.root)
        menubar.add_command(label='开户', command=self.create)
        menubar.add_command(label='查询', command=self.query)
        menubar.add_command(label='取款', command=self.getMoney)
        menubar.add_command(label='存款', command=self.saveMoney)
        menubar.add_command(label='转账', command=self.transfer)
        menubar.add_command(label='锁定', command=self.lock)
        menubar.add_command(label='解锁', command=self.unlock)
        menubar.add_command(label='退出', command=self.exit)
        self.root['menu'] = menubar  # 设置菜单栏
    def create(self):
        self.CreatePage.pack()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def query(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def getMoney(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack()
        self.SavePage.pack_forget()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def saveMoney(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def transfer(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.TransferPage.pack()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.exitPage.pack_forget()

    def lock(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.LockPage.pack()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def unlock(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.LockPage.pack_forget()
        self.UnlockPage.pack()
        self.TransferPage.pack_forget()
        self.exitPage.pack_forget()

    def exit(self):
        self.CreatePage.pack_forget()
        self.QueryPage.pack_forget()
        self.GetPage.pack_forget()
        self.SavePage.pack_forget()
        self.LockPage.pack_forget()
        self.UnlockPage.pack_forget()
        self.TransferPage.pack_forget()
        self.exitPage.pack()

