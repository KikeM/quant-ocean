import pandas as pd
import numpy as np
from itertools import combinations

def generate_correlation_matrix(symbol_ids, params):
    """Generate random correlation matrix with given structure.

    Parameters
    ----------
    symbol_ids: list of int

    params: dict
    
    Returns
    -------
    corr_df: pd.DataFrame
    """
    high  = params['rho_high']
    low   = params['rho_low']
    sigma = params['rho_sigma']

    # Create initial correlation matrix
    corr_df = pd.DataFrame(data    = 1.0, 
                           index   = symbol_ids, 
                           columns = symbol_ids)

    symbols_selected = []
    
    for _symbol1, _symbol2 in combinations(symbol_ids, 2):

        # Generate acceptable correlation within bounds
        rho = 5 # Impossible correlation to start iteration
        while ~belongs_to_interval(rho, low, high):

            rho = generate_random_float(sigma)

        # Save correlation and make symmetric
        corr_df.loc[_symbol1, _symbol2] = rho    
        corr_df.loc[_symbol2, _symbol1] = rho

    return corr_df

def generate_random_float(sigma = 1):
    """Generate random float with zero mean.
    
    Parameters
    ----------
    sigma: float
    
    Returns
    -------
    float
    """
    return sigma * np.random.randn(1)[0]

def belongs_to_interval(rho, low, high):
    """Check if |rho| belongs to [low, high] interval.
    
    Parameters
    ----------
    rho, low, high: float
    
    Returns
    -------
    bool
    """
    rho = np.abs(rho)
    greater = rho > low
    smaller = rho < high
    
    return greater & smaller

def is_pos_def(x):
    """Check if symmetric matrix is semi-positive definite. 
    
    Parameters
    ----------
    x: array
    
    Notes
    -----
    Only valid for symmetric matrices.
    """
    return np.all(np.linalg.eigvals(x) >= 0)