import pickle
import pandas 
import numpy 

df=pandas.read_csv('interactions.tsv', sep='\t',index_col=None)
print df