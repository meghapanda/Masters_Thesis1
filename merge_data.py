#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:07:52 2017
This python code is only for unclusterd data
@author: meghapanda
"""
import numpy as np
import glob
import math
import os

data_path=os.path.abspath("D:\Megha\New Data\Mix_1\LCQ_Deca\mzXML\LQ20051019_LCQ_18MIX01_03/*.dta")
files=glob.glob(data_path) 
space=['\n','\n']



        

number_of_files_in_each_search=1200
number_of_search_files=int(math.ceil(float(len(files))/float(number_of_files_in_each_search)))
for index in range(number_of_search_files):
    file_name="D:\\Megha\\Results\\Mix1\\LCQ_Deca\\indivisual\\" +str(index)+'_'
#    for index in range(number_of_search_files):
    if ((index+1)*number_of_files_in_each_search>=len(files)):
        last=len(files)
    else:
        last=(index+1)*number_of_files_in_each_search
    begin=index*number_of_files_in_each_search
    print(index,begin,last)
    files_temp=files[begin:last]
    consolidated_file=[]
    query_map_temp=[]
    dtype = [ ('mass', float),('file_name', 'S50'),('query', 'int')] 
    for file_content in files_temp: 
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
    
    f =  open(os.path.join(file_name+'indivsual_part.dta'), 'w')
    
    for element in consolidated_file:
        f.write(element)
    f.close()
    
    np.savetxt(os.path.join(file_name+'merge_query_key.csv'),query_map, delimiter=",", fmt="%s") 
 


 



    
