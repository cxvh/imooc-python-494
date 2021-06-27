import pandas as pd
from jqdatasdk import *
import time

auth('13282329141', 'qQ123456')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位

# 上海证券交易所	.XSHG	600519.XSHG	贵州茅台
# 深圳证券交易所	.XSHE	000001.XSHE	平安银行

# 获取所有 A股 的行情数据
# stocks = list(get_all_securities(['stock']).index)

# 如何获取股票行情数据（获取平安银行按1分钟为周期以“2015-01-30 14:00:00”为基础前4个时间单位的数据）'000001.XSHE'
# df = get_price(stocks, end_date='2021-06-26 16:00:00',count=10, frequency='minute', fields=['open','close','high','low','volume','money'],panel=False)
# print(df)

# for stock_code in stocks:
#     print('正在获取股票行情数据，股票代码：',stock_code)
#     df = get_price(stock_code, end_date='2021-06-26 16:00:00', count=10, frequency='daily',panel=False)
#     print(df)
#     time.sleep(3)

''' resample函数的使用'''
'''
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',10)

# 转换周期：日K转换为周K
# df = get_price('000001.XSHE',count=10,end_date='2021-06-26', frequency='daily',panel=False) # 获取日K
df = get_price('000001.XSHE',start_date='2020-01-01',end_date='2020-12-31', frequency='daily',panel=False) # 获取日K
df['weekday']=df.index.weekday

# 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）
df_week=pd.DataFrame()
df_week['open']=df['open'].resample('W').first() # 周k W 月k M
df_week['close']=df['close'].resample('W').last()
df_week['high']=df['high'].resample('W').max()
df_week['low']=df['low'].resample('W').min()

# 汇总统计：统计一下月成交量、成交额（sum）
df_week['volume(sum)']=df['volume'].resample('W').sum()
df_week['money(sum)']=df['money'].resample('W').sum()
print(df_week)

'''
'''作业1'''
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',10)

# 转换周期：日K转换为周K
# df = get_price('000001.XSHE',count=10,end_date='2021-06-26', frequency='daily',panel=False) # 获取日K
df = get_price('000001.XSHE',start_date='2021-01-01',end_date='2021-01-31', frequency='daily',panel=False) # 获取日K
df['weekday']=df.index.weekday

print(df)

# 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）
df_week=pd.DataFrame()
df_week['开盘[open]']=df['open'].resample('M').first() # 周k W 月k M
df_week['收盘[close]']=df['close'].resample('M').last()
df_week['最高[high]']=df['high'].resample('M').max()
df_week['最低[low]']=df['low'].resample('M').min()

# 汇总统计：统计一下月成交量、成交额（sum）
df_week['成交量[volume(sum)]']=df['volume'].resample('M').sum()
df_week['成交额[money(sum)]']=df['money'].resample('M').sum()
print(df_week)