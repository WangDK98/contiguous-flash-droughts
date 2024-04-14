# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:52:36 2024

@author: 18262
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#%%pdf for max_intensity
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["ytick.minor.visible"] = False
bins = np.arange(np.min(df['max_intensity']),np.max(df['max_intensity']),0.01)
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
hist = ax.hist(x=df['max_intensity'], bins=bins,color="#8fa5ba",linewidth=0.4,
          edgecolor ='black',rwidth =1,density =True)
ax.set_xticks(np.arange(0,0.23,0.05))
ax.set_yticks(np.arange(0,18,2.5))
ax.set_xlim(0,0.22)
ax.set_ylim(0,18)
ax.tick_params(axis='both', pad=0.05,width =1,length= 3)
ax.set_xlabel('Max_intensity', )
ax.set_ylabel('Probability density',labelpad=4)
plt.show()
#%%pdf for acc_area
df = pd.DataFrame([lon_fig, lat_fig, np.array(accum_area)/1000000, max_intensity]).T
df.columns = ['lon','lat','area','max_intensity']
'''
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
'''
plt.rcParams["axes.labelsize"] = 10

bins = np.arange(np.min(df['area']),np.max(df['area']),0.2)
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
hist = ax.hist(x=df['area'], bins=bins,color="#8fa5ba",linewidth=0.4,
          edgecolor ='black',rwidth =1)
ax.set_xticks(np.arange(0,15,1))
ax.set_yticks(np.arange(0,600,100))
ax.set_xlim(0.5,15)
ax.set_ylim(0,600)
ax.tick_params(axis='both', pad=0.05,width = 1,length =3)
ax.xaxis.labelpad = 0.5
ax.yaxis.labelpad = 0.5
ax.set_xlabel('Accumulated area')
ax.set_ylabel('Probability density',labelpad=4)
plt.show()