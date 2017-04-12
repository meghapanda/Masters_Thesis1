#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:28:11 2017

@author: meghapanda
"""
import numpy as np


original_key=np.genfromtxt("BLindTestDTA/key.csv", dtype=None, delimiter=' ',names=True)
uncluster_result=np.genfromtxt("Res_main_500_final.csv", dtype=None, delimiter=',',names=True)
cluster_result=np.genfromtxt("Res_main_cluster_final.csv", dtype=None, delimiter=',',names=True)


final_result=[]

for i,ele in enumerate(original_key['File']):
    arr_clus=np.where(cluster_result['file_']==int(ele[:-4]))
    arr_unclus=np.where(uncluster_result['file_']==int(ele[:-4]))
    #dealing with clustered result
    
    if len(arr_clus[0])>1:
        temp_identity=[]
        temp_homology=[]
        temp_seq=[]
        for file_1 in arr_clus[0]:
            temp_identity.append(cluster_result[file_1][1])
            temp_homology.append(cluster_result[file_1][2])
            temp_seq.append(cluster_result[file_1][3])
            
        if original_key['Sequence'][i] in temp_identity:
            cluster_entry=[1,0,0]
        elif original_key['Sequence'][i] in temp_homology:
            cluster_entry=[0,1,0]
        elif original_key['Sequence'][i] in temp_seq:
            cluster_entry=[0,1,0]
        else:
            cluster_entry=[3,0,0]
            

                
             
    elif(cluster_result[arr_clus[0][0]][1]!='0' and cluster_result[arr_clus[0][0]][1]==original_key['Sequence'][i]):
        cluster_entry=[1,0,0]
    elif(cluster_result[arr_clus[0][0]][2]!='0' and cluster_result[arr_clus[0][0]][2]==original_key['Sequence'][i]):
        cluster_entry=[0,1,0]
    elif(cluster_result[arr_clus[0][0]][3]!='0' and cluster_result[arr_clus[0][0]][3]==original_key['Sequence'][i]):
        cluster_entry=[0,0,1]
    else:
        cluster_entry=[0,0,0]

    #dealing with unclustered result
    
    if len(arr_unclus[0])>1:
        temp_identity=[]
        temp_homology=[]
        temp_seq=[]
        for file_1 in arr_unclus[0]:
            temp_identity.append(uncluster_result[file_1][1])
            temp_homology.append(uncluster_result[file_1][2])
            temp_seq.append(uncluster_result[file_1][3])
            
        if original_key['Sequence'][i] in temp_identity:
            uncluster_entry=[1,0,0]
        elif original_key['Sequence'][i] in temp_homology:
            uncluster_entry=[0,1,0]
        elif original_key['Sequence'][i] in temp_seq:
            uncluster_entry=[0,1,0]
        else:
            uncluster_entry=[0,0,0]
            

                
             
    elif(uncluster_result[arr_unclus[0][0]][1]!='0' and uncluster_result[arr_unclus[0][0]][1]==original_key['Sequence'][i]):
        uncluster_entry=[1,0,0]
    elif(uncluster_result[arr_unclus[0][0]][2]!='0' and uncluster_result[arr_unclus[0][0]][2]==original_key['Sequence'][i]):
        uncluster_entry=[0,1,0]
    elif(uncluster_result[arr_unclus[0][0]][3]!='0' and uncluster_result[arr_unclus[0][0]][3]==original_key['Sequence'][i]):
        uncluster_entry=[0,0,1]
    else:
        uncluster_entry=[0,0,0]

   
    newentry=(original_key[i][0],original_key[i][1],uncluster_entry[0],uncluster_entry[1],uncluster_entry[2],cluster_entry[0],cluster_entry[1],cluster_entry[2])
    final_result.append(newentry)

dtype = [('file_name', 'S50'),('seq', 'S50'),('unclus_iden', 'int'),('unclus_homo', 'int'),('unclus_seq', 'int'),('clus_iden', 'int'),('clus_homo', 'int'),('clus_seq', 'int')]    
final_result = np.array(final_result, dtype=dtype) 

print('Clustered_homology_matches',np.sum(final_result['clus_homo']))
print('Unclustered_homology_matches',np.sum(final_result['unclus_homo']))
 
print('Clustered_identity_matches',np.sum(final_result['clus_iden']))
print('Unclustered_identity_matches',np.sum(final_result['unclus_iden']))
 
print('Clustered_seq_matches',np.sum(final_result['clus_seq']))
print('Unclustered_seq_matches',np.sum(final_result['unclus_seq']))