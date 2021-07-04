#!/usr/bin/env python
# encoding: utf-8

import data.stock as st

# 初始化变量
code='000001.XSHG'

'''

# 调用一只股票的行情数据
data=st.get_single_price(
    code=code,
    time_freq='daily',
    start_date='2021-06-01',
    end_date='2021-07-01'
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

# 试试更新数据

