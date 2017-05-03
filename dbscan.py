#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:34:04 2017

@author: meghapanda
"""
### Importing
from sklearn.cluster import DBSCAN
import numpy as np
import glob
import consensus as con
from collections import OrderedDict
from Similarity import Spec_Sim as sim
from scipy.spatial.distance import squareform
import os
import merge
import preproc as pre
import math
import json




## loading Data

data_path="/Users/meghapanda/Documents/Msc_Project/Code/BLindTestDTA/*.dta" 
files=glob.glob(data_path) 
#number_data_points=len(files)


strong_peaks=50
spectra_list=OrderedDict()
spectra_list_full=OrderedDict()
for file_spectra in files:     
#    spectra_list[file_spectra.split('/')[-1][:-4]]=pre.process(np.loadtxt(file_spectra),strong_peaks)
    spectra_list_full[file_spectra.split('/')[-1][:-4]]=np.loadtxt(file_spectra)
    spectra_list[file_spectra.split('/')[-1][:-4]]=np.loadtxt(file_spectra)

file_name_main="/Users/meghapanda/Documents/Msc_Project/Code/DBSCAN_full/"
distance_matrix_condensed=[]
#distance_matrix_condensed=np.load(os.path.join(file_name_main+'distance_matrix.npy'))       


                
for item_x in range (0,len(spectra_list.keys())):
    print(item_x)
    for item_y in range (item_x+1,len(spectra_list.keys())):
        similarity=sim(spectra_list[spectra_list.keys()[item_x]],spectra_list[spectra_list.keys()[item_y]])
        distance_matrix_condensed.append(1-similarity)
np.save(os.path.join(file_name_main+'distance_matrix.npy'),distance_matrix_condensed)


distance_matrix=squareform(distance_matrix_condensed)
file_save_search=[]
eps=[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9]
min_samples=np.arange(1,7,1)
#eps=[0.1]
#min_samples=[2]

for eps_val in eps:
    for min_points in  min_samples:
        
        file_name=file_name_main+'eps-'+str(eps_val)+'_'+'min_pts-'+str(min_points )
        db = DBSCAN(eps=eps_val, min_samples=min_points, metric='precomputed')
        db.fit(distance_matrix)
        labels = np.array(db.labels_) 
        n_clusters_ = len(set(db.labels_)) - (1 if -1 in labels else 0)
        noise_=np.count_nonzero(labels == -1)
        print(eps_val,min_points,n_clusters_,noise_,len(np.unique(labels)))
        



        
        cluster_count=1 
        concensus_key=[]            
        for i in np.unique(labels):
            temp=''
            if i==-1:
                arr=np.where(labels==i)
                for item in arr[0]:
                    concensus_key.append(('cluster'+str(cluster_count),spectra_list.keys()[item]))
                    cluster_count +=1
            else:
                arr=np.where(labels==i)
                for item in arr[0]:
                    temp=temp+str(spectra_list.keys()[item])+','
                concensus_key.append(('cluster'+str(cluster_count),temp[:-1]))
                cluster_count +=1
        
        
                
        number_of_files_in_each_search=1200
        number_of_search_files_cluster=int(math.ceil(float(len(concensus_key))/float(number_of_files_in_each_search)))  
        for index in range(number_of_search_files_cluster):
            file_name=file_name+'part-' +str(index)+'_'
            if ((index+1)*number_of_files_in_each_search>=len(concensus_key)):
                last=len(concensus_key)
            else:
                last=(index+1)*number_of_files_in_each_search
            begin=index*number_of_files_in_each_search
            print(index,begin,last)
            
            concensus_key_save=np.row_stack((['cluster_name','file_name'],concensus_key[begin:last]))
           
            np.savetxt(os.path.join(file_name+'query_mapped.csv'),concensus_key_save, delimiter="->", fmt="%s")     
            dtype = [ ('cluster', 'S50'),('file_name', 'object')]     
            concensus_key_temp=np.array(concensus_key[begin:last],dtype=dtype)
            
            
            
            remove_files = glob.glob('/Users/meghapanda/Documents/Msc_Project/Code/Consen/*')
            for f in remove_files:
                os.remove(f)
            con.concensus_ms(concensus_key_temp,spectra_list_full)
            merge.merge(file_name)
            file_save_search.append([file_name.split('/')[-1],last-begin])
    
        
 
with open(os.path.join(file_name_main+'file_search.txt'),'w')as outfile:
    json.dump(file_save_search,outfile)