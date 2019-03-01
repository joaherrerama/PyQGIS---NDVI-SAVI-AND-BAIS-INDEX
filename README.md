# PyQGIS---NDVI-SAVI-AND-BAIS-INDEX
This script allow you calculate NDVI, SAVI and BAIS (Burn Area) index in QGIS (Works as a loop from a folder)

# Instruction
 
In order to optimize time, the follow script allow you to calculate three basic index:
 
## SAVI (Soil Adjusted Vegetation Index)
 
Empirically derived NDVI products have been shown to be unstable, varying with soil colour, soil moisture, and saturation effects from high density vegetation. In an attempt to improve NDVI, Huete [1] developed a vegetation index that accounted for the differential red and near-infrared extinction through the vegetation canopy. The index is a transformation technique that minimizes soil brightness influences from spectral vegetation indices involving red and near-infrared (NIR) wavelengths.

![alt text](https://cdn-images-1.medium.com/max/1600/1*HzbTbt6yrFxMhW0cHBl4jg.png)
 
## NDVI (Normalized Difference Vegetation Index)

Normalized Difference Vegetation Index (NDVI) quantifies vegetation by measuring the difference between near-infrared (which vegetation strongly reflects) and red light (which vegetation absorbs). NDVI always ranges from -1 to +1. But there isn’t a distinct boundary for each type of land cover.
<p align="center">
  <img src="https://gisgeography.com/wp-content/uploads/2014/12/ndvi-formula-300x123.png">
</p>

## BAIS (Burned Area Index for Sentinel 2)

Accurate and rapid mapping of fire damaged areas is fundamental to support fire management, account for environmental loss, define planning strategies and monitor the restoration of vegetation. Under climate change conditions, drought severity may trigger tough fire regimes, in terms of number and dimension of fires. In order to deliver rapid information about areas damaged by fires, Burned Area Index (BAI), Normalized Burn Ratio (NBR), and their relative versions have been largely employed in the past to map burned areas from high resolution optical satellite data. The new MSI sensor aboard Sentinel-2 satellites carries more spectral information recorded in the red-edge spectral region, opening the way to the development of new indices for burned area mapping. This study present a newly developed Burned Area Index for Sentinel-2 (BAIS2), based on Sentinel-2 spectral bands, to detect burned areas at 20 m spatial resolution and the design of a processor developed to perform post-fire mapping using Sentinel-2 data. The new index has been tested on various study cases in Italy for summer 2017 fires, and results show a good performance of the index and highlighted critical issues related to the Sentinel-2 data processing.

<p align="center">
  <img src="">
</p>

# Parameter
to run the script you need just the input folder, and all the raster will be saved in the folder where the bads were taked. Also i have to be clear that the script run on QGIS platform.
 
# Steps

- Open QGIS
- In the GUI, click in the Python Module
- then just click in the script module that seems to be like a piece of paper with a pen 
- and just load the script or copy and paste it.

# *Thanks and hope could be helpful to you*

*Autor: Jorge Andrés Herrera Maldonado*
*FDCS PROJECT*

