#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:22:24 2017

@author: meghapanda
"""

def process(data,strong_peaks):
	Spectrum_data=data[1:len(data)]
	if len(Spectrum_data)<strong_peaks:
		return Spectrum_data
	else:
		temp=Spectrum_data[Spectrum_data[:,1].argsort()][::-1][0:strong_peaks]
		return temp
#              return temp[temp[:,0].argsort()]