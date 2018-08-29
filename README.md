## TEMPORARY 

The entire CodingDonky repo is going to be removed soon. It serves only as a testing ground for Alex Newberry.
Everything will be cleaned up and ported over to the ActiveBrainAtlas repo. Some files I will need to be extra
careful with as I have altered them significantly.

Files that have been altered:
  - preprocess_cshl_data_v2_neurotrace.ipynb
  - preprocess_ucsd_data_v2.ipynb
  - brightness_correction.ipynb
  - distributed_utilities.py
  - utilities2015.py

<br><br>

Naming conventions are the each file has a unique filename, FILENAME. Every different transform of the file will have the naming convention FILE_SUFFIX where SUFFIX is an abbreviated description of the file's state.

Files will always be in *.tif form unless otherwise stated. One important exception is that the raw files given to us are typically in the format *_raw.jp2.

Examples:
- [FILENAME] = MD662&661-F1-2017.06.02-17.07.55_MD662_1_0001.jp2
- FILE_STEP1 = MD662&661-F1-2017.06.02-17.07.55_MD662_1_0001_raw.tif
- FILE_STEP2 = MD662&661-F1-2017.06.02-17.07.55_MD662_1_0001_raw_Ntb.tif
- FILE_STEP3 = MD662&661-F1-2017.06.02-17.07.55_MD662_1_0001_thumbnail_Ntb.tif

Preprocessing Steps:
1) raw (.jp2) -> raw_Ntb (.tif): extract_channel
2) raw_Ntb -> thumbnail_Ntb: rescale
3) thumbnail_Ntb -> thumbnail_NtbNormalized: normalize_intensity
4) Compute transforms using thumbnail_NtbNormalized: align + compose
5) Supply prep1_thumbnail_mask
6) prep1_thumbnail_mask -> thumbnail_mask: warp
7) raw_Ntb -> raw_NtbNormalizedAdaptiveInvertedGamma: brightness_correction
8) Compute prep5 (alignedWithMargin) cropping box based on prep1_thumbnail_mask
9) raw_NtbNormalizedAdaptiveInvertedGamma -> prep5_raw_NtbNormalizedAdaptiveInvertedGamma: align + crop
10) thumbnail_NtbNormalized -> prep5_thumbnail_NtbNormalized: align + crop
11) prep5_raw_NtbNormalizedAdaptiveInvertedGamma -> prep5_thumbnail_NtbNormalizedAdaptiveInvertedGamma: rescale
12) Specify prep2 (alignedBrainstemCrop) cropping box
13) prep5_raw_NtbNormalizedAdaptiveInvertedGamma -> prep2_raw_NtbNormalizedAdaptiveInvertedGamma: crop
14) prep2_raw_NtbNormalizedAdaptiveInvertedGamma -> prep2_raw_NtbNormalizedAdaptiveInvertedGammaJpeg: compress_jpeg

<br><br>


* Doc: documentation
* src: code

## Guides
- [Alex User Guide](doc/RunningFiles.md)
  - Running Guide made by AlexN to assist with running the code [INC]
- **[Historical]** [Yuncong User Guide](doc/User%20Manuals/UserGuide.md)
  - User Guide made by Yuncong to assist with running the code

- **[Historical/Incomplete]** [Dev Guide](doc/DeveloperGuide.md)
  - Incomplete to-be guide of entire running process
- **[Historical]** [Registration Steps](doc/Analysis.md)
  - Guide for Registration with list of relevant scripts
- **[Historical]** [Old README](doc/old_readme.md)
  - Yuncong's old README

## Server Information
- [File Transfer](doc/TransferFiles.md)
  - Guide for transferring files to/from AWS S3 and Birdstore
- [AWS Instructions](doc/writeup/AWS_instruction.md)
  - AWS instruction manual

## File Organization
- **[Incomplete]** [S3 File Organization](doc/writeup/S3_file_organization.md)
  - Naming conventions in S3 storage [INC]
- [Stack Directories](doc/Brain_stack_directories.md)
  - Description of every stack, all relevant information

## Machine Learning Documents
- [Bayesian Parameters](doc/writeup/bayesian.md)
  - Parameters and associated uncertainty in Atlas building process
- [Uncertainty](doc/writeup/zscore_hessian.md)
  - Z-score and Hessians used to quantify uncertainty
