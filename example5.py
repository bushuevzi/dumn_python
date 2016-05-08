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
    car_colors = pd.Series(['Blue', 'Red', 'Green'], dtype='category')
    car_data = pd.Series(
            pd.Categorical(
                ['Blue','Green', 'Red', 'Blue', 'Red'],
                categories=car_colors, ordered=False))
    
    car_colors.cat.categories = ['Purple','Yellow', 'Mauve']
    car_data.cat.categories = car_colors

    print(car_data)


if __name__ == '__main__':
    main()
