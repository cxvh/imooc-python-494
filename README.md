---

代码：[https://github.com/cxvh/imooc-python-494/tree/task3.8](https://github.com/cxvh/imooc-python-494/tree/task3.8)

---

摘要
```py
if __name__ == '__main__':
    code_mt='600519.XSHG' # 贵州茅台
    code_pa='000001.XSHE' # 平安银行
    code_pf='600000.XSHG' # 浦发银行
    start_date='2019-01-01'
    end_date='2020-01-01'
    data_mt=week_period_strategy(code_mt, time_freq, start_date, end_date)
    data_pa=week_period_strategy(code_pa, time_freq, start_date, end_date)
    data_pf=week_period_strategy(code_pf, time_freq, start_date, end_date)
    print('-----------------------------------------------------------')
    print('贵州茅台收益率',data_mt.describe()['cum_profit'])
    print('-----------------------------------------------------------')
    print('平安银行收益率',data_pa.describe()['cum_profit'])
    print('-----------------------------------------------------------')
    print('浦发银行收益率',data_pf.describe()['cum_profit'])
    print('-----------------------------------------------------------')
    data_mt['cum_profit'].plot()
    data_pa['cum_profit'].plot()
    data_pf['cum_profit'].plot()
    plt.show()
```

1. 你选取了哪 3 只股票分别是什么？
	- `600519.XSHG`  贵州茅台
	- `000001.XSHE`  平安银行
	- `600000.XSHG`  浦发银行
2. 测算的结果如何，哪一只收益率最高？
	- 贵州茅台最高（蓝色），为：0.589659
```
-----------------------------------------------------------
贵州茅台收益率 count    50.000000
mean      0.390921
std       0.152723
min       0.026259
25%       0.317366
50%       0.418066
75%       0.515513
max       0.589659
Name: cum_profit, dtype: float64
-----------------------------------------------------------
平安银行收益率 count    50.000000
mean      0.276506
std       0.101266
min       0.049107
25%       0.220397
50%       0.264453
75%       0.368012
max       0.440113
Name: cum_profit, dtype: float64
-----------------------------------------------------------
浦发银行收益率 count    50.000000
mean      0.172610
std       0.057650
min       0.017738
25%       0.157398
50%       0.188192
75%       0.205433
max       0.262781
Name: cum_profit, dtype: float64
-----------------------------------------------------------

Process finished with exit code 0

```

---

![收益率](https://img.mukewang.com/szimg/60e202be09f50b7a14211037.jpg)

---