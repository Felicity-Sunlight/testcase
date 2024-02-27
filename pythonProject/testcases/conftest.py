import pymysql
import pytest


@pytest.fixture(scope="function")
def test_select_mysql():
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='admin',
                         database='TESTDB')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    yield
    # SQL 插入语句
    sql = """select * from students """
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            # 打印结果
            print("id=%s,name=%s,age=%s," % (id, name, age,))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()