import pandas as pd
import numpy as np

# ============================================================================ #
# Preprocess data

data_df = pd.read_json('data.json')
data_df.index = pd.to_datetime(data_df.index)
data_df = data_df.asfreq('B')

# ============================================================================ #
# Create time series

equity_df = data_df['equity'].copy()
returns_df = data_df['returns'].copy()
prices_df = pd.DataFrame(data_df['prices'].copy())

# ============================================================================ #
# Compute the daily annualized return

number_days = len(data_df.index)
total_return = equity_df.tail(1).values[0]
a_T = np.power((1+total_return), 1.0/(number_days-1)) - 1

# ============================================================================ #
# Build the risk free price series
prices_df['risk_free'] = a_T

prices_df.loc[prices_df.index[0], 'risk_free'] = 0.0
prices_df['risk_free'] = prices_df['risk_free'].add(1.0).cumprod().mul(100)

# ============================================================================ #
# Generate series between the original and the risk free

def space_curves(eps, returns_df, annualized_ret):
    """
    Linear interpolation between the original returns
    and the annualized series.

    Parameters
    ----------
    eps: float

    returns_df: pd.DataFrame

    annualized_ret: float

    Returns
    -------
    pd.DataFrame
    """
    return returns_df * (1-eps) + eps * annualized_ret

space_curves_df = pd.DataFrame()
space_curves_df['original']  = returns_df 
space_curves_df['risk_free'] = a_T

N = 10

for eps in np.linspace(0.0, 1.0, N):
    space_curves_df[eps] = space_curves(eps, returns_df, a_T)

space_curves_df.loc[space_curves_df.index[0], :] = 0.0
space_curves_df = space_curves_df.add(1.0).cumprod().mul(100)