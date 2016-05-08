# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
#import block
########################
import datetime as dt

########################
#def block
########################

########################
#main block
########################
def main():
    now = dt.datetime.now()
    print(str(now))
    print(now.strftime('%a, %d %B %Y'))
    print('\n\n\n')

    timevalue = now +dt.timedelta(hours=3)
    print(now.strftime('%H:%M:%S'))
    print(timevalue.strftime('%H:%M:%S'))
    print(timevalue - now)


if __name__ == '__main__':
    main()
