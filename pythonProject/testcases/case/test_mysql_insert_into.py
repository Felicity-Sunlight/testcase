#!/usr/bin/python3
import pytest
import pymysql


class TESTInsertDelete:

    # 向数据库插入数据
    def test_mysql_insert_into(self, test_select_mysql):
        # 打开数据库连接
        db = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            database='testdb'
        )

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句
        sql = "INSERT INTO students(id,Name, age) VALUES ('1005','张七','17')"

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

    # 删除插入的数据
    def test_mysql_delete(self, test_select_mysql):
        # 连接数据库
        db = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            database='testdb'
        )

        # 获取游标
        curses = db.cursor()

        # 删除语句
        sql = "DELETE from students where id=1005"
        try:
            # 执行SQL语句
            curses.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭连接
        db.close()

