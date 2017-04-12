#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:07:52 2017

@author: meghapanda
"""
import numpy as np
import glob

def merge(file_name):
    data_path = 'Consen/*.dta' 
    files=glob.glob(data_path) 
    consolidated_file=[]
    space=['\n','\n']
    
    query_map_temp=[]
     
    dtype = [ ('mass', float),('file_name', 'S50'),('query', 'int')] 
    
    for file_content in files: 
        with open(file_content) as f:
            content = f.readlines()
            consolidated_file=consolidated_file+content+space
            temp=(float(content[0].split(' ')[0]),file_content.split('/')[-1][:-4],0)
            query_map_temp.append(temp)
        
    query_map_temp = np.array(query_map_temp, dtype=dtype)
    query_map_temp=np.sort(query_map_temp, order='mass')
    
    query=1
    for element in query_map_temp:
        element[2]=query
        query+=1
    
    query_map=np.column_stack((query_map_temp['file_name'],query_map_temp['query']))
    query_map=np.row_stack((['file','query'],query_map))   
    
    f =  open(file_name+'.dta', 'w')
    
    for element in consolidated_file:
        f.write(element)
    f.close()
    
    np.savetxt(file_name+'merge_query_key.csv',query_map, delimiter=",", fmt="%s") 
 