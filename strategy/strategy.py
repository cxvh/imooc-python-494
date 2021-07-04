# 用来创建交易策略、生成交易信号
import data.stock as st
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# 初始化变量
code='000001.XSHE'
time_freq='daily'
start_date='2020-01-01'
start_date=None
end_date='2020-03-01'
end_date=datetime.date.today()

def compose_singal(data):
    # 整合信号
    data['buy_signal']=np.where((data['buy_signal']==1) & (data['buy_signal'].shift(1)==1),0,data['buy_signal'])
    data['sell_signal']=np.where((data['sell_signal']==-1) & (data['sell_signal'].shift(1)==-1),0,data['sell_signal'])
    data['signal']=data['buy_signal']+data['sell_signal']
    return data

def calculate_prof_pct(data):
    # 计算单次收益率：开仓、平仓（开仓的全部股数）
    data=data[data['signal'] != 0] # 筛选
    data['profit_pct'] = (data['close']-data['close'].shift(1))/data['close'].shift(1) # 当前数的上一个数
    data=data[data['signal']==-1]
    return data

def calculate_cum_prof(data):
    """
    计算累计收益率
    :param data: dataframe
    :return:
    """
    data['cum_profit']=pd.DataFrame((1+data['profit_pct'])).cumprod()-1
    return data

def week_period_strategy(code,time_freq,start_date,end_date):
    data=st.get_single_price(code,time_freq,start_date,end_date)
    # 新建周期字段
    data['weekday']=data.index.weekday
    # 周四买入
    data['buy_signal']=np.where((data['weekday']==3),1,0) # [1,2,3,4,5,6][index]===3?1:0
    # 周一卖出
    data['sell_signal']=np.where((data['weekday']==0),-1,0) # [1,2,3,4,5,6][index]===3?1:0
    # # 模拟重复买入：周五再次买入
    # data['buy_signal']=np.where((data['weekday']==3) | (data['weekday']==4),1,0)
    # 模拟重复卖出：周二再次卖出
    # data['sell_signal']=np.where((data['weekday']==0) | (data['weekday']==1),-1,0)

    # # 整合信号
    # data['buy_signal']=np.where((data['buy_signal']==1) & (data['buy_signal'].shift(1)==1),0,data['buy_signal'])
    # data['sell_signal']=np.where((data['sell_signal']==-1) & (data['sell_signal'].shift(1)==-1),0,data['sell_signal'])
    # data['signal']=data['buy_signal']+data['sell_signal']
    data=compose_singal(data)

    # 计算单次收益率：开仓、平仓（开仓的全部股数）
    # data=data[data['signal'] != 0] # 筛选
    # data['profit_pct'] = (data['close']-data['close'].shift(1))/data['close'].shift(1) # 当前数的上一个数
    # data=data[data['signal']==-1]
    data=calculate_prof_pct(data)

    data=calculate_cum_prof(data) # 计算累计收益率

    return data;

if __name__ == '__main__':
    df=week_period_strategy(code,time_freq,start_date,end_date)
    print(df)
    print('-----------------------------------------------------------')
    print(df.describe())
    print('-----------------------------------------------------------')
    # df['profit_pct'].plot()
    df['cum_profit'].plot() # 收益率
    plt.show()
