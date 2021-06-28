import pandas as pd
from jqdatasdk import *
import time
import datetime

auth('13282329141', 'qQ123456')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位

# 上海证券交易所	.XSHG	600519.XSHG	贵州茅台
# 深圳证券交易所	.XSHE	000001.XSHE	平安银行

code='600519.XSHG' # 贵州茅台
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',1000)

'''第一题：使用 Python 计算贵州茅台的最新市值数据，并验证其是否正确。'''
### 方法一：当天市值 = 当天股票收盘价 × 发行总股数
# close 收盘价
# capitalization	总股本(万股)
mt_close = get_price(code,count=1,end_date='2021-06-28', frequency='daily',panel=False)['close'][0]
mt_capitalization=get_fundamentals(
    query(valuation).filter(
        valuation.code.in_([code])
    ),
    date="2021-06-28"
)['capitalization'][0]
df_101=mt_close*mt_capitalization # 计算当天市值
print('第一题：计算当天总市值')
print(df_101)

### 方法二： 直接获取当天总市值
df_102 = get_fundamentals(query(valuation).filter(
    valuation.code == code
), '2021-06-28')['market_cap'][0]

print('第一题：直接获取当天总市值')
print(df_102)

'''第二题：使用 Python 计算贵州茅台的市盈率（静态），并验证其是否正确。'''
### 方法一：市盈率（静态） = 每股股价 / 每股收益
# mt_close 每股股价（收盘价）
# eps 每股收益EPS(元)
mt_close = get_price(code,count=1,end_date='2021-06-28', frequency='daily',panel=False)['close'][0]
mt_eps=get_fundamentals(query(indicator).filter(
    indicator.code == code
),date="2021-06-28")['eps'][0]
df_201=mt_close/mt_eps
print('第二题：市盈率（静态） = 每股股价 / 每股收益')
print(df_201)

### 方法二：市值 / 母公司净利润
# market_cap 市值
# np_parent_company_owners 归属于母公司股东的净利润(元)
mt_market_cap=get_fundamentals(query(valuation).filter(
    valuation.code == code
), '2021-06-28')['market_cap'][0]
mt_income=get_fundamentals(query(income).filter(
    income.code == code
),"2021-06-28")['np_parent_company_owners'][0]
df_202=mt_market_cap/mt_income*100000000
print('第二题：市值 / 母公司净利润')
print(df_202)


'''
参考来源：http://quote.eastmoney.com/sh600519.html?from=BaiduAladdin
打印内容：
第一题：计算当天总市值
264179656.06141204
第一题：直接获取当天总市值
26417.9648
第二题：市盈率（静态） = 每股股价 / 每股收益
189.3153891164424
第二题：市值 / 母公司净利润
189.31554205041547
'''