import boa
import matplotlib.pyplot as plt
import pandas as pd

import ujson

N = 1200
gen = boa.conventions.tseries.DataGenerator(
    n_periods=[N], nans_per_col=[0], col_nans=[0], date_init="20010101"
)
prices_df = gen.sequential_order(n=1)[0]
prices_df = prices_df.rename(columns = {0:'ts'})
prices_df.index.name = 'date'

returns_df = prices_df.p2r()
equity_df  = prices_df.p2c()

payload = pd.DataFrame()
payload['prices']  = prices_df['ts']
payload['returns'] = returns_df['ts']
payload['equity']  = equity_df['ts']

payload.to_json('data.json')

