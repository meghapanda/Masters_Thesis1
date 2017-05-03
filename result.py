#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:18:49 2017

@author: meghapanda
"""

import numpy as np
import csv
import os
import glob


all_files_path='/Users/meghapanda/Documents/Msc_Project/Code/indivisual/*.dta'
all_files=glob.glob(all_files_path)
print('File_name,Identity,Homology,Sequence')
for a_file in all_files:
    file_name=a_file[:-4]

    with open(os.path.join(file_name+'_search.csv'), 'r') as f:
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
     
    
    temp_key = np.genfromtxt(os.path.join(file_name+'merge_query_key.csv'), dtype=None, delimiter=',', names=True)       
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
        new_entry=(temp_key['file_'][arr[0][0]],entry[0],entry[1],entry[2])
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
    
    
    print(len(Identity))
    print(len(Homology))
    print(len(Sequence))
    #np.savetxt('Res_main_500_final.csv',final_result, delimiter=",",header="'file','Identity','homology','sequence'", fmt="%s") 