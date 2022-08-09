# coding=utf-8
"""
@author: lishanshan
@time: 2022/02/22 11:25
"""
import pymysql

from get_platformId_by_mobile import is_platform_user


def check_mission(phone):
    platformId = is_platform_user(phone)
    db = pymysql.connect(
        host='testdb.61info.com',
        # host='db.preprod.61draw.com',
        user='root',
        password='dbtest',
        database='i61-bizcenter-marketing-activity')

    cursor = db.cursor()

    if not platformId:
        print('手机号未在平台注册')
        return

    sql_reward = "SELECT  biz_type,biz_id ,reward_type ,reward_value,state ,retry_num ,reward_title ,finish_time , gmt_create ,gmt_update FROM `i61-bizcenter-marketing-activity`.ma_reward_record where user_id ='{}'  order by gmt_create desc".format(        platformId)
    cursor.execute(sql_reward)
    data_reward = cursor.fetchall()
    if data_reward:
        print('**********************************************奖励记录**********************************************',
              end='\r\n')
        for reward in data_reward:
            (biz_type, biz_id, reward_type, reward_value, state, retry_num, reward_title, finish_time, gmt_create,
             gmt_update) = reward[:]
            print('\t活动ID：{}，奖励类型：{}，value:{}，发放状态：{}，发放时间:{}，奖励标题：{}，奖励类型：【{}】'.
                  format( biz_id, reward_type, reward_value, state, finish_time,reward_title,reward_type))
        print('**********************************************查询完毕**********************************************',
              end='\r\n')
    else:
        print('无【奖励发放】记录')

    sql_record = 'SELECT id, biz_channel_code, user_id, activity_config_id, activity_id, trigger_num, finish_time, status, gmt_create, gmt_update FROM ma_activity_participate_record where user_id ={} order by gmt_create desc'.format(
        platformId)
    cursor.execute(sql_record)
    data = cursor.fetchall()
    if data:
        print('**********************************************【任务参与】记录**********************************************',
              end='\r\n')
        for one in data:
            biz_channel_code = one[1]
            user_id = one[2]
            activity_config_id = one[3]
            activity_id = one[4]
            trigger_num = one[5]
            finish_time = one[6]
            status = one[7]
            status_dic = {1: "待完成", 2: "等待完成(等待完成事件触发)", 3: "已完成", 10: "已过期", 11: "已取消"}
            gmt_create = one[8]
            print("\t所属方：{}，用户ID：{}，任务配置ID：{}，任务ID：{}, 触发次数：{}，活动完成时间：{}，状态：{}".
                  format(biz_channel_code, user_id, activity_config_id, activity_id, trigger_num, finish_time,
                         status_dic[status]))
    else:
        print('无任务参与记录')

    cursor.close()
    db.cursor()


if __name__ == '__main__':
    check_mission('18925256632')
