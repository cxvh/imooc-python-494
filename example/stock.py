#!/usr/bin/env python
# encoding: utf-8

import data.stock as st
import time

# 初始化变量
code='000001.XSHG'
start_date='2021-07-01'
oneday_time=24*60*60

'''
# 调用一只股票的行情数据
data=st.get_single_price(
    code=code,
    time_freq='daily',
    start_date='2021-06-01',
    end_date='2021-06-10'
)

# 存入 csv
st.export_data(
    data=data,
    filename=code,
    type='price'
)

# 从 csv 中获取数据
data=st.get_csv_data(code=code,type='price')
print(data)
'''

# 本章小结：实时更新数据
# 将所有股票列表转换成数组，测试取5条
stock_list=st.get_stock_list() #[:5]

def timer():
    # 获取当前日期
    now_date=time.strftime('%Y-%m-%d')
    # 获取当前时间戳
    now_strptime=int(time.time())
    # 计算今天收盘时间戳
    close_strptime = int(time.mktime(time.strptime(now_date+' 16:00:00', "%Y-%m-%d %H:%M:%S")))

    # 计算昨天时间戳
    yesterday_strptime = int(time.mktime(time.strptime(now_date, "%Y-%m-%d")))-oneday_time
    # 昨天时间戳转换为日期
    yesterday_date=time.strftime('%Y-%m-%d',time.localtime(yesterday_strptime))

    # 计算明天时间戳
    tomorrow_strptime = int(time.mktime(time.strptime(now_date, "%Y-%m-%d")))+oneday_time
    # 明天时间戳转换为日期
    tomorrow_date=time.strftime('%Y-%m-%d',time.localtime(tomorrow_strptime))

    # 获取现在到明天凌晨的秒数
    sleep_time=tomorrow_strptime-now_strptime
    # 获取现在到收盘的秒数
    close_time=close_strptime-now_strptime
    # 判断当前时间是否收盘
    # 当前时间：未收盘=>结束日期为昨天
    # 当前时间：已收盘=>结束日期为今天
    end_date=now_date
    if close_time>0:
        sleep_time=close_time
        end_date=yesterday_strptime
    for code in stock_list:
        try:
            data=st.get_csv_data(code=code,type='price')
            # 获取最后一天的明天日期、并转换为时间戳
            last_tomorrow_date=time.mktime(time.strptime(data.date[data.date.size - 1],'%Y-%m-%d'))+oneday_time
            # 时间戳转换为日期
            tomorrow_date=time.strftime('%Y-%m-%d',time.localtime(last_tomorrow_date))
            print(tomorrow_date)
            data = st.get_single_price(
                code=code,
                time_freq='daily',
                start_date=tomorrow_date,
                end_date=end_date
            )
            st.export_data(
                data=data,
                filename=code,
                type='price',
                mode='a'
            )
        except Exception as err:
            print('error：',err)
            # start_date='2021-06-29'
            # end_date='2021-06-30'
            data = st.get_single_price(
                code=code,
                time_freq='daily',
                start_date=start_date,
                end_date=end_date
            )
            st.export_data(
                data=data,
                filename=code,
                type='price'
            )
        # time.sleep(2)
    return sleep_time;

while True:
    sleep_time=timer()
    time.sleep(sleep_time)
    
