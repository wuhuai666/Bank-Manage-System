import random

from Bank.DbUtils.DbUtils import *
class CreateUsers:
    def __init__(self,username,IdCard,phoneNumber,savaMoney,password,repwd):
         self.username=username
         self.IdCard=IdCard
         self.phoneNumber=phoneNumber
         self.saveMoney=savaMoney
         self.password=password
         self.repwd=repwd
    def randomiCardId(self):
        # 随机生成卡号
        cardId = ""
        while True:
            num = str(random.randint(0, 9))
            cardId += num
            if len(cardId) == 6:
                break;
        return cardId

    def creatUser(self):
        name = self.username
        number =self.IdCard
        phone = self.phoneNumber
        money =self.saveMoney
        password = self.password
        rPassword=self.repwd
        card = CreateUsers.randomiCardId(self)
        conn = DbUtils.getConnection(self)
        cursor = conn.cursor()
        sql = "insert into users values(%d,'%s','%s','%s','%s')" % (0, name, number, phone, card)
        cursor.execute(sql)
        conn.commit()
        sql1 = "insert into card(cardId,cardPwd,money) values('%s','%s','%s')" % (card, password, money)
        cursor.execute(sql1)
        conn.commit()
        cursor.close
        conn.close()
        return card



