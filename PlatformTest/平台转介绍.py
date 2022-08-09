# coding=utf-8
"""
@author: lishanshan
@time: 2022/02/15 16:32
"""
import pymysql


def is_platform_user(phone:str=''):
    # 打开数据库连接
    db_test = pymysql.connect(host='testdb.61info.com',
                         user='root',
                         password='dbtest',
                         database='i61-bizcenter-usercenter')

    db_pre = pymysql.connect(host='db.preprod.61draw.com',
                                                   user='root',
                                                   password='dbtest',
                                                   database='i61-bizcenter-usercenter')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_test.cursor()


    sql = "SELECT ID,create_time from u_platform_user where mobile='%s'" % (phone)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            print('手机号：'+str(phone)+'，平台用户ID是：'+str(results[0][0])+'，注册时间：'+str(results[0][1]))
            return results[0][0]
        else:
            print('未注册平台')
            return None
    except:
        print("Error: unable to fetch data")

    db_test.close()


def has_relation_or_pre(phone:str=''):
    # 打开数据库连接
    platformId=is_platform_user(phone)
    if platformId is None:
        print('用户未注册')
        return
    db_test = pymysql.connect(host='testdb.61info.com',
                         user='root',
                         password='dbtest',
                         database='i61-bizcenter-marketing-activity')

    db_pre= pymysql.connect(host='db.preprod.61draw.com',
                              user='root',
                              password='dbtest',
                              database='i61-bizcenter-marketing-activity')

    cursor = db_test.cursor()
    sql_pre = "SELECT * from ma_fission_invite_rel_pre where invitee_id ='%s'" % (platformId)
    try:
        # 执行SQL语句
        cursor.execute(sql_pre)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            for row in results:
                inviter=row[1]
                invitee=row[2]
                start=row[5]
                end=row[6]
                print('平台邀请人：{}，预绑定时间：{} ~ {} \r\n'.format(inviter,start,end))
        else:
            print('作为被邀请人，无预绑定关系')
    except:
        print("Error: unable to fetch data")

    sql = "SELECT * from ma_fission_invite_rel where invitee_id  ='%s'" % (platformId)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            for row in results:
                inviter=row[1]
                xueke=row[8]
                configId=row[5]
                kemu=row[9]
                time=row[10]
                print('学科绑定邀请人：{}，学科：{}，科目：{}，配置ID：{}，绑定创建时间：{}'.format(inviter,xueke,kemu,configId,time))
                # print(row)
            print()
        else:
            print('作为被邀请人，无平台学科绑定关系')
    except:
        print("Error: unable to fetch data")



    db2 = pymysql.connect(
        host='testdb.61info.com', #查询用户是否已经有平台订单
        # host='db.preprod.61draw.com', #查询用户是否已经有平台订单
                         user='root',
                         password='dbtest',
                         database='i61-bizcenter-order')

    cursor2 = db2.cursor()
    sql_order = "SELECT order_id ,place_order_time ,finish_form_time ,has_finish_form ,title ,main_goods_id FROM o_order where user_id ={}".format(platformId)
    try:
        # 执行SQL语句
        cursor2.execute(sql_order)
        # 获取所有记录列表
        results = cursor2.fetchall()
        # print(results)
        if len(results) > 0:
            for row in results:
                order_id = row[0]
                place_order_time = row[1]
                finish_form_time = row[2]
                has_finish_form = row[3]
                title = row[4]
                main_goods_id = row[5]

                print('订单号：{}，下单时间：{}，表格提交时间：{}，已完成表格提交：{}，商品名称：{}，主商品ID：{}'.format(order_id,place_order_time,finish_form_time,has_finish_form,title,main_goods_id))
        else:
            print('在平台尚无订单')
    except:
        print("Error: unable to fetch data")

    db_test.close()
if __name__ == '__main__':

    from 平台任务 import check_mission
    # 邀请人
    # phone='18928250018'
    # has_relation_or_pre(phone)
    # check_mission(phone)
    # 邀请人1
    phone = '18928250027'
    has_relation_or_pre(phone)
    check_mission(phone)
    phone = '18928250033'
    has_relation_or_pre(phone)