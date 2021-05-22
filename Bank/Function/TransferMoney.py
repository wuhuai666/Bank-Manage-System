from tkinter.messagebox import showerror, showinfo, askokcancel

from Bank.DbUtils.DbUtils import *


class TransferMoney:
    def __init__(self, Idcard1,Idcard2, password, money):
        self.Idcard1 = Idcard1
        # 别人的银行卡号
        self.Idcard2 = Idcard2
        self.password = password
        self.money = money

    def  transferMoney(self,count):
         while True:
             #别人的银行卡
             another_cardId= self.Idcard2
             # 自己的银行卡
             cardId = self.Idcard1
             cardPwd = self.password
             money = self.money
             count2 = -1
             conn = DbUtils.getConnection(self)
             cursor = conn.cursor()
             # 查询别人卡的状态
             sql1 = "select cardLock from card where cardId='%s'" % (another_cardId)
             cursor.execute(sql1)
             another_result = cursor.fetchone()
             # 转入账号不存在
             if another_result==None:
                 another_result="3"
             else:
                 another_result="".join(another_result)
             if another_result=="3":
                 showerror(title='不存在', message='转入的账户 '+another_cardId+ '不存在!')
             elif another_result=="1":
                 showerror(title='锁定', message='转入账户 '+another_cardId+' 被锁定,不能转账!')
             else:
                 # 查询自己卡的状态
                 sql = "select cardLock from card where cardId='%s' and cardPwd='%s'" % (cardId, cardPwd)
                 cursor.execute(sql)
                 result = cursor.fetchone()
                 # 判断是转出的账号不存在或者是密码错误
                 if result == None:
                     sql2 = "select cardId from card where cardId='%s'" % (cardId)
                     cursor.execute(sql2)
                     result2 = cursor.fetchone()
                     if result2 == None:
                         # 账号不存在的情况
                         showerror(title='不存在', message='转出账号'+cardId+'不存在')
                         break
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
                             showerror(title='锁定', message='你的账户 '+cardId+' 已上锁,请先解锁后转账!')
                             return 0
                         else:
                             count2 = count - 1
                             showerror(title='错误', message='密码错误,你还剩' + str(count2) + '次机会!')
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
                         showerror(title='锁定', message='你的账户 '+cardId+' 已上锁,请先解锁后转账!')
                         return 0
                     # 卡没被锁,转账
                     else:
                         # 查询转出账户的余额
                         sql1 = "select money from card where cardId='%s' and cardPwd='%s'" % (cardId, cardPwd)
                         cursor.execute(sql1)
                         result = cursor.fetchone()
                         # 查询转入账户的余额
                         sql2 = "select money from card where cardId='%s' " % (another_cardId)
                         cursor.execute(sql2)
                         another_result = cursor.fetchone()
                         for row in result:
                             result = row
                         for row1 in another_result:
                             another_result=row1
                             # 余额不足
                             if result < money:
                                 showerror(title="余额不足", message='余额不足,你余额为 ' + str(result) + '元!')
                             else:
                                 if cardId==another_cardId:
                                     showerror(title='错误',message='不能给自己转账!')
                                 else:
                                     a = askokcancel('转账', '确认向账户为: ' + another_cardId + ' 转账' + str(money) + '元?')
                                     if a == True:
                                         # 转账,转出账户减钱
                                         result2 = str((int(result) - money))
                                         sql = "update card set money=%s where cardId='%s' and cardPwd='%s'" % (
                                             result2, cardId, cardPwd)
                                         cursor.execute(sql)
                                         conn.commit()
                                         # 转入账户加钱
                                         result3 = str((int(another_result) + money))
                                         sql = "update card set money=%s where cardId='%s'" % (result3, another_cardId)
                                         cursor.execute(sql)
                                         conn.commit()
                                         showinfo(title="转账成功", message='你现在的余额为:' + result2 + '元!')
                         break
             break
         if count2 == 0:
             showerror(title='卡号锁定', message='你已经输错了3次,账号已被锁定!')
             sql3 = "update card set cardLock=1 where cardId='%s'" % (cardId)
             cursor.execute(sql3)
             conn.commit()
             cursor.close()
             conn.close()
             return count2
         elif count2 > 0:
             cursor.close()
             conn.close()
             return count2
         return count
