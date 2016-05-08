# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
#import block
########################
import pandas as pd

########################
#def block
########################

########################
#main block
########################
def main():
    df = pd.DataFrame({'A': [0,0,0,0,0,1,1],
                       'B': [1,2,3,5,4,2,5],
                       'C': [5,3,4,1,1,2,3]})

    a_group_desc = df.groupby('A').describe()
    print(a_group_desc)
    unstacked = a_group_desc.unstack()
    print(unstacked)

    print(unstacked.loc[:,(slice(None), ['count', 'mean']),])


if __name__ == '__main__':
    main()
