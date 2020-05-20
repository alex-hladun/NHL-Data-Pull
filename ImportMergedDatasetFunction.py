import pickle
import pandas as pd
from ArrayFunction import gamearray
from CleanTimeFunction import cleantimeanddate
from NHLOddsMergerFunction import NHLoddsmerger


def importmergeddataset(url, DSTdate, Excelfilepath, importfilename):
    df1 = gamearray(url)
    df1 = cleantimeanddate(df1, DSTdate)
    df1 = NHLoddsmerger(df1, Excelfilepath)
    outfile = open(importfilename, 'wb')
    pickle.dump(df1, outfile)
    outfile.close()
