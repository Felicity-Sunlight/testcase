# #!/usr/bin/python3
#
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='admin',
#                      database='TESTDB')
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 更新语句
# sql = "UPDATE students SET name = '张六' where id=1004;"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()