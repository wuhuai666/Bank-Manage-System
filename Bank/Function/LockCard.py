from tkinter.messagebox import showerror, showinfo

from Bank.DbUtils.DbUtils import *


class LockCard:
    def __init__(self, Idcard, password):
        self.Idcard = Idcard
        self.password = password
    def Lock(self):
        # 查询信息
        cardId = self.Idcard
        cardPwd = self.password
        count2 = -1
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
                # 账号存在的情况
                # 密码错误
                # 不管有没有次数,都要判断是否被锁定
                sql = "select cardLock from card where cardId='%s'" % (cardId)
                cursor.execute(sql)
                result3 = cursor.fetchone()
                for row in result3:
                    result3 = row
                if result3 == "1":
                    showerror(title='卡号锁定', message="你的账号已经被锁了,请先解锁!")
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
            # 卡号被锁
            if result3 == "1":
                showerror(title='卡号锁定', message="你的账号已经被锁了,请先解锁!")
                return 0
            # 卡没被锁,上锁
            else:
                sql1 = "update card set cardLock=1 where cardId='%s'"%(cardId)
                cursor.execute(sql1)
                conn.commit()
                showinfo(title='上锁', message='你的银行卡' + cardId + '已经上锁！')