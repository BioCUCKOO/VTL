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

    A 4 minutes fly movements tracking video in the mp4 format.

* demo-v_1.vtl

    The raw vtl result file of demo-v.mp4, processed by vtl.py.

* demo-v_1-order.vtl

    The sorted vtl result file of demo-v_1.vtl, processed by dataorder.py.
