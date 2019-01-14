FEM resources
=============

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/nicoguaro/FEM_resources)

This is a repo for Finite Element resources. I have used this resources for learning (myself) or prototyping some FEM features before implement them in a bigger FEM software.

Right now it counts with some wxMaxima worksheets, where the CAS ([Computer Algebra System](http://en.wikipedia.org/wiki/Computer_algebra_system)) Maxima is used to compute analytically the elements.

It is a good idea (and practice) using CAS for manipulate algebraic expressions, like the ones that appear commonly in the derivation of FEM (or other numerical methods). Two examples: Prof. Carlos Felipa suggest to use CAS for it (and uses Mathematica in its [Introductory FEM course](http://www.colorado.edu/engineering/cas/courses.d/IFEM.d/)), Prof. Alan Bower presents some Maple codes for FEM in its online book [Applied Mechanics of Solids](http://solidmechanics.org/FEA.php).

TODO: Add Python code with matrices generated "automatically" from Maxima.


Installation
============
For wxMaxima worksheets (.wxm files) a wxMaxima (and Maxima) installation is needed. For Windows the Maxima [installer](http://sourceforge.net/projects/maxima/files/Maxima-Windows/) already contains wxMaxima. In Linux and Mac OS they should be installed separately: [Maxima](http://sourceforge.net/projects/maxima/files/), [wxMaxima](http://andrejv.github.io/wxmaxima/). Once wxMaxima is installed the worksheets can be downloaded and executed ([10 minutes Maxima](http://andrejv.github.io/wxmaxima/tutorials/10minute.zip), [spanish version](http://andrejv.github.io/wxmaxima/tutorials/10minute_es.zip)).


List of files
=============
This will change in the future (probably?). But the current list of files is:

Maxima
------
* `Analytical FEM.wxm`: a Finite Element Method code written in Maxima language. It illustrates some of the steps in a FEM code but the use of a CAS ease the process.
* `Elemental Matrices.wxm`: computes stiffness and mass matrices for common types of (2D) elements.

Python
------
* [`Analytical FEM.ipynb`](http://nbviewer.ipython.org/github/nicoguaro/FEM_resources/blob/master/Analytic%20FEM.ipynb): a Finite Element Method code written in SymPy. It illustrates some of the steps in a FEM code but the use of a CAS ease the process.
* [`Bilinear interpolation plots`](http://nbviewer.ipython.org/github/nicoguaro/FEM_resources/blob/master/Bilinear%20interpolation%20plots.ipynb): Example of interpolation using bilinear elements.
* [`Circular_membrane.ipynb`](http://nbviewer.ipython.org/github/nicoguaro/FEM_resources/variational/blob/master/Circular_membrane.ipynb.ipynb): Weighted residual method illustration for a circular membrane.
* [`FEM_4Nodes.ipynb`](http://nbviewer.jupyter.org/github/nicoguaro/FEM_resources/blob/master/FEM_4Nodes.ipynb): Notebook that computes analytically the stiffness and mass matrices for a 4 node element with undistorted shape.
common procedure for (explicit) time marching algorithms.
* [`Hermite_interpolation.ipynb`](http://nbviewer.jupyter.org/github/nicoguaro/FEM_resources/blob/master/Hermite_interpolation.ipynb): Piecewise Hermite interpolation.
* [`Lumped mass FEM.ipynb`](http://nbviewer.jupyter.org/github/nicoguaro/FEM_resources/blob/master/Lumped%20mass%20FEM.ipynb): computes lumped mass matrices. A
* [`poly_ritz.ipynb`](http://nbviewer.ipython.org/github/nicoguaro/FEM_resources/variational/blob/master/poly_ritz.ipynb): IPython Notebook with Vibration modes of membranes with convex polygonal shape.
* [`XFEM_enrichment.ipynb`](http://nbviewer.jupyter.org/github/nicoguaro/FEM_resources/blob/master/XFEM_enrichment.ipynb): Notebook  for enrichment basis functions for XFEM.


License
=======
* Text and multimedia is under Creative Commons Attribution 4.0 (CC-by 4.0) https://creativecommons.org/licenses/by/4.0/
* Code is under MIT License http://opensource.org/licenses/MIT
