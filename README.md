# VTL
**Note**: For experimental verification, we developed a video tracking instrument that can simultaneously track the movements of each fly in a group for days.

## Requirements

The main requirements are listed below:

* Python 3.5.6
* NumPy
* OpenCV 3.4.1.15
* Skimage
* Matplotlib
* Numba

## The description of VTL source codes and files

* vtl.py

    The code is used for videos transforming into a data point in a two-dimensional coordinate system.

* dataorder.py

    The code is used for raw wo-dimensional coordinate system data ordering.

* demo-v.mp4

    A 4 minutes fly movements tracking video in the mp4 format. The video file can be downloaded at https://vtl.biocuckoo.cn/download.html

* demo-v_1.vtl

    The raw vtl result file of demo-v.mp4, processed by vtl.py.

* demo-v_1-order.vtl

    The sorted vtl result file of demo-v_1.vtl, processed by dataorder.py.

## OS Requirements

Above codes have been tested on the following systems:

* Windows: Windows7, Windos10
* Linux: CentOS linux 7.8.2003

## Hardware Requirements

All codes and softwares could run on a "normal" desktop computer, no non-standard hardware is needed.

## Installation guide

All codes can run directly on a "normal" computer with Python 3.5.6 installed, no extra installation is required.

## Instruction

For users who want to run vtl in own computer, you should first use the **vtl.py** to process the **demo-v.mp4 file** to get the raw vtl file **demo-v_1.vtl**. Then, **dataorder.py** was used to sort the raw vtl files to get the ordered vtl file **demo-v_1-order.vtl** that stored the location of each fruit fly in each frame.

## Additional information
**Note that the version of media transcoder OpenCV should be 3.4.1.15. Otherwise, the Python program may report error.**
