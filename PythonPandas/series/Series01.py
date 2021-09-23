import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
index_list = np.arange(1, data.size + 1)
s = pd.Series(data, index=index_list)
print(data)
print(s)

data = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
}
s = pd.Series(data, index=['b','c','d','a'])
print(s)

np_index = np.arange(10)

s = pd.Series(5, index=np_index)
print(s)