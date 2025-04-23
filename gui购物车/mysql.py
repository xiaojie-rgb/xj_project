import pymysql

# 建立数据库连接
def connection():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='shopping',
            charset='utf8'
        )
        return conn
    except pymysql.Error as e:
        print(f"数据库连接错误: {e}")
        return None
