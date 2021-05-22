from tkinter.messagebox import showinfo, showerror
from Bank.DbUtils.DbUtils import *
class SaveMoney:
    def __init__(self,Idcard,password,money):
        self.Idcard=Idcard
        self.password=password
        self.money=money
    def save(self,count):
     while True:
        # 查询信息
        cardId = self.Idcard
        cardPwd = self.password
        money=self.money
        count2=-1
        conn = DbUtils.getConnection(self)
        cursor = conn.cursor()
        # 先查询卡的状态
        sql = "select cardLock from card where cardId='%s' and cardPwd='%s'" % (cardId, cardPwd)
        cursor.execute(sql)
        result = cursor.fetchone()
        # 判断是账号不存在或者是密码错误
        if result==None:
            sql2 = "select cardId from card where cardId='%s'" % (cardId)
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            if result2 == None:
                #账号不存在的情况
                showerror(title='账号不存在', message='你输入的账号不存在')
                break
            else:
                #账号存在的情况
                # 密码错误
                #不管有没有次数,都要判断是否被锁定
                sql = "select cardLock from card where cardId='%s'" % (cardId)
                cursor.execute(sql)
                result3 = cursor.fetchone()
                for row in result3:
                    result3=row
                if result3=="1":
                    showerror(title='卡号锁定',message="你的账号已经被锁了,请先解锁后使用!")
                    return 0
                else:
                    count2 = count - 1
                    showerror(title='错误', message='密码错误,你还剩' + str(count2) + '次机会!')
        else:
            # 账号正确和密码正确
            #判断有没有被锁...........
            sql = "select cardLock from card where cardId='%s'" % (cardId)
            cursor.execute(sql)
            result3 = cursor.fetchone()
            for row in result3:
                result3 = row
            # 卡号被锁
            if result3 == "1":
                showerror(title='卡号被锁', message="你的账号已经被锁了,请先解锁后使用!")
                return 0
            # 卡没被锁,存钱
            else:
                sql1 = "select money from card where cardId='%s' and cardPwd='%s'" % (cardId, cardPwd)
                cursor.execute(sql1)
                result = cursor.fetchone()
                for row in result:
                    result=row
                    # 加钱
                    result2 = str((int(result) + money))
                    sql = "update card set money=%s where cardId='%s' and cardPwd='%s'" % (result2, cardId, cardPwd)
                    cursor.execute(sql)
                    conn.commit()
                    showinfo(title="存款成功",message='你现在的余额为:'+result2+'元.')
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
