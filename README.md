FEM resources
=============

This is a repo for Finite Element resources. I have used this resources for learning (myself) or prototyping some FEM features before implement them in a bigger FEM software.

Right now it counts with some wxMaxima worksheets, where the CAS Maxima is used to compute analytically the elements.


Installation
============
For wxMaxima worksheets (.wxm files) a wxMaxima (and Maxima) installation is needed. For Windows the Maxima [installer](http://sourceforge.net/projects/maxima/files/Maxima-Windows/) already contains wxMaxima. In Linux and Mac OS they should be installed separately: [Maxima](http://sourceforge.net/projects/maxima/files/), [wxMaxima](http://andrejv.github.io/wxmaxima/). Once wxMaxima is installed the worksheets can be downloaded and executed ([10 minutes Maxima](http://andrejv.github.io/wxmaxima/tutorials/10minute.zip), [spanish version](http://andrejv.github.io/wxmaxima/tutorials/10minute_es.zip)).


List of files
=============
This will change in the future (probably?). But the current list of files is:
* `Analytical FEM.wxm`: a Finite Element Method code written in Maxima language. It illustrates some of the steps in a FEM code but the use of a CAS ease the process.
* `Elemental Matrices.wxm`: computes stiffness and mass matrices for common types of (2D) elements.
* `FEM_8node_element.wxm`: computes (analytically) stiffnesss and mass matrices for the most common element serendipity of 8 nodes.
* `lumped_mass_FEM.wxm`: computes lumped mass matrices. A common procedure for (explicit) time marching algorithms.


License
=======
* Text and multimedia is under Creative Commons Attribution 3.0 United States License (CC-by) http://creativecommons.org/licenses/by/3.0/us.
* Code is under MIT Licenes http://opensource.org/licenses/MIT
