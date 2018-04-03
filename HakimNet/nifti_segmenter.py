#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:52:14 2018

@author: user
"""
import nibabel as nib
import numpy as np
import random
import os

def nifti_segmenter(filepath, 
                    NumberOfSegmentsPerFile,
                    SegmentShape, 
                    Reuse=False, 
                    Origins=None):
    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    mould = filename.strip(".nii.gz")
    
    
    data = nib.load(filepath).get_data()
    data = data[:,:,:]
    #print("Data has shape : " + str(data.shape))
    
    s,r,c = SegmentShape
    
    S,R,C = data.shape
    """
    print("Sample will have " + str(R)
    + " rows, " + str(C)
    + " columns, " + str(S) + " slices.")
    print("Segments will have " + str(r)
    + " rows, " + str(c)
    + " columns, " + str(s) + " slices.")
    """
    Segs = []
    
    if Reuse == False:
        Origins = []
    else:
        Origins = Origins
    ori = 0
    for seg in np.arange(NumberOfSegmentsPerFile):
        if Reuse == False:
            oS, oR, oC = [random.randint(s, (S-s)),
                          random.randint(r, (R-r)),
                          random.randint(c, (C-c))]
            Origins.append([oS, oR, oC])
        else:
            oS, oR, oC = Origins[ori]
            ori = ori + 1
            
        #print("Origin: ("+str([oS,oR, oC]) + ")")
        SEGMENT = data[oS:oS+s,oR:oR+r,oC:oC+c]
        #print("Segment " + str(seg) + " has shape " + str(SEGMENT.shape))
        SEG_FILENAME = mould + "_seg_" + str(seg) + ".nii"
        Segs.append([SEGMENT])
        
        """
        SEG = nib.Nifti1Image(SEGMENT, np.eye(4))
        nib.save(SEG, SEG_FILENAME)
        """
        
    return Segs, Origins

    
    