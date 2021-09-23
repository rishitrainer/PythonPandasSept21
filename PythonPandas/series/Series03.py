# Series Basic Functionality

import pandas as pd
import numpy as np

#Create a series with 10 random numbers
s = pd.Series(np.random.randn(10))
empty = pd.Series()
print(s)
print("The axes are:")
print(s.axes)
print("The dtype are:")
print(s.dtype)
print ("Is the series Object empty?")
print (s.empty)
print ("Is the empty Object empty?")
print (empty.empty)
print ("The dimensions of the object:")
print (s.ndim)
print ("The size of the object:")
print (s.size)
print ("The actual data series is:")
print (s.values)
print ("The first two rows of the data series:")
print (s.head(2))
print ("The last two rows of the data series:")
print (s.tail(2))
print ("Head with no parameter of the data series:")
print (s.head())
print ("Tail with no parameter of the data series:")
print (s.tail())


