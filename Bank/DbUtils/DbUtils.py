from pymysql import *
class DbUtils:
  def getConnection(self):
    return connect(host='localhost', port=3306, user='root', password='wuhuai12',db="bank")


