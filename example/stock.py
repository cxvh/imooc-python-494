import data.stock as st

# 初始化变量
code='000001.XSHE'

# 获取平安银行的行情数据（日 K）
data=st.get_single_price(code,'daily','2020-06-01','2020-07-01')
print(data)

# # 计算涨跌幅，验证准确性
# data=st.calculate_change_pct(data)
# print(data) # 多了一列 close_pct

# 获取周 K
data=st.transfer_price_freq(data,'w')
print(data)

# 计算涨跌幅，验证准确性
data=st.calculate_change_pct(data)
print(data) # 多了一列 close_pct
