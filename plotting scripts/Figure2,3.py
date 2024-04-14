# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:41:00 2024

@author: 18262
"""

import glob
import xarray as xr
import dask
import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np
import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib import gridspec
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cc3d
import seaborn as sns
from geopy.distance import geodesic
import math
from math import sin, asin, cos, radians, fabs, sqrt, pi, atan2
import cartopy.feature as cfeature
from scipy import stats
import matplotlib.colors as mcolors
from matplotlib import patches
from PIL import Image


#%%fig2

for i in range(len(centroid_total)):
    lon_fig.append(centroid_total[i][1])
    lat_fig.append(centroid_total[i][0])


df = pd.DataFrame([lon_fig, lat_fig, accum_area, max_intensity]).T
df.columns = ['lon','lat','area','max_intensity']

color_climate= ['#FA9B58','#FECE7C','#FFF5AE','#FBFAE6','#B9E176','#96D268','#69BE63','#33A456','#108647']

bins = [500000,750000,900000,1050000,1200000,1500000,20000000]  
labels=['5','20','40','60','80','100'] 
df['area']=pd.cut(df['area'], bins=bins,labels=labels).astype(float)

df['lon'] = np.where(df['lon']>180,df['lon']-360,df['lon'])


xticks = np.arange(-180, 180.1, 90)
yticks = np.arange(-90, 90.1, 30)
custom_cmap = mcolors.ListedColormap(['#FF4500','#FA9B58','#FECE7C','#FFF5AE','#FBFAE6','#B9E176','#96D268','#69BE63','#33A456'])

proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111,projection=proj)
ax.coastlines(resolution='50m')
ax.set_extent([-180,180,90,-60])
ax.set_title('Spatial distribution of flash drought events globally')
scatter = ax.scatter(df['lon'], df['lat'], marker='o',c=df['max_intensity'],linewidths=1, s=df['area'], cmap=custom_cmap)
ax.add_feature(cfeature.LAND, linewidth=0.01, facecolor='white')
ax.coastlines()
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
ax.gridlines(xlocs=np.arange(-180, 180, 90),ylocs=np.arange(-60, 91, 30),linestyle='--')
ax.set_ylim(-60,90)
cbar = plt.colorbar(scatter,orientation='horizontal',pad=0.03,aspect=20,shrink=0.5)
cbar.ax.set_ylabel('Intensity',rotation=0,labelpad =30)

NA= patches.Rectangle((-105, 32),40,25, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)  #-170 -50  25-70
NA= patches.Rectangle((-82, -10),25,17, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((-65, -35),23,17, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((7, -5),30,10, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((-5, 40),40,33, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((40, 53),60,16, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((68, 6),20,30, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((100, 22),22,15, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((93, -10),62,18, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)

plt.show()



#%%fig3
xticks = np.arange(-180, 180.1, 90)
yticks = np.arange(-90, 90.1, 30)

proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111,projection=proj)
ax.coastlines(resolution='50m')
ax.set_title('Movement of flash drought')
ax.set_extent([0,360,90,-60])
for i in range(len(df)):
    if  df['end_lat'][i]-df['start_lat'][i]>0:
        plt.arrow(df['start_lon'][i], df['start_lat'][i], df['end_lon'][i]-df['start_lon'][i], df['end_lat'][i]-df['start_lat'][i], width=0.1,
              head_width=1,head_length=1,length_includes_head=True,color='r')
    else:
        plt.arrow(df['start_lon'][i], df['start_lat'][i], df['end_lon'][i]-df['start_lon'][i], df['end_lat'][i]-df['start_lat'][i], width=0.1,
              head_width=1,head_length=1,length_includes_head=True,color='b')
ax.gridlines(xlocs=np.arange(-180, 180, 90),ylocs=np.arange(-60, 91, 30),linestyle='--')
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
ax.set_ylim(-60,90)
NA= patches.Rectangle((-105, 32),40,25, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)  #-170 -50  25-70
NA= patches.Rectangle((-82, -10),25,17, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((-65, -35),23,17, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((7, -5),30,10, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((-5, 40),40,33, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((40, 53),60,16, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((68, 6),20,30, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((100, 22),22,15, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)
NA= patches.Rectangle((93, -10),62,18, linewidth=2, linestyle='-',zorder=4, edgecolor='#1663A9',facecolor='none', transform=ccrs.PlateCarree())
ax.add_patch(NA)