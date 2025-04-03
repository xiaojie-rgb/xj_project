DEBUG = True
# 秘钥配置
SECRET_KEY = 'your-super-secret-key-here'

# mysql配置(小型)
# MYSQL_HOST = 'localhost'
# MYSQL_USER = 'root'
# MYSQL_PORT = 3306
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'super_interview'
# MYSQL_CURSORCLASS = 'DictCursor'

# Flask-SQLAlchemy配置数据库
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/super_interview'
SQLALCHEMY_TRACK_MODIFICATIONS = False
