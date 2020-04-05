import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from functools import partial

def plot_corr(corr, my_cmap = "YlGnBu"):
    """Plot heatmap with appropriate size.
    
    Parameters
    ----------
    corr: array-like
    """
    ax = plt.subplots(figsize=(8,8))
    g = sns.heatmap(data = corr, annot = True, cmap=my_cmap)

    g.set_xticklabels(g.get_xticklabels(), rotation = 45)

def plot_corr_multiple(corr1, corr2, my_cmap = "YlGnBu", titles = None):
    
    plotter = partial(sns.heatmap, cmap = my_cmap, annot = True)
    
    f,(ax1, ax2, axcb) = plt.subplots(1,3, 
                gridspec_kw={'width_ratios':[1,1,0.08]}, figsize = (15, 8))
    
    ax1.get_shared_y_axes().join(ax2)
    
    # Left plot has left axis labels
    g1 = plotter(corr1, cbar=False, ax=ax1)
    g1.set_ylabel('')
    g1.set_xlabel('')
    
    # Right plot has colorbar but no left labels
    g2 = plotter(corr2, cbar=True, ax=ax2, cbar_ax=axcb)
    g2.set_ylabel('')
    g2.set_xlabel('')
    g2.set_yticks([])

    # may be needed to rotate the ticklabels correctly:
    for ax in [g1,g2]:
        tl = ax.get_xticklabels()
        ax.set_xticklabels(tl, rotation=90)
        tly = ax.get_yticklabels()
        ax.set_yticklabels(tly, rotation=0)
        
    if titles is not None:
        g1.set_title(titles[0])
        g2.set_title(titles[1])

def plot_corr_cluster(corr):
    """Plot clustermap with annot.
    
    Parameters
    ----------
    corr: array-like
    """
    sns.clustermap(data = corr, annot = True, cmap='viridis')