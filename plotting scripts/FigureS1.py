# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:45:51 2024

@author: 18262
"""

import numpy as np
import matplotlib.pyplot as plt




#%%
voxels = np.zeros((3, 3, 5), dtype=int)

voxels[:, :, :] = 3 
voxels[2,0,0]=1


voxels[2,2,4]=2
voxels[1,2,3:]=2
voxels[0,2,3]=2
voxels[0,1,2:4]=2
voxels[1,0:2,1:4]=2
voxels[2,0,1:3]=2





# 创建画布和坐标轴
fig = plt.figure()
ax =  fig.add_subplot(projection='3d')

# 定义颜色映射
colors = ['white', 'blue', 'red', 'gray']

# 绘制建筑物的不同部分


ax.voxels(voxels == 1, facecolors='#DC143C', edgecolor='#F08080',alpha=0.8)
ax.voxels(voxels == 2, facecolors='#FFA500', edgecolor='#F5DEB3',alpha=0.8)
ax.voxels(voxels == 3, facecolors='#708090', edgecolor='#B0C4DE',alpha=0.3)
'''
ax.voxels(voxels == 3, facecolors='#6495ED', edgecolor='#87CEFA',alpha=0.3)
'''

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

help(voxels)
# 设置坐标轴标签
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
'''
ax.axis('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
# 设置图形标题

plt.title('Step 1')

# 显示图形
plt.savefig("C:/Users/18262/Desktop/论文数据/图/step1.tiff",dpi=300,format="tiff")
plt.show()
#%%
voxels = np.zeros((3, 3, 5), dtype=int)
voxels[:, :, :] = 3 
voxels[2,0,0:2]=1
voxels[1,0:3,1]=1


voxels[2,2,4]=2
voxels[1,2,3:]=2
voxels[0,2,3]=2
voxels[0,1,2:4]=2
voxels[1,0:2,2:4]=2
voxels[2,0,2]=2

fig = plt.figure()
ax =  fig.add_subplot(projection='3d')

# 定义颜色映射
colors = ['white', 'blue', 'red', 'gray']

# 绘制建筑物的不同部分


ax.voxels(voxels == 1, facecolors='#DC143C', edgecolor='#F08080',alpha=0.8)
ax.voxels(voxels == 2, facecolors='#FFA500', edgecolor='#F5DEB3',alpha=0.8)
ax.voxels(voxels == 3, facecolors='#708090', edgecolor='#B0C4DE',alpha=0.3)
'''
ax.voxels(voxels == 3, facecolors='#6495ED', edgecolor='#87CEFA',alpha=0.3)
'''

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

help(voxels)
# 设置坐标轴标签
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
'''
ax.axis('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Step 2')
plt.savefig("C:/Users/18262/Desktop/论文数据/图/step2.tiff",dpi=300,format="tiff")

#%%
voxels = np.zeros((3, 3, 5), dtype=int)
voxels[:, :, :] = 3 

voxels[2,0,0:3]=1
voxels[1,0:3,1:3]=1
voxels[0,1,2]=1


voxels[2,2,4]=2
voxels[1,2,3:]=2
voxels[0,2,3]=2
voxels[0,1,3]=2
voxels[1,0:2,3]=2

fig = plt.figure()
ax =  fig.add_subplot(projection='3d')

# 定义颜色映射
colors = ['white', 'blue', 'red', 'gray']

# 绘制建筑物的不同部分


ax.voxels(voxels == 1, facecolors='#DC143C', edgecolor='#F08080',alpha=0.8)
ax.voxels(voxels == 2, facecolors='#FFA500', edgecolor='#F5DEB3',alpha=0.8)
ax.voxels(voxels == 3, facecolors='#708090', edgecolor='#B0C4DE',alpha=0.3)
'''
ax.voxels(voxels == 3, facecolors='#6495ED', edgecolor='#87CEFA',alpha=0.3)
'''

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

help(voxels)
# 设置坐标轴标签
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
'''
ax.axis('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Step 3')
plt.savefig("C:/Users/18262/Desktop/论文数据/图/step3.tiff",dpi=300,format="tiff")


#%%
voxels = np.zeros((3, 3, 5), dtype=int)
voxels[:, :, :] = 3 

voxels[2,0,0:3]=1
voxels[1,0:3,1:4]=1
voxels[0,1,2:4]=1
voxels[0:2,2,3]=1


voxels[1:,2,4]=2


fig = plt.figure()
ax =  fig.add_subplot(projection='3d')

# 定义颜色映射
colors = ['white', 'blue', 'red', 'gray']

# 绘制建筑物的不同部分


ax.voxels(voxels == 1, facecolors='#DC143C', edgecolor='#F08080',alpha=0.8)
ax.voxels(voxels == 2, facecolors='#FFA500', edgecolor='#F5DEB3',alpha=0.8)
ax.voxels(voxels == 3, facecolors='#708090', edgecolor='#B0C4DE',alpha=0.3)
'''
ax.voxels(voxels == 3, facecolors='#6495ED', edgecolor='#87CEFA',alpha=0.3)
'''

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

help(voxels)
# 设置坐标轴标签
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
'''
ax.axis('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Step 4')
plt.savefig("C:/Users/18262/Desktop/论文数据/图/step4.tiff",dpi=300,format="tiff")

#%%

voxels = np.zeros((3, 3, 5), dtype=int)
voxels[:, :, :] = 3 

voxels[2,0,0:3]=1
voxels[1,0:3,1:4]=1
voxels[0,1,2:4]=1
voxels[0:2,2,3]=1


voxels[1:,2,4]=1


fig = plt.figure()
ax =  fig.add_subplot(projection='3d')

# 定义颜色映射
colors = ['white', 'blue', 'red', 'gray']

# 绘制建筑物的不同部分


ax.voxels(voxels == 1, facecolors='#DC143C', edgecolor='#F08080',alpha=0.8)
ax.voxels(voxels == 2, facecolors='#FFA500', edgecolor='#F5DEB3',alpha=0.8)
ax.voxels(voxels == 3, facecolors='#708090', edgecolor='#B0C4DE',alpha=0.3)
'''
ax.voxels(voxels == 3, facecolors='#6495ED', edgecolor='#87CEFA',alpha=0.3)
'''

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

help(voxels)
# 设置坐标轴标签
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
'''
ax.axis('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Step 5')