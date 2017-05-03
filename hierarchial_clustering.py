#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:34:04 2017

@author: meghapanda
"""
### Importing
import scipy.cluster.hierarchy as sp
import numpy as np
import glob
import consensus as con
from collections import OrderedDict
from Similarity import Spec_Sim as sim
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
    spectra_list[file_spectra.split('/')[-1][:-4]]=pre.process(np.loadtxt(file_spectra),strong_peaks)
    spectra_list_full[file_spectra.split('/')[-1][:-4]]=np.loadtxt(file_spectra)
#    spectra_list[file_spectra.split('/')[-1][:-4]]=np.loadtxt(file_spectra)

file_name_main="/Users/meghapanda/Documents/Msc_Project/Code/hierarchical_full/"
file_save_search=[]


distance_matrix_condensed=[]
distance_matrix_condensed=np.load(os.path.join(file_name_main+'distance_matrix.npy'))       


                
#for item_x in range (0,len(spectra_list.keys())):
#    print(item_x)
#    for item_y in range (item_x+1,len(spectra_list.keys())):
#        similarity=sim(spectra_list[spectra_list.keys()[item_x]],spectra_list[spectra_list.keys()[item_y]])
#        distance_matrix_condensed.append(1-similarity)
#np.save(os.path.join(file_name_main+'distance_matrix.npy'),distance_matrix_condensed)


linkage_matrix=sp.linkage(distance_matrix_condensed,method='complete')


threshold=[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9]
#threshold=[0]
#threshold=[s*0.001 for s in threshold]
#eps=[0.9]
#min_samples=[1]

for threshold_value in threshold:
        
    file_name=file_name_main+'threshold-'+str(threshold_value)+'_'
    labels=sp.fcluster(linkage_matrix,threshold_value,criterion='distance')
    
    labels = np.array(labels) 
    n_clusters_ =len(np.unique(labels))
    print(threshold_value,n_clusters_)
    



    number_of_files_in_each_search=1200
    number_of_search_files=int(math.ceil(float(len(np.unique(labels)))/float(number_of_files_in_each_search)))                  
    for index in range(number_of_search_files):
        file_name=file_name+'part-' +str(index)+'_'
#    for index in range(number_of_search_files):
        if ((index+1)*number_of_files_in_each_search>=len(np.unique(labels))):
            last=len(np.unique(labels))
        else:
            last=(index+1)*number_of_files_in_each_search
        begin=index*number_of_files_in_each_search
        print(index,begin,last)

        labels_temp=np.unique(labels)[begin:last]
        cluster_count=1 
        concensus_key=[]            
        for i in labels_temp:
            temp=''
            arr=np.where(labels==i)
            for item in arr[0]:
                temp=temp+str(spectra_list.keys()[item])+','
            concensus_key.append(('cluster'+str(cluster_count),temp[:-1]))
            cluster_count +=1
        
        concensus_key_save=np.row_stack((['cluster_name','file_name'],concensus_key))
           
        np.savetxt(os.path.join(file_name+'query_mapped.csv'),concensus_key_save, delimiter="->", fmt="%s")     
        dtype = [ ('cluster', 'S50'),('file_name', 'object')]     
        concensus_key=np.array(concensus_key,dtype=dtype)
        
        
        
        remove_files = glob.glob('/Users/meghapanda/Documents/Msc_Project/Code/Consen/*')
        for f in remove_files:
            os.remove(f)
        con.concensus_ms(concensus_key,spectra_list_full)
        merge.merge(file_name)
        file_save_search.append([file_name.split('/')[-1],last-begin])
        
        
 
with open(os.path.join(file_name_main+'file_search.txt'),'w')as outfile:
    json.dump(file_save_search,outfile)