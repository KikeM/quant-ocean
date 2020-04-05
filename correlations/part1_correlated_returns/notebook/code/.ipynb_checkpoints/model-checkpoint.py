import pandas as pd
import numpy as np

def get_cholesky(array):
    """Get cholesky lower triangle matrix. 
    
    Parameters
    ----------
    array: pd.DataFrame or np.array
    
    Returns
    -------
    array
    """
    return np.linalg.cholesky(array)

def generate_random_returns(n_days, symbol_ids = [1], mu = 1e-4, sigma = 1e-2, start = '20010101'):
    """Generate random returns normally distributed.
    
    Parameters
    ----------
    n_days: int
    
    symbol_ids: list
    
    mu: float
    
    sigma: float
    
    start: str, Datetime-like
    
    Returns
    -------
    pd.DataFrame
    """
    n_sids = len(symbol_ids)
    
    returns = mu + sigma * np.random.randn(n_days, n_sids)
    
    # Wrap in Dataframe
    dates = pd.date_range(start = start, freq = 'B', periods=n_days)
    returns_df = pd.DataFrame(data = returns, index = dates, columns=symbol_ids)
    
    return returns_df

def _generate_random_ints(n_sids):
    """Generate a list of random integers.
    
    Parameters
    ----------
    n_sids: int
    
    Returns
    -------
    list
    
    Notes
    -----
    Might contain duplicates.
    """
    symbol_ids = []

    for _ in range(n_sids):

        symbol_ids.append(np.random.randint(low = 1, high = n_sids * 100))
        
    return symbol_ids

def generate_random_symbols(n_sids):
    """Generate unique random symbol ids.
    
    Parameters
    ----------
    n_sids: int
    
    Returns
    -------
    list
    """
    symbol_ids = []

    while len(symbol_ids) != n_sids:

        symbol_ids = _generate_random_ints(n_sids = n_sids)
        symbol_ids = list(set(symbol_ids))
        symbol_ids = sorted(symbol_ids)
        
    return symbol_ids