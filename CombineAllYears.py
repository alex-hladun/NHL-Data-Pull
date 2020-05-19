from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle


def openfile(filename):
    infile = open(filename, 'rb')
    df1 = pickle.load(infile)
    infile.close()
    return df1


df07 = openfile('2007-08dataset')
df08 = openfile('2008-09dataset')
df09 = openfile('2009-10dataset')
df10 = openfile('2010-11dataset')
df11 = openfile('2011-12dataset')
df12 = openfile('2012-13dataset')
df13 = openfile('2013-14dataset')
df14 = openfile('2014-15dataset')
df15 = openfile('2015-16dataset')
df16 = openfile('2016-17dataset')
df17 = openfile('2017-18dataset')
df18 = openfile('2018-19dataset')
df19 = openfile('2019-20dataset')
df_allyears = [df07, df08, df09, df10, df11, df12, df13, df14, df15,
               df16, df17, df18, df19]
outfile = open("2007-20dataset", 'wb')
pickle.dump(df_allyears, outfile)
outfile.close()
