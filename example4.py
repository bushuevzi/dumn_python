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
    car_colors = pd.Series(['Blue', 'Red', 'Green'],dtype='category')
    car_data = pd.Series(
            pd.Categorical(['Yellow', 'Green', 'Red', 'Blue', 'Purple'],
                categories=car_colors, ordered = False))
    find_entries = pd.isnull(car_data)

    print(car_colors)
    print()
    #for i in range(0,4):
    print(car_data)
    print()
    print(find_entries)
    print(find_entries[find_entries == True])


if __name__ == '__main__':
    main()
