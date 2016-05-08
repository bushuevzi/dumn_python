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
from sklearn.preprocessing import Imputer

########################
#def block
########################

########################
#main block
########################
def main():
   s = pd.Series([1,2,3,np.NaN,5,6,None])
   imp = Imputer(missing_values='NaN',
                strategy='mean', axis=0)
   imp.fit([1,2,3,4,5,6,7])

   x = pd.Series(imp.transform(s).tolist()[0])
   
   print(x)


if __name__ == '__main__':
    main()
