#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 6 19:50:23 2017

@author: meghapanda
"""
import os,scipy.cluster.hierarchy as sp, numpy as np,glob
from collections import OrderedDict
from matplotlib import pyplot as plt

file_name_main="/Users/meghapanda/Documents/Msc_Project/Code/hierarchical_full_complete/"
data_path="/Users/meghapanda/Documents/Msc_Project/Code/BLindTestDTA/*.dta" 

files=glob.glob(data_path) 

spectra_list_full=OrderedDict()
for file_spectra in files:     
    spectra_list_full[file_spectra.split('/')[-1][:-4]]=np.loadtxt(file_spectra)
    
distance_matrix_condensed=np.load(os.path.join(file_name_main+'distance_matrix.npy')) 
linkage_matrix=sp.linkage(distance_matrix_condensed,method='complete')

plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('spectra')
plt.ylabel('distance')
dn = sp.dendrogram(linkage_matrix,leaf_rotation=90.,leaf_font_size=8,color_threshold=0.3,labels=spectra_list_full.keys())
fig = plt.gcf()
fig.savefig('myimage.png', dpi=3000)


