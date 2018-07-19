# Alex N's notes for running through the code

## Pre-Preprocessing
Files will come in raw as .CZI files or Nanozoomer files (.NDPI). NDPI files are from CSHL and can only be converted into JP2000 directly which is why that is how the raw, lossless data is stored. Yuncong converts these into TIFF files so they are useable but it requires conversion of 16bit to 8bit and Hannah said nobody understands how that works nor has Yuncong told anyone.

These files need to be converted to .TIFF files and have all of the surrounding, non-brain, area cut out of the image so that it does not slow down the rest of the code or interfere with anything.

## Preprocessing
### Neurotrace (CSHL)
Requires files from pre-preprocessing step including [name]_anchor.txt, [name]_sorted_filenames.txt, and a collection of other text, json files, and pkl files (< I will elaborate on this soon).

Neutrace data typically is stained with another indicator, data has multiple channels that are a part of the preprocessing stage.

Run **preprocess_cshl_data_v2_neurotrace.ipynb**, it will complete every step of the preprocessing stage for neurotrace brains as outlined below:
#### preprocess_cshl_data_v2_neurotrace.ipynb
* Prepare data
  - set 'stack' equal to brain name, make sure raw files are on S3:///mousebrainatlas-rawdata/...
* Download raw scanner files from S3 and Specify raw file locations
  - Specify where to download all raw files, for me was `~/MD###/`
* Convert raw JPEG2000 to TIFF format **[JP2 -> TIF]**
  - CSHL uses NanoZoomer, gives CSHL format which apparently can onlly be converted to jp2
  - input:  `~/MD###/*.jp2`  (Location of ALL raw files, defined earlier)
  - output: `~/CSHL_data_processed/MD###/MD###_raw/*_raw.tif`
  - NOTE: may have discrepency with defined input/output directories
* Extract Neurotrace channel **[raw -> raw_Ntb]**
  - input:  `~/CSHL_data_processed/MD###/MD###_raw/*_raw.tif`
  - output: `~/CSHL_data_processed/MD###/MD###_raw_Ntb/*_raw_Ntb.tif`
* Generate thumbnails and linearly contrast stretch **[raw_Ntb -> thumbnail_Ntb -> thumbnail_NtbNormalized]**
  - Requires file `MD###_sorted_filenames.txt` in `~/CSHL_data_processed/MD###/` among others
    - List of necessary pre-preprocess files here [NEED TO ADD]
  - input:   ----`~/CSHL_data_processed/MD###/MD###_raw_Ntb/*_raw_Ntb.tif`
  - output1: `~/CSHL_data_processed/MD###/MD###_thumbnail_Ntb/*_thumbnail_Ntb.tif`
  - output2: `~/CSHL_data_processed/MD###/MD###_thumbnail_NtbNormalized/*_thumbnail_NtbNormalized.tif`
* Compute Transforms using thumbnail_NtbNormalized
#### Align.py
  - Use Elastix to align, computing transforms between adjacent sections
    - Gives *pairwise* transforms
  - Next step is to Compose the pairwise transformations, requires anchor slide
    - Then for each section (=slide), multiply all the pairwise transforms between this section and the anchor section. This gives each section a X-to-anchor transform. The X-to-anchor transforms for all sections are stored in a pkl file.
      - Yuncong: "This is the basics, though partially innacurate"
    - REAL STEPS
      - Run Elastix code, pairwise transforms should work ~97% of the time. 
        - output: `~/CSHL_data_processed/MD###/MD###_elastix_output/`
      - Correct the failed 3% with a GUI and select an anchor slide
        - Gui script: `gui/preprocess_tool_v3.py`
        - output1: `~/CSHL_data_processed/MD###/MD###_custom_transform/`
          - Corrected pairwise transforms done by hand
        - output2: `~/CSHL_data_processed/MD###/MD###_anchor.txt`
          - Name of the anchor slice. Every other slice will be rigidly transformed based on the anchor
        - output3: `~/CSHL_data_processed/MD###/MD###_transformTo_*.pkl`
          - Transformation matrices for every stack, stored as Python Dictionary
#### Compose.py
      - Apply transformations
        - output: `~/CSHL_data_processed/MD###/MD###_prep1_thumbnail_normalized/`
#### Warp.py
* Generate Thumbnail mask
  - Requires GUI (Active Contour Algorithm), using this program, you draw rough outlines, which are then shrinked by an algorithm called "active contour" to tightly fit the tissue content. [SKIP FOR NOW]
    - output: `prep1_thumbnail_mask`



### Thionin (UCSD)
Not yet started.
### Detection/Classification
Not yet started.
### Registration/3D Construction
Not yet started.


## Setting up environment
metadata.py
distributed_utilities.py
