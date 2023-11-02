# -*- coding: utf-8 -*-
 
#
# Imports
#
import os
import json
import pydicom  
from DicomProcessing import DicomProcessing

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title ="Medical Image Processing", version="0.1.0")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
#
# Routes
#
@app.get("/")
async def root():
    """ Send a welcome message for the user """
    
    return {"message": "Welcome to the DICOM image processing application"}
 
@app.post('/calculate-dicom-image-volume')
async def handleDicomImage( imageFile: UploadFile):
    """ Calculates the volume of a dicom medical image """
    
    threshold = float(os.environ['threshold'])
    
    if( imageFile.filename == '' ):
        raise HTTPException(status_code=422, detail="The file was not uploaded")
    
    if( not imageFile.filename.endswith(".dcm") ):
        raise HTTPException(status_code=422, detail="This image is not a dicom file")
    
    try:
        obj = DicomProcessing()
        pixelsAboveCutoff, volume = obj.runVolumePipeline(imageFile.file, threshold)
    except:
        raise HTTPException(status_code=422, detail="This image is not a valid dicom file")
        
    return {'name': imageFile.filename, 'volume': volume, "pixelsAboveCutoff": pixelsAboveCutoff }
