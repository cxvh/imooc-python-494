import pandas as pd
from jqdatasdk import *
import time

auth('13282329141', 'qQ123456')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位

# 上海证券交易所	.XSHG	600519.XSHG	贵州茅台
# 深圳证券交易所	.XSHE	000001.XSHE	平安银行

# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',1000)

# 初始化环境变量
data_root='e:/learn/imooc/python/pythonProject/data/'

def get_stock_list():
    """
    获取所有A股股票列表
    :return:
    """
    stock_list=list(get_all_securities(['stock']).index)
    return stock_list

def get_single_price(code,time_freq,start_date,end_date):
    """
    获取单个股票行情数据
    :param code:
    :param time_freq:
    :param start_date:
    :param end_date:
    :return:
    """
    data = get_price(code, start_date=start_date,end_date=end_date, frequency=time_freq,panel=False)
    return data

def export_data(data,filename,type,mode='w'):
    """
    导出股票相关数据
    :param data: 
    :param filename: 
    :param type: 股票数据类型，可以是->price、finance
    :param mode: 默认w->只能写入，a->追加
    :return: 
    """
    file_root=data_root+type+'/'+filename+'.csv'
    data.index.names=['date']
    header=True
    if mode=='a':
        header=False
    data.to_csv(file_root,mode=mode,header=header)
    print('已经成功存储至：',file_root)

def get_csv_data(code,type):
    """
    :param code:
    :param type:
    :return:
    """
    file_root=data_root+type+'/'+code+'.csv'
    return pd.read_csv(file_root)

def transfer_price_freq(data,time_freq):
    """
    转换股票行情周期：开盘价（周期第一天）、收盘价（周期最后一天）、最高价（周期内）、最低价（周期内）
    :param data:
    :param time_freq:
    :return:
    """
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()  # 周k W 月k M
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()
    return df_trans

def get_single_finance(code,date,statDate):
    """
    获取单个股票财务指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(indicator).filter(valuation.code == code),date=date,statDate=statDate)  # 获取财务指标数据 bank_indicator（银行业）security_indicator（券商）insurance_indicator（保险）
    return data

def get_single_finance(code,date,statDate):
    """
    获取单个股票估值指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date,statDate=statDate)
    return data


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

'''2-10 【作业】使用财务数据计算估值指标-简答题'''
'''
code='600519.XSHG' # 贵州茅台
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',1000)

###### 第一题：使用 Python 计算贵州茅台的最新市值数据，并验证其是否正确。
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

###### 第二题：使用 Python 计算贵州茅台的市盈率（静态），并验证其是否正确。
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


'''实时更新股票数据'''
