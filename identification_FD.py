# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:21:22 2024

@author: 18262
"""




import xarray as xr
import numpy as np

#%%

print("#### Processing SMroot_p20")
SMroot_p20 = SM_use.quantile(0.2, dim='time')
print("#### Processing SMroot_p40")
SMroot_p40 = SM_use.quantile(0.4, dim='time')

#%%
# condition of SM being below the 20th pencentile
print("#### Processing cond1")
cond1 = (SMroot < SMroot_p20).astype(int)
# condition of SM being above the 40th pencentile
print("#### Processing cond2")
cond2 = (SMroot > SMroot_p40).astype(int)
#condition of SM being below the 25th pencentile during a drought


timename = "time"
# %%
# SMroot must go from over 40th pencentile to under 20th pencentile in 4 pentads or less
print("#### Processing cond4")
cond3 = (cond1 * (sum([cond2.shift({timename: sft}) for sft in range(1,5)]) > 0)).astype(int)
# duration of the drought between 4 and 18 pentads (until SMroot gets above 20th pencentile again)
print("#### Processing cond5")
cond4 = (sum([cond1.shift({timename: sft * -1}) for sft in range(0, 4)]) == 4).astype(int)

print("#### Processing cond6")
cond5 = (sum([cond1.shift({timename: sft * -1}) for sft in range(0, 19)]) <= 18).astype(int)

# cond4*cond5*cond6 gives True on the possible onsets of flash droughts
print("#### Processing cond7")
cond6 = cond3 * cond4 * cond5
#%%
def fd(onsets, under25) :
    # create an array of zeros (False) like the onsets vector
    fdindex = np.zeros_like(onsets)
    for i in range(onsets.shape[0]) :
        if bool(onsets[i]) == True : # if this pentad is an onset pentad
            if bool(onsets[i-1]) != True : # and the previous pentad is not an onset
                if fdindex[i-1] == 0 : # and the previous pentad is not under flash drought
                     # fill the lenght of the drought with 1s while the under25 condition is True
                    j = 0
                    while bool(under25[i+j]):
                        fdindex[i+j] = 1
                        j += 1
    return fdindex

#apply the funtion to all lon/lat
fdindex = xr.apply_ufunc(fd, cond6, cond1, input_core_dims=[[timename], [timename]],
                         output_core_dims=[[timename]], vectorize = True)