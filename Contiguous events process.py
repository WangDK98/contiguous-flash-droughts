# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:25:15 2024

@author: 18262
"""

import numpy as np
import cc3d
import pandas as pd
#%%


fdi_in = np.array(fdi)
labels_out, N = cc3d.connected_components(fdi_in, return_N=True, connectivity=26)
statsdata = cc3d.statistics(labels_out)
voxel_count = statsdata['voxel_counts']
centroids = statsdata['centroids']
bounding = statsdata['bounding_boxes']


index_needed = np.unique(voxel_count>50)

list_1=[]
for i in range(1,len(index_needed[0])):
    list_1.append(np.where(labels_out == index_needed[0][i]))
    print('process'+str(i))

rad = 4.0*np.arctan(1.0)/180.0
re = 6371.220
rr = re*rad/2


ARE=[]
for i in range(len(list_1)):
    print('process'+str(i))
    area=0
    for j in range(len(list_1[i][0])):
        area = area + rr*rr*np.cos((lat[list_1[i][0][j]])/180*np.pi)
    ARE.append(area)


np.count_nonzero(np.array(ARE)>500000)

list_2=[]
for i in range(len(np.where(np.array(ARE)>500000)[0])):
    list_2.append(list_1[np.where(np.array(ARE)>500000)[0][i]])
    
    
#%% f(calu_area)--mean area

def area_cal(lat1,lon1,area):
    df=pd.DataFrame([lat1,lon1]).T
    df = df.drop_duplicates(keep='first')
    df.columns=['lat','lon']
    group_df = df.groupby('lat',as_index=False).count()
    for z in range(len(group_df)):
        area =area + rr*group_df['lon'][z]*rr*np.cos((group_df['lat'][z])/180*np.pi)
    return area





#%% Mean_area and accum_area
for i in range(len(list_2)):
    print('process'+str(i))
    area_stat = []
    lat_list=[]
    lon_list=[]
    time_list=[]
    for j in range(len(list_2[i][0])):
        lat_list.append(lat[list_2[i][0][j]])    
        lon_list.append(lon[list_2[i][1][j]])
        time_list.append(list_2[i][2][j])
    df = pd.DataFrame([lat_list,lon_list,time_list]).T
    df.columns = ['lat','lon','time']
    group_df = df.groupby('time').groups
    dict_items = group_df.items()
    list_obj = [item for item in dict_items]
    for z in range(len(list_obj)):
        area=0
        list_lat=[]
        list_lon=[]
        for a in range(len(list_obj[z][1])):
            list_lat.append(lat_list[list_obj[z][1][a]])
            list_lon.append(lon_list[list_obj[z][1][a]])
        area = area_cal(list_lat, list_lon, area)
        area_stat.append(area)
        
        
        
#%%f(calu_intensity)
def area_weighting(lat1,lon1,SMroot1,area):
    df=pd.DataFrame([lat1,lon1,SMroot1]).T
    df = df.drop_duplicates(keep='first')
    df.columns=['lat','lon','smv']
    group_df = df.groupby('lat',as_index=False).count()
    for z in range(len(group_df)):
        area = area + rr*group_df['lon'][z]*rr*np.cos((group_df['lat'][z])/180*np.pi)
    SM_weight = 0
    for z1 in range(len(df)):
        area_div = rr*rr*np.cos((df['lat'][z1])/180*np.pi)
        ratio = area_div / area
        SM_weight = SM_weight + ratio*df['smv'][z1]
    return SM_weight, area


# intensity metric

for i in range(len(list_2)):
    print('process'+str(i))
    lat_list=[]
    lon_list=[]
    time_list=[]
    SM_values=[]
    for j in range(len(list_2[i][0])):
        lat_list.append(lat[list_2[i][0][j]])    
        lon_list.append(lon[list_2[i][1][j]])
        time_list.append(list_2[i][2][j])
        SM_values.append(SM_minus[list_2[i][0][j],list_2[i][1][j],list_2[i][2][j]].values.tolist())
    df = pd.DataFrame([lat_list,lon_list,time_list,SM_values]).T
    df.columns = ['lat','lon','time','value']
    magnitude = 0
    for k in range(len(df)):
        magnitude = magnitude + rr*rr*np.cos((df['lat'][k])/180*np.pi)*df['value'][k]
    total_magnitude.append(magnitude)
    max_intensity.append(np.max(df['value']))
    group_df = df.groupby('time').groups
    dict_items = group_df.items()
    list_obj = [item for item in dict_items]
    area_stat=[]    
    SM_stat=[]
    for z in range(len(list_obj)):
        group_lat=[]
        group_lon=[]
        group_value=[]
        area=0
        for a in range(len(list_obj[z][1])):
            group_lat.append(lat_list[list_obj[z][1][a]])
            group_lon.append(lon_list[list_obj[z][1][a]])
            group_value.append(SM_values[list_obj[z][1][a]])
        SM_Weight, area_total = area_weighting(group_lat, group_lon, group_value, area)
        area_stat.append(area_total)
        SM_stat.append(SM_Weight)
    area_stat = list(np.array(area_stat)/sum(area_stat))

#%%centroids
def distance_calcu(lat,lon,list_dis):
    for i in range(len(lat)-1):
        dis = geodesic((lat[i],lon[i]),(lat[i+1],lon[i+1])).kilometers
        list_dis.append(dis)
    return list_dis

speed=[]
distance=[]
start_centroid=[]
end_centroid=[]
centroid_total=[]

for i in range(len(list_2)):
    print('process'+str(i))
    lat_list=[]
    lon_list=[]
    SM_values=[]
    time_list=[]
    for j in range(len(list_2[i][0])):
        lat_list.append(lat[list_2[i][0][j]])    
        lon_list.append(lon[list_2[i][1][j]])
        time_list.append(list_2[i][2][j])
        SM_values.append(SM_minus[list_2[i][0][j],list_2[i][1][j],list_2[i][2][j]].values.tolist())
    df = pd.DataFrame([lat_list,lon_list,time_list,SM_values]).T
    df.columns = ['lat','lon','time','value']
    group_df = df.groupby('time').groups
    dict_items = group_df.items()
    list_obj = [item for item in dict_items]
    lat_cen_list=[]
    lon_cen_list=[]
    for z in range(len(list_obj)):
        group_lat=[]
        group_lon=[]
        group_value=[]
        for a in range(len(list_obj[z][1])):
            group_lat.append(lat_list[list_obj[z][1][a]])
            group_lon.append(lon_list[list_obj[z][1][a]])
            group_value.append(SM_values[list_obj[z][1][a]])
        df=pd.DataFrame([group_lat,group_lon,group_value]).T
        df.columns = ['lat','lon','value']
        df['value']=df['value']/sum(df['value'])
        lat_centroid=0
        lon_centroid=0
        for b in range(len(df)):
            lat_centroid = lat_centroid + df['lat'][b]*df['value'][b]
            lon_centroid = lon_centroid + df['lon'][b]*df['value'][b]    
        lat_cen_list.append(lat_centroid)
        lon_cen_list.append(lon_centroid)        
    start_centroid.append((np.mean(lat_cen_list[:math.ceil(len(lat_cen_list)/2)]),np.mean(lon_cen_list[:math.ceil(len(lon_cen_list)/2)])))
    end_centroid.append((np.mean(lat_cen_list[math.ceil(len(lat_cen_list)/2):]),np.mean(lon_cen_list[math.ceil(len(lon_cen_list)/2):])))
    centroid_total.append((np.mean(lat_cen_list),np.mean(lon_cen_list)))    

#%%
#Calculate move angle
def calcu_azimuth(lat1, lon1, lat2, lon2):
    lat1_rad = lat1 * pi / 180
    lon1_rad = lon1 * pi / 180
    lat2_rad = lat2 * pi / 180
    lon2_rad = lon2 * pi / 180
    y = sin(lon2_rad - lon1_rad) * cos(lat2_rad)
    x = cos(lat1_rad) * sin(lat2_rad) - sin(lat1_rad) * cos(lat2_rad) * cos(lon2_rad - lon1_rad)
    brng = atan2(y, x) / pi * 180
    return brng
'''
calcu_azimuth(start_centroid[0][0],start_centroid[0][1],end_centroid[0][0],end_centroid[0][1])
'''
angel=[]
for i in range(len(start_centroid)):
    angel.append(calcu_azimuth(start_centroid[i][0],start_centroid[i][1],end_centroid[i][0],end_centroid[i][1]))