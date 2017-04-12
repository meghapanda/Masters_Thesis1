#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:22:42 2017

@author: meghapanda
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv



with open('DBSCAN_top 100/Result DBSCAN_top 100.csv', 'r')  as f:
            temp_result = list(csv.reader(f, delimiter=","))

result=np.array(temp_result[4:])
            
arr=np.where(result[:,2]=='2')
 
n_groups = len(arr[0])+1
identity = tuple(np.append([temp_result[3][3]],result[arr[0],3]))
homology = tuple(np.append([temp_result[3][4]],result[arr[0],4]))
sequence = tuple(np.append([temp_result[3][5]],result[arr[0],5]))
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, identity, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Identity')
 
rects2 = plt.bar(index + bar_width, homology, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Homology')
 
rects3 = plt.bar(index + 2*bar_width, sequence, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Sequence')
plt.xlabel('Parameters')
plt.ylabel('Count')
plt.title("min_pts=2: When strongest 100 peaks is considered")
plt.xticks(index + bar_width, tuple(np.append([temp_result[3][0]],result[arr[0],0])))
plt.legend()

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom',rotation=90)

        
        
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.tight_layout()
plt.show()