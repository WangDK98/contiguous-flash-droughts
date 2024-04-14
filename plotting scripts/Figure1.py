# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:37:58 2024

@author: 18262
"""


import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from matplotlib import patches



#%%
number= fdi.sum(dim='time')/len(time)

xticks = np.arange(-180, 180.1, 90)
yticks = np.arange(-90, 90.1, 30)

number_2 = np.where(number, number, np.nan) 

plt.rcParams["font.family"] = "Times New Roman"
proj=ccrs.PlateCarree()
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection=proj)
ax.tick_params(axis='both',labelsize=20)
ax.coastlines(resolution='110m')
con = ax.contourf(number['lon'], number['lat'], number_2, cmap='Reds',levels=np.arange(0,0.18,0.02))
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
ax.set_ylim(-60,90)
cbar = plt.colorbar(con,orientation='horizontal',pad=0.03,aspect=20,shrink=0.6,extend='both')
cbar.ax.set_xlabel('Frequency')
ax.gridlines(xlocs=np.arange(-180, 180, 90),ylocs=np.arange(-60, 91, 30),linestyle='--')
ax.set_title('40th-25th',fontsize=30)

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