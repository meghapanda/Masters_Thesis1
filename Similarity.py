#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:05:19 2017

@author: meghapanda
"""

import numpy as np
def Spec_Sim(Spectrum1,Spectrum2):
    l1=Spectrum1.shape[0]
    l2=Spectrum2.shape[0]
    
    if (l1<=1 and l2<=1):
		return 0
    else:
        mass=list(Spectrum1[1:,0])+list(Spectrum2[1:,0])
        mass=np.floor(mass)
        massnew=np.unique(mass)
        similarity=[]
        
        bin_size=5
        I_a= [[] for _ in xrange(bin_size)]
        I_b= [[] for _ in xrange(bin_size)]
        mass_range=[[] for _ in xrange(bin_size)]
        Ia=0
        Ib=0
        for mass_start in massnew:
            for index in range(0,len(mass_range)):
                mass=mass_start+(0.1*index)
              
                ## Spectrum 1
                    ## first bin
                
                a=np.where(np.logical_and ((Spectrum1[:,0]>=(mass)) ,(Spectrum1[:,0]<(mass+0.5)) ))
                if (len(a[0])):
                    for k in a[0]:
                        Ia=Ia+Spectrum1[k,1]
                else:
                    Ia=0
                I_a[index].append(Ia)
                Ia=0
                a=np.where(np.logical_and ((Spectrum1[:,0]>=(mass+0.5)) ,(Spectrum1[:,0]<(mass+1)) ))
                if (len(a[0])):
                    for k in a[0]:
                        Ia=Ia+Spectrum1[k,1]
                else:
                    Ia=0
                I_a[index].append(Ia)
                Ia=0
                
                
            
            
            
            
            
            
            
            
            
                 ## Spectrum 2
                    ## first bin
                    
                a=np.where(np.logical_and ((Spectrum2[:,0]>=(mass)) ,(Spectrum2[:,0]<(mass+0.5)) ))
                if (len(a[0])):
                    for k in a[0]:
                        Ib=Ib+Spectrum2[k,1]
                else:
                    Ib=0
                I_b[index].append(Ib)
                Ib=0
                a=np.where(np.logical_and ((Spectrum2[:,0]>=(mass+0.5)) ,(Spectrum2[:,0]<(mass+1)) ))
                if (len(a[0])):
                    for k in a[0]:
                        Ib=Ib+Spectrum2[k,1]
                else:
                    Ib=0
                I_b[index].append(Ib)
                Ib=0
            
            
            
            
        ## Calculating all the similarities
        for index in range (0,len(I_a)):
            sim_score=np.dot(I_a[index],I_b[index])/np.sqrt(np.dot(I_a[index],I_a[index])*np.dot(I_b[index],I_b[index]))
            similarity.append(sim_score)
    return max(similarity)
        
       
   
   
   

