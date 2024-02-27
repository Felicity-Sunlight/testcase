# import pymysql
#
#
# def test_mysql_delete():
#     # 连接数据库
#     db = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='admin',
#         database='testdb'
#     )
#
#     # 获取游标
#     curses = db.cursor()
#
#     # 删除语句
#     sql = "DELETE from students where id=1005"
#     try:
#         # 执行SQL语句
#         curses.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭连接
#     db.close()
