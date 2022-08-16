import numpy as np
from scipy.interpolate import LinearNDInterpolator, interp1d

lats = np.arange(-90,90.5,0.5)
lons = np.arange(-180,180,0.5)
alts = np.arange(1,1000,21.717)
time = np.arange(8)
data = np.random.rand(len(lats)*len(lons)*len(alts)*len(time)).reshape((len(lats),len(lons),len(alts),len(time)))

interpolatedData = np.array([None, None, None, None])
interpolatedData[0] = interp1d(lats,data,axis=0)
interpolatedData[1] = interp1d(lons,data,axis=1)
interpolatedData[2] = interp1d(alts,data,axis=2)
interpolatedData[3] = interp1d(time,data,axis=3)
