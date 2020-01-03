#!/usr/bin/env python3
import os
import pymysql
from DBUtils.PooledDB import PooledDB
from influxdb import InfluxDBClient


# Tornado app配置
settings = {
    # 'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    # 'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    'login_url': '/login',
    'debug': True,
}


# --------------------------------------mysqlDB----------------------------
# mysql数据库名 'iot_manage'
mysql_db_name = "tornado_db_test"

# mysql基本配置、连接
mysql_db_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "mysql",
        "database": mysql_db_name
}
# mysql连接池
spool = PooledDB(creator=pymysql, maxconnections=1000, blocking=True, **mysql_db_config)
mysql_db_client = spool.connection()


PooledDB 的参数：

POOL = PooledDB(
creator=pymysql, # 使用链接数据库的模块
maxconnections=6, # 连接池允许的最大连接数，0和None表示不限制连接数
mincached=2, # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
maxcached=5, # 链接池中最多闲置的链接，0和None不限制
maxshared=1, # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
blocking=True, # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
maxusage=None, # 一个链接最多被重复使用的次数，None表示无限制
setsession=[], # 开始会话前执行的命令列表。如：[“set datestyle to …”, “set time zone …”]
ping=0,
