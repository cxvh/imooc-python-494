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
'''
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
df_week['开盘']=df['open'].resample('M').first() # open 周k W 月k M
df_week['收盘']=df['close'].resample('M').last() # close
df_week['最高']=df['high'].resample('M').max() # high
df_week['最低']=df['low'].resample('M').min() # low

# 汇总统计：统计一下月成交量、成交额（sum）
df_week['成交量']=df['volume'].resample('M').sum() # volume(sum)
df_week['成交额']=df['money'].resample('M').sum() # money(sum)
print(df_week)
'''

'''作业2'''
'''
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',10)

# 转换周期：日K转换为周K
# df = get_price('000001.XSHE',count=10,end_date='2021-06-26', frequency='daily',panel=False) # 获取日K
df = get_price('000001.XSHE',start_date='2020-01-01',end_date='2020-12-31', frequency='daily',panel=False) # 获取日K
df['weekday']=df.index.weekday

print(df)

# 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）
df_week=pd.DataFrame()
df_week['开盘']=df['open'].resample('M').first() # open 周k W 月k M
df_week['收盘']=df['close'].resample('M').last() # close
df_week['最高']=df['high'].resample('M').max() # high
df_week['最低']=df['low'].resample('M').min() # low

# 汇总统计：统计一下月成交量、成交额（sum）
df_week['成交量']=df['volume'].resample('M').sum() # volume(sum)
df_week['成交额']=df['money'].resample('M').sum() # money(sum)
print(df_week)
'''

'''使用JQData查询财务指标'''
'''
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',1000)

# df=get_fundamentals(query(bank_indicator),statDate=2020)[:5] # 限制数据 5 条
df=get_fundamentals(query(indicator),statDate=2020) # 获取财务指标数据 bank_indicator（银行业）security_indicator（券商）insurance_indicator（保险）

# print(df[['code','pubDate','statDate','total_loan']])

# df.to_csv('e:/learn/imooc/python/pythonProject/data/finance/finance2020.csv') # 存储数据

# 基于盈利指标选股：eps、operating_profit、roe、inc_net_profit_year_on_year
df=df[
        # (df['eps']>0) & # 下面三个是平均值
        # (df['operating_profit']>944280248.1) &
        # (df['roe']>4.550607029) &
        # (df['inc_net_profit_year_on_year']>-166.13775)

        (df['eps'] > 0) &
        (df['operating_profit'] > 1044280248) &
        (df['roe'] > 10) &
        (df['inc_net_profit_year_on_year'] > 10)
    ]
print(df)
'''

'''使用JQData查询估值指标'''
'''
# df=get_fundamentals(query(valuation),statDate=datetime.datetime.today()) # valuation 估值数据
df_valuation=get_fundamentals(query(valuation),statDate=2020) # valuation 估值数据
df_valuation.index=df_valuation['code']
df['pe_ratio']=df_valuation['pe_ratio']
df=df[df['pe_ratio']<50]
print(df)
'''

