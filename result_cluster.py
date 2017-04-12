#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:18:49 2017

@author: meghapanda
"""

import numpy as np
import csv
eps=[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9]
min_samples=np.arange(1,7,1)
#eps=[0.8]
#min_samples=[1]
print('Epsilon,Min Points,Identity,Homology,Sequence')
for eps_val in eps:
    for min_points in  min_samples:
        file_name='DBSCAN_top 100/dbs_top_100'
        file_name=file_name+'eps-'+str(eps_val)+'_'+'min_pts'+str(min_points )


## search result    
        with open(file_name+'_search.csv', 'r') as f:
            temp_result = list(csv.reader(f, delimiter=","))
        result=np.empty(shape=[14,])
        for data in temp_result:
            if len(data)==14:
                result=np.row_stack((result,data))
        result=np.column_stack((result[2:,2],result[2:,7],result[2:,8],result[2:,9],result[2:,11]))
        
        for i,row in enumerate(result):
            for j,data in enumerate(row):
                if not data:
                    result[i][j]=0
        
        ##query key from from merge
        temp_key = np.genfromtxt(file_name+'merge_query_key.csv', dtype=None, delimiter=',', names=True)
        #mapped from clustering
        cluster_key= np.genfromtxt(file_name+'query_mapped.csv', dtype=None, delimiter='->',names=True)
        
        
        final_result=[]
        
        dtype = [ ('file_name', 'S50'),('Identity', 'S50'),('Homology', 'S50'),('Sequence', 'S50')]
        for query in result:
            entry=[]
            if (float(query[1])>float(query[3])):
                entry=[query[4],'0', '0']
            elif(float(query[1])>float(query[2])):
                entry=['0',query[4],'0']
            else:
                entry=['0','0',query[4]]
            arr=np.where(temp_key['query']==int(query[0]))
            arr_1=np.where(cluster_key['cluster_name']==temp_key[arr[0][0]][0])
            file_list=cluster_key['file_name'][arr_1[0][0]].split(',')
        
            for file_name in file_list:
                new_entry=(file_name,entry[0],entry[1],entry[2])
                final_result.append(new_entry)
          
            
        final_result = np.array(final_result, dtype=dtype)   
        final_result=np.sort(final_result, order='file_name')
        
        
        
        
        Identity=[]
        Homology=[]
        Sequence=[]
        for file_name in np.unique(final_result['file_name']):
            arr=np.where(final_result['file_name']==file_name)
            if (len(arr[0])>1):
                temp_identity=[]
                temp_homology=[]
                temp_sequence=[]
                for f in arr[0]:
                    if(final_result['Identity'][f]!='0'):
                        temp_identity.append(final_result['Identity'][f])
                    
                        
                        
                    if(final_result['Homology'][f]!='0'):
                        temp_homology.append(final_result['Homology'][f])
                    
                        
                    if(final_result['Sequence'][f]!='0'):
                        temp_sequence.append(final_result['Sequence'][f])
                
                Identity.extend(list(np.unique(temp_identity)))
                Homology.extend(list(np.unique(temp_homology)))
                Sequence.extend(list(np.unique(temp_sequence)))
                        
            elif (final_result['Identity'][arr][0]!='0'):
                Identity.append(final_result['Identity'][arr][0])
                
            elif (final_result['Homology'][arr][0]!='0'):
                Homology.append(final_result['Homology'][arr][0])
                
            elif (final_result['Sequence'][arr][0]!='0'):
                Sequence.append(final_result['Sequence'][arr][0])
        
        
        
        print(eps_val,min_points,len(Identity),len(Homology),len(Sequence))
            #np.savetxt('Res_main_cluster_final.csv',final_result, delimiter=",",header="'file','Identity','homology','sequence'", fmt="%s") 