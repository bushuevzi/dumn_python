# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
#import block
########################
from lxml import objectify
import pandas as pd

########################
#def block
########################

########################
#main block
########################
def main():
    xml = objectify.parse(open('../XMLData2.xml'))
    root = xml.getroot()
    df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))
    for i in range(0, len(root.getchildren())):
        obj = root.getchildren()[i].getchildren()
        row = dict(zip(['Number', 'String', 'Boolean'],
                        [obj[0].text, obj[1].text, obj[2].text]))
        row_s = pd.Series(row)
        row_s.name = i
        df = df.append(row_s)
    print(df.drop_duplicates())
	 


if __name__ == '__main__':
    main()
