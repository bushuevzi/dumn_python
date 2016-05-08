# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
#import block
########################
import pandas as pd
import numpy as np

########################
#def block
########################

########################
#main block
########################
def main():
    s = pd.Series([1,2,3,np.NaN,5,6,None])
    print(s.isnull())
    print()
    print(s[s.isnull()])


if __name__ == '__main__':
    main()
