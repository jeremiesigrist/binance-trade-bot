from pandas import read_csv
import pandas as pd
#from ta import *
import os

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import csv


def calc_rapports_begin():
    print('======')
    # load the dataset

    ratio_jer_p = {}
    return ratio_jer_p

def calc_rapport(coin_opt_coin_ratio,transaction_fee,multiplier, pair, current_coin, ratio_jer_p):

    ratio_jer = round(((coin_opt_coin_ratio - transaction_fee * multiplier * coin_opt_coin_ratio)-pair.ratio)*100/pair.ratio,1)
    if ratio_jer > -10:
        print('{0}{1}: {2}%'.format(current_coin, pair.to_coin,ratio_jer))
    
    ratio_jer_p[current_coin+pair.to_coin] = ratio_jer
    

def calc_rapports_end(ratio_jer_p, current_coin):
    filename = './exports/ratio_'+str(current_coin)+'.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        df = pd.DataFrame()
    df = df.append(ratio_jer_p, ignore_index=True)
    df.to_csv(filename, index=False)
    renderDF(df,current_coin)

    
def renderDF(df, current_coin):
    fig, ax1 = plt.subplots(figsize=(14,4))
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Ratios', color=color)
    ax1.plot(df)
    ax1.legend(df, loc=6, fontsize=6)
    ax1.grid(b=True,which='major', axis='y', linestyle='--')
    #ax2 = ax1.twinx()
    # Set the limits of the new axis from the original axis limits
    #ax2.set_ylim(ax1.get_ylim())
   
    '''
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('USDT', color=color)  # we already handled the x-label with ax1
    ax2.plot(df.ATOMBAT,color=color)
    '''
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.savefig('./exports/display_ratios_'+str(current_coin)+'.svg')
    plt.close()    
    
    
    
    
