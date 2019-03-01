# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:29:19 2019

@author: Jorge Andrés Herrera Maldonado en FCDS
"""

        
import os 
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator
from qgis.core import QgsRasterLayer
from qgis.core import QgsProject
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator


# Input Parameter (the paths can't have space in their names) (LA RUTA NO PUEDE TENER ESPACIOS)

path= '\user\input folder with .SAFE files'
output =  '\user\output folder with .SAFE files'

dirs = os.listdir( path )
cont = 0
R_10 = 'B04_10m.jp2'
NIR_10 = 'B08_10m.jp2'
R_20 = 'B04_20m.jp2'
NIR_740_20 = 'B06_20m.jp2'
NIR_783_20 = 'B07_20m.jp2'
NIR_865_20 = 'B8A_20m.jp2'
SWIR_20 = 'B12_20m.jp2'

A_R_10 = []

for root, dirs, files in os.walk(path):
    if root.endswith("R10m"):
        for f in files:
            if f.endswith(R_10):
                R= root +"\\" + f
                print (R) 
            if  f.endswith(NIR_10):
                NIR= root +"\\" + f
                print (NIR)
#NDVI INDEX -------------------------------------------------------------------------------------------------------------         
        fileInfoR = QFileInfo(R)
        fileInfoNIR = QFileInfo(NIR)
        pathR = fileInfoR.filePath()
        pathNIR = fileInfoNIR.filePath()
        baseNameR = fileInfoR.baseName()
        baseNameNIR = fileInfoNIR.baseName()

        layerR = QgsRasterLayer(pathR, baseNameR)
        layerNIR = QgsRasterLayer(pathNIR, baseNameNIR)
        
        entries = []
        # Define r
        r = QgsRasterCalculatorEntry()
        r.ref = 'r@1'
        r.raster = layerR
        r.bandNumber = 1
        entries.append( r )

        # Define nir
        nir = QgsRasterCalculatorEntry()
        nir.ref = 'nir@2'
        nir.raster = layerNIR
        nir.bandNumber = 1
        entries.append( nir )

        # Process calculation with input extent and resolution
        calc = QgsRasterCalculator( '(nir@2 - r@1)/(nir@2 + r@1)', root + '\\' +'NDVI.tif', 'GTiff', layerR.extent(), layerR.width(), layerR.height(), entries )
        calc.processCalculation()
        
        # Process calculation with input extent and resolution
        calc = QgsRasterCalculator( '((nir@2 - r@1)/(nir@2 + r@1 + 0.428))*(1+0.428)', root + '\\' +'SAVI.tif', 'GTiff', layerR.extent(), layerR.width(), layerR.height(), entries )
        calc.processCalculation()

        #the NDVI.TIF and SAVI.TIF file is saved in the same folder where the bands are located.

#############################################################################################################################################################################################################
# BAIS INDEX------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if root.endswith("R20m"):
        for f in files:
            if f.endswith(R_20):
                R= root +"\\" + f
                print (R) 
            if  f.endswith(NIR_740_20):
                NIR1= root +"\\" + f
                print (NIR1)
            if  f.endswith(NIR_783_20):
                NIR2= root +"\\" + f
                print (NIR2)
                
            if  f.endswith(NIR_865_20):
                NIR3= root +"\\" + f
                print (NIR3)
                
            if  f.endswith(SWIR_20):
                SWIR= root +"\\" + f
                print (SWIR)
                
        fileInfoR = QFileInfo(R)
        fileInfoNIR1 = QFileInfo(NIR1)
        fileInfoNIR2 = QFileInfo(NIR2)
        fileInfoNIR3 = QFileInfo(NIR3)
        fileInfoSWIR = QFileInfo(SWIR)
        
        pathR = fileInfoR.filePath()
        pathNIR1 = fileInfoNIR1.filePath()
        pathNIR2 = fileInfoNIR2.filePath()
        pathNIR3 = fileInfoNIR3.filePath()
        pathSWIR = fileInfoSWIR.filePath()
        
        baseNameR = fileInfoR.baseName()
        baseNameNIR1 = fileInfoNIR1.baseName()
        baseNameNIR2 = fileInfoNIR2.baseName()
        baseNameNIR3 = fileInfoNIR3.baseName()
        baseNameSWIR = fileInfoSWIR.baseName()
        
        layerR = QgsRasterLayer(pathR, baseNameR)
        layerNIR1 = QgsRasterLayer(pathNIR1, baseNameNIR1)       
        layerNIR2 = QgsRasterLayer(pathNIR2, baseNameNIR2)    
        layerNIR3 = QgsRasterLayer(pathNIR3, baseNameNIR3)    
        layerSWIR = QgsRasterLayer(pathSWIR, baseNameSWIR)            

        entries = []
        
        # Define r
        r = QgsRasterCalculatorEntry()
        r.ref = 'r@1'
        r.raster = layerR
        r.bandNumber = 1
        entries.append( r )

        # Define nir1
        nir1 = QgsRasterCalculatorEntry()
        nir1.ref = 'nir@1'
        nir1.raster = layerNIR1
        nir1.bandNumber = 1
        entries.append( nir1 )
        
        # Define nir2
        nir2 = QgsRasterCalculatorEntry()
        nir2.ref = 'nir@2'
        nir2.raster = layerNIR2
        r.bandNumber = 1
        entries.append( nir2 )

        # Define nir3
        nir3 = QgsRasterCalculatorEntry()
        nir3.ref = 'nir@3'
        nir3.raster = layerNIR3
        nir3.bandNumber = 1
        entries.append( nir3 )
        
        # Define SWIR
        swir = QgsRasterCalculatorEntry()
        swir.ref = 'swir@1'
        swir.raster = layerSWIR
        swir.bandNumber = 1
        entries.append( swir )

        output = root + '\\' +'BAIS.tif'
        output2 = root + '\\' +'BAIS_10m.tif'
        width = 2*layerR.width()
        height = 2*layerR.height()
        # Process calculation with input extent and resolution
        calcBAIS = QgsRasterCalculator( '(1-( sqrt (("nir@1"*"nir@2"*"nir@3")/("r@1"))))*((("swir@1"-"nir@3")/( sqrt ("swir@1"+"nir@3" )))+1)', output, 'GTiff', layerR.extent(), (layerR.width()), (layerR.height()), entries )
        calcBAIS.processCalculation()
        
        # Process calculation with input extent and resolution
        calcBAIS_10 = QgsRasterCalculator( '(1-( sqrt (("nir@1"*"nir@2"*"nir@3")/("r@1"))))*((("swir@1"-"nir@3")/( sqrt ("swir@1"+"nir@3" )))+1)', output2, 'GTiff', layerR.extent(), width , height, entries )
        calcBAIS_10.processCalculation()

        #the BAIS.TIF and BAIS_10m.TIF files are saved in the same folder where the bands are located.
        