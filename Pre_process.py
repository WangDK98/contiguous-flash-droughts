# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:15:32 2024

@author: 18262
"""


import xarray as xr
import dask

#%%
# load the data
# set the path of the data
data_path = "E:/ERA-5"

#create a list with the name of the folders of SMroot each year to load
n= 41
i = 0
var_folders = []
year = []

while i < n :
    y = 1980 + i
    year.append(str(y))
    var_folders.append(str(y))
    i = i + 1

timename = "time"
#%%
#load data and resample to pentads
#create dictionaries to store data

data_daily = dict()
data_daily_365 = dict()
data_pentad = dict()
pentads_list = []

#load the data, then resample to pentads
for vf in var_folders :
    print("#### Processing " + vf)
    data_daily[vf] =xr.open_mfdataset(data_path + "/" + vf +".nc").astype("float16")


#remove leap days so we have the same number of pentads in each year
#avoid large chunks
    with dask.config.set(**{"array.slicing.split_large_chunks": True}):
        data_daily_365[vf] = data_daily[vf].sel(time=~((data_daily[vf].time.dt.month == 2) & (data_daily[vf].time.dt.day == 29)))


    # create index of pentads in 365 calender to resample
    for n in range(int(data_daily_365[vf].time.shape[0]/5)):
        for m in range(5):
            pentads_list.append(n)
    pentads_group = xr.DataArray(pentads_list, dims=timename, name=timename,coords={timename: data_daily_365[vf].time})
    pentads_list = []
    #resample to pentads
    data_pentad[vf] = data_daily_365[vf].groupby(pentads_group).apply(lambda x: x.mean(dim=timename, skipna=True)).compute().assign_coords({timename:data_daily_365[vf]["time"][::5]})

#%%  
SMroot = data_pentad["1980"]['RZMC']
j = 1
while j < 41 :
    years = 1980 + j
    print("#### Processing " + str(years))
    SMroot = xr.concat([SMroot,data_pentad[str(years)]["RZMC"]], dim=timename)
    j = j + 1
    
SMroot = SMroot.transpose('lat','lon','time')
SM_use = SMroot.astype('float32')