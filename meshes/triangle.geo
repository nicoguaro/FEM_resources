// Geometry for a triangle for meshing with quadrilaterals

side = 2;

// Points
Point(1) = {-side/2, 0, 0, 1.0};
Point(2) = {side/2, 0, 0, 1.0};
Point(3) = {0, side/2*Sqrt(2), 0, 1.0};
Point(4) = {0, 0, 0, 1.0};
Point(5) = {side/4, side/2*Sqrt(2)/2, 0, 1.0};
Point(6) = {-side/4, side/2*Sqrt(2)/2, 0, 1.0};
Point(7) = {0, side/2*Sqrt(2)/3, 0, 1.0};

// Lines
Line(1) = {1, 4};
Line(2) = {4, 7};
Line(3) = {7, 6};
Line(4) = {6, 1};
Line(5) = {4, 2};
Line(6) = {2, 5};
Line(7) = {5, 7};
Line(8) = {5, 3};
Line(9) = {3, 6};

// Surfaces
Line Loop(10) = {4, 1, 2, 3};
Plane Surface(11) = {10};
Line Loop(12) = {5, 6, 7, -2};
Plane Surface(13) = {12};
Line Loop(14) = {-7, 8, 9, -3};
Plane Surface(15) = {14};

// Mesh parameters
ndiv1 = 10;
ndiv2 = 10;
ndiv3 = 10;
Transfinite Line {4, 2, 6} = ndiv1 Using Progression 1;
Transfinite Line {1, 3, 8} = ndiv2 Using Progression 1;
Transfinite Line {5, 7, 9} = ndiv3 Using Progression 1;
Transfinite Surface {11};
Transfinite Surface {13};
Transfinite Surface {15};
Recombine Surface {15, 11, 13};
