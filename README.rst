====================
Gaussian Density Model
====================

Segmentation algorithm of urban environment, we used the LiDAR Velodyne 64E. The algorithm read and write type files csv.

Input: cloud points (x,y,z,d) where d is density and (x,y,z) without density.

Ouput: cloud points (x,y,z,d) objects segmentation.

==================


Required Modules:
====================

  * PIP      
  * Numpy
  * Math
  * Pandas
  * CSV
  * Matplotlib
  * Intertools

Installation:
==============================

``$ sudo apt update``

``$ sudo apt upgrade``

``$ pip install numpy``

``$ pip install math``

``$ pip install pandas``

``$ pip install python-csv``

``$ pip install matplotlib``

``$ pip install itertools-s``



Example:
========

``$ python GDM.py --help``

``$ python GDM.py -i iValue``


Cite article (In review):
========

@article{article,
author = {A. R. Pedraza, J. J. G. Barbosa, K. L. F. Rodríguez, A. I. G. Moreno and E. A. G. Barbosa},
year = {2019},
month = {},
pages = {},
title = {Free-form object segmentation in urbanenvironments using Gaussian Density Model},
volume = {},
journal = {Latin America Transactions, IEEE (Revista IEEE America Latina},
doi = {10.1109/TLA.}
}

  .. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3
