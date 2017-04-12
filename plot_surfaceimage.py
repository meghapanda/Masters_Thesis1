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

eps=[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9]
min_samples=np.arange(1,7,1)
img_identity=np.zeros((len(eps), len(min_samples)))
img_homology=np.zeros((len(eps), len(min_samples)))
img_sequence=np.zeros((len(eps), len(min_samples)))
#eps=[0.9]
#min_samples=[1]
for i,eps_val in enumerate(eps):
    for j,min_points in  enumerate(min_samples):            
        arr=np.where(np.logical_and(result[:,2]==str(min_points) ,result[:,1]==str(eps_val)))
        img_identity[i,j]=result[arr[0],[3]][0]
        img_homology[i,j]=result[arr[0],[4]][0]
        img_sequence[i,j]=result[arr[0],[4]][0]
 

plt.subplot(1,3,1), 
plt.imshow(img_identity,extent=[0,1,6,1],aspect='auto')
plt.xlabel('epsilon')
plt.ylabel('min_points')
plt.title('Identity')
plt.subplot(1,3,2),
plt.imshow(img_homology,extent=[0,1,6,1],aspect='auto')
plt.xlabel('epsilon')
plt.ylabel('min_points')
plt.title('Homology')
plt.subplot(1,3,3),
plt.imshow(img_sequence,extent=[0,1,6,1],aspect='auto')
plt.xlabel('epsilon')
plt.ylabel('min_points')
plt.title('Sequence')
plt.show()