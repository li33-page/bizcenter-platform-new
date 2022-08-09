# coding=utf-8
"""
@author: lishanshan
@time: 2022/02/22 11:25
"""
import pymysql


def is_platform_user(phone:str=''):
    # 打开数据库连接
    db = pymysql.connect(host='testdb.61info.com',
    # db = pymysql.connect(host='db.preprod.61draw.com',
                         user='root',
                         password='dbtest',
                         database='i61-bizcenter-usercenter')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT ID,create_time from u_platform_user where mobile='%s' and tel_code='86' " % (phone)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        cursor.close()
        if len(results) > 0:
            print('手机号'+str(phone)+'，平台用户ID：'+str(results[0][0])+'，注册时间：'+str(results[0][1]))
            return results[0][0]
        else:
            print('未注册平台')
            return None
    except:
        print("Error: unable to fetch data")

    db.close()