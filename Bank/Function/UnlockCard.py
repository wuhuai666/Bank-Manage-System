from tkinter.messagebox import showerror, showinfo
from Bank.DbUtils.DbUtils import *
class UnlockCard:
    def __init__(self, Idcard, password):
        self.Idcard = Idcard
        self.password = password
    def UnLock(self):
        # 查询信息
        cardId = self.Idcard
        cardPwd = self.password
        conn = DbUtils.getConnection(self)
        cursor = conn.cursor()
        # 先查询卡的状态
        sql = "select cardLock from card where cardId='%s' and cardPwd='%s'" % (cardId, cardPwd)
        cursor.execute(sql)
        result = cursor.fetchone()
        # 判断是账号不存在或者是密码错误
        if result == None:
            sql2 = "select cardId from card where cardId='%s'" % (cardId)
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            if result2 == None:
                # 账号不存在的情况
                showerror(title='账户', message='你输入的账号不存在')
            else:
                # 账号存在的情况,密码错误,先判断是否上锁
                sql = "select cardLock from card where cardId='%s'" % (cardId)
                cursor.execute(sql)
                result3 = cursor.fetchone()
                for row in result3:
                    result3 = row
                if result3 == "1":
                    # 解锁
                    showerror(title='锁定', message="卡号已被锁定!,请输入正确的密码解锁")
                    return 0
                else:
                    showerror(title='密码错误', message='你输入的密码错误,请重新输入')
        else:
            # 账号正确和密码正确
            # 判断有没有被锁...........
            sql = "select cardLock from card where cardId='%s'" % (cardId)
            cursor.execute(sql)
            result3 = cursor.fetchone()
            for row in result3:
                result3 = row
            # 卡号被锁,解锁
            if result3 == "1":
                sql1 = "update card set cardLock=0 where cardId='%s'" % (cardId)
                cursor.execute(sql1)
                conn.commit()
                showinfo(title='解锁', message='你的银行卡' + cardId + '已被解锁！')
            # 卡没被锁,
            else:
                showerror(title='解锁', message="你的卡号没被锁定,可以正常使用!")
                return 0