import pandas as pd

s = pd.Series([10,20,30,40,50],index = ['a','b','c','d','e'])
print(s['a'])
print(s[1])
print(s[0:2])
print(s[2:])
print(s[:4])
print(s[-2:])
print(s[['a', 'e', 'c']])
print(s['f'])