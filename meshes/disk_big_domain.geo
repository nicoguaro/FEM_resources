/*
Disk embedded in a big domain.

Author: Nicolás Guarín-Zapata
Date: November 2021
*/
rad = 1.0;
rad2 = 10.0;
size = 1.0;


// Points
Point(1) = {0, 0, 0, size};
Point(2) = {rad*Sqrt(2)/2, rad*Sqrt(2)/2, 0, size};
Point(3) = {-rad*Sqrt(2)/2, rad*Sqrt(2)/2, 0, size};
Point(4) = {-rad*Sqrt(2)/2, -rad*Sqrt(2)/2, 0, size};
Point(5) = {rad*Sqrt(2)/2, -rad*Sqrt(2)/2, 0, size};
Point(6) = {rad*Sqrt(2)/4, rad*Sqrt(2)/4, 0, size};
Point(7) = {-rad*Sqrt(2)/4, rad*Sqrt(2)/4, 0, size};
Point(8) = {-rad*Sqrt(2)/4, -rad*Sqrt(2)/4, 0, size};
Point(9) = {rad*Sqrt(2)/4, -rad*Sqrt(2)/4, 0, size};
Point(10) = {rad2*Sqrt(2)/2, rad2*Sqrt(2)/2, 0, size};
Point(11) = {-rad2*Sqrt(2)/2, rad2*Sqrt(2)/2, 0, size};
Point(12) = {-rad2*Sqrt(2)/2, -rad2*Sqrt(2)/2, 0, size};
Point(13) = {rad2*Sqrt(2)/2, -rad2*Sqrt(2)/2, 0, size};

// Lines
Line(1) = {8, 9};
Line(2) = {9, 6};
Line(3) = {6, 7};
Line(4) = {7, 8};
Circle(5) = {5, 1, 2};
Circle(6) = {2, 1, 3};
Circle(7) = {3, 1, 4};
Circle(8) = {4, 1, 5};
Circle(9) = {13, 1, 10};
Circle(10) = {10, 1, 11};
Circle(11) = {11, 1, 12};
Circle(12) = {12, 1, 13};
Line(13) = {9, 5};
Line(14) = {6, 2};
Line(15) = {7, 3};
Line(16) = {8, 4};
Line(17) = {5, 13};
Line(18) = {2, 10};
Line(19) = {3, 11};
Line(20) = {4, 12};

// Surfaces
Curve Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Curve Loop(2) = {8, -13, -1, 16};
Plane Surface(2) = {2};
Curve Loop(3) = {13, 5, -14, -2};
Plane Surface(3) = {3};
Curve Loop(4) = {14, 6, -15, -3};
Plane Surface(4) = {4};
Curve Loop(5) = {15, 7, -16, -4};
Plane Surface(5) = {5};
Curve Loop(6) = {17, 9, -18, -5};
Plane Surface(6) = {6};
Curve Loop(7) = {18, 10, -19, -6};
Plane Surface(7) = {7};
Curve Loop(8) = {19, 11, -20, -7};
Plane Surface(8) = {8};
Curve Loop(9) = {20, 12, -17, -8};
Plane Surface(9) = {9};

// Physical groups
Physical Curve(1) = {8, 5, 6, 7};      // Inner interface
Physical Curve(2) = {12, 9, 10, 11};   // Exterior line
Physical Surface(3) = {5, 4, 1, 3, 2}; // Inner surfaces
Physical Surface(4) = {7, 8, 9, 6};    // Exterior surfaces

// Mesh parameters
ndiv_arc = 11;
ndiv_rad_in = 11;
ndiv_rad_ext = 11;
Transfinite Curve {1:12} = ndiv_arc Using Progression 1;
Transfinite Curve {13:16} = ndiv_rad_in Using Progression 1;
Transfinite Curve {17:20} = ndiv_rad_ext Using Progression 1.5;
Transfinite Surface {1:9};
Recombine Surface {1:9};

