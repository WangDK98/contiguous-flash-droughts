# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:47:49 2024

@author: 18262
"""


import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature



fdi = xr.open_dataarray('F:/lwdata/ERA-5/4-18(40-20)/fdindex.nc')

labels_out= xr.DataArray(labels_out,dims=['lat','lon','time'],coords=[lat,lon,time])
label_1 = labels_out.sel(lon=slice(90,130),lat=slice(40,20))
a =np.unique(label_1)


lat = fdi['lat'].values
lon = fdi['lon'].values
time = fdi['time'].values

lat_fig = np.where(labels_out ==35484)[0]
lon_fig = np.where(labels_out ==35484)[1]
time_fig = np.where(labels_out ==35484)[2]



data  = np.zeros((361,720),dtype=int)
data = xr.DataArray(data,dims=['lat','lon'],coords=[lat,lon])

for i in range(len(np.where(time_fig==545)[0])):
    print(i)
    data[lat_fig[np.where(time_fig==545)[0][i]],lon_fig[np.where(time_fig==545)[0][i]]]=1
    



#%%    
xticks = np.arange(110, 140, 10)
yticks = np.arange(30, 60.1, 10)

custom_cmap = mcolors.ListedColormap(['white','red'])

proj=ccrs.PlateCarree()
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection=proj)
ax.coastlines(resolution='10m')
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.LAKES)
ax.add_feature(cfeature.BORDERS.with_scale('10m'), linestyle=':')
con = ax.contourf(data['lon'], data['lat'], data,cmap=custom_cmap)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
ax.set_extent([110,135,30,52])
ax.gridlines(xlocs=np.arange(110, 140, 10),ylocs=np.arange(30, 60.1, 10),linestyle='--')
ax.set_title('1987-07-15',fontsize=20)
