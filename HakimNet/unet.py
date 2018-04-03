#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:12:02 2018

@author: user
"""

from __future__ import absolute_import, print_function, division
import os
from nifti_segmenter import nifti_segmenter
# '/home/user/Desktop/Unet-ants-master/data_3D/image_filemap.csv'
import csv
import numpy as np

#csvname = input('Enter filemaps here: ').strip("'")
csvname = '/home/user/Desktop/Unet-ants-master/data_3D/image_filemap.csv'.strip("'")
basedir = '/home/user/Desktop/Unet-ants-master/data_3D/images'.strip("'")
                
def form_dataset_from_CSV(CSV_PATH):
    inputs = []; labels = []; alg = [];
    with open(CSV_PATH, 'r') as file:
        reader = csv.reader(file)
        r = 0
        for row in reader:
            if r == 0:
                r = r + 1
                continue
            else:
                #print(os.path.join(basedir, row[0]))
                temp, orig = nifti_segmenter(os.path.join(basedir, row[0]), 
                                             NumberOfSegmentsPerFile=5, 
                                             SegmentShape=(50,50,50), 
                                             Reuse=False,
                                             Origins=None)
                inputs.append(temp)
                
                #print(os.path.join(basedir, row[1]))
                temp, _ = nifti_segmenter(os.path.join(basedir, row[1]), 
                                       NumberOfSegmentsPerFile=5, 
                                       SegmentShape=(50,50,50), 
                                       Reuse=True, 
                                       Origins=orig)
                labels.append(temp)
                r = r + 1
            """
            temp = nifti_segmenter(os.path.join(basedir, row[0]), 5, (50,50,50)); inputs.append(temp)
            temp = nifti_segmenter(os.path.join(basedir, row[1]), 5, (50,50,50)); labels.append(temp)
            """                
            r = r + 1

    return inputs, labels
            
inputs, labels = form_dataset_from_CSV(csvname)
print((np.array(inputs[0][0]).shape))
print((np.array(labels[0][0]).shape))