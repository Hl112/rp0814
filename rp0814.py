import random
import pandas as pd
import numpy as np

from scipy.interpolate import griddata
from scipy.interpolate import LinearNDInterpolator

# dataset
filename = '051.csv'

# Sampling data
# n = sum(1 for line in open(filename)) - 1  # number of lines in the file
# s = n // 1  # sample size 10%
# skip = sorted(random.sample(range(1, n + 1), n - s))  # skip lines in the file, n + 1 to compensate for header
# columns = ['lat', 'lon', 'alt']  # columns in the file
df = pd.read_csv(filename)
df.head()

df.describe()

# choose data
df_lon, df_lat, df_alt = (df['lon'].values,
                          df['lat'].values,
                          df['alt'].values)

points = np.stack((df_lon, df_lat, df_alt), axis=1) 
# and put the moisture corresponding data values in a separate array:
values = np.array([0.205, 0.197, 0.204, 0.197, 0.212,
                   0.208, 0.204, 0.205, 0.211, 0.215])
# Finally, put the desired point/points you want to interpolate over
request = np.array([[25, 20, -30], [27, 20, -32]])
#
print(griddata(points, values, request))

# First, define an interpolator function
linInter = LinearNDInterpolator(points, values)

# Then, apply the function to one or more points
print(linInter(np.array([[25, 20, -30]])))
# print(linInter(request))
# OUTPUT: [0.20448536  0.20782028]
# I think you may use it with python map or pandas.apply as well
