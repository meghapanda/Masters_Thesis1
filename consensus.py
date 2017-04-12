#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 01:05:41 2017

@author: meghapanda
"""

import numpy as np
#np.set_printoptions(suppress=True)  
#
#
#data_path = 'BLindTestDTA/*.dta' 
#spectra_list={}
#files=glob.glob(data_path) 
#number_data_points=len(files)
#
#count=101
#for file_spectra in files:     
#    spectra_list[count]=np.loadtxt(file_spectra)
#    count=count+1
## Reading the key for consensus List
#
#fname='Key Mapped - concensus.csv'
#
#concensus_key=np.genfromtxt(fname, dtype=None, delimiter='->',names=True)
def concensus_ms(concensus_key,spectra_list):
    
    if (concensus_key.size==1):
        concensus_key=concensus_key.flatten()
    count=0
    for sequence in concensus_key:
        concensus_list=[np.int16(el) for el in sequence[1].split(',')]
    
        concensus_mass=0
        concensus_charge=2
        
        concensus_spectrum=np.empty(shape=[0, 2])
        for spectrum in concensus_list:
            count+=1
            concensus_spectrum=np.concatenate((concensus_spectrum,spectra_list[str(spectrum)][1:len(spectra_list[str(spectrum)])]),axis=0)
            concensus_mass=concensus_mass+spectra_list[str(spectrum)][0,0]
        concensus_mass=concensus_mass/len(concensus_list)
        
        concensus_spectrum=concensus_spectrum[concensus_spectrum[:, 0].argsort()]
        
        
        threshold=0.1
        while(threshold<=0.4):
            temp=np.empty(shape=[2,])
            index=0
            while (index<len(concensus_spectrum)):
                if (index==len(concensus_spectrum)-1):
                    temp=np.row_stack((temp,concensus_spectrum[index]))
                    index=index+1l
                elif (concensus_spectrum[index+1][0]-concensus_spectrum[index][0]<threshold):
                    new_entry=np.array(((concensus_spectrum[index+1][0]+concensus_spectrum[index][0])/2,concensus_spectrum[index+1][1]+concensus_spectrum[index][1]))
                    temp=np.row_stack((temp,new_entry))
                    index=index+2
                else:
                    temp=np.row_stack((temp,concensus_spectrum[index]))
                    index=index+1
            concensus_spectrum=temp
            threshold=threshold+0.1
        
        concensus_spectrum=np.row_stack((np.array((concensus_mass,concensus_charge)),concensus_spectrum))   
        
                
        file_name='Consen/'+sequence[0]+'.dta'
        np.savetxt(file_name, concensus_spectrum, delimiter=' ')     
                                          

