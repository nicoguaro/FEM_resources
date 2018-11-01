/*
Geometry for a triangle with a hole intended to meshed with quadrilaterals
*/

side = 2;
radius = 0.3;

// Points
Point(1) = {-side/2, 0, 0, 1.0};
Point(2) = {side/2, 0, 0, 1.0};
Point(3) = {0, side/2*Sqrt(2), 0, 1.0};
Point(4) = {0, 0, 0, 1.0};
Point(5) = {side/4, side/2*Sqrt(2)/2, 0, 1.0};
Point(6) = {-side/4, side/2*Sqrt(2)/2, 0, 1.0};
Point(7) = {0, side/2*Sqrt(2)/3, 0, 1.0};
Point(8) = {0, side/2*Sqrt(2)/3 - radius, 0, 1.0};
Point(9) = {radius*Cos(Pi/6), side/2*Sqrt(2)/3 + radius*Sin(Pi/6), 0, 1.0};
Point(10) = {-radius*Cos(Pi/6), side/2*Sqrt(2)/3 + radius*Sin(Pi/6), 0, 1.0};
Point(11) = {radius*Cos(Pi/6), side/2*Sqrt(2)/3 - radius*Sin(Pi/6), 0, 1.0};
Point(12) = {-radius*Cos(Pi/6), side/2*Sqrt(2)/3 - radius*Sin(Pi/6), 0, 1.0};
Point(13) = {0, side/2*Sqrt(2)/3 + radius, 0, 1.0};

// Lines
Line(1) = {1, 4};
Line(2) = {4, 2};
Line(3) = {2, 5};
Line(4) = {5, 3};
Line(5) = {3, 6};
Line(6) = {6, 1};
Line(7) = {4, 8};
Line(8) = {5, 9};
Line(9) = {6, 10};
Line(10) = {12, 1};
Line(11) = {11, 2};
Line(12) = {13, 3};
Circle(13) = {8, 7, 11};
Circle(14) = {11, 7, 9};
Circle(15) = {9, 7, 13};
Circle(16) = {13, 7, 10};
Circle(17) = {10, 7, 12};
Circle(18) = {12, 7, 8};

// Surfaces
Line Loop(19) = {10, 1, 7, -18};
Plane Surface(20) = {19};
Line Loop(21) = {-7, 2, -11, -13};
Plane Surface(22) = {21};
Line Loop(23) = {11, 3, 8, -14};
Plane Surface(24) = {23};
Line Loop(25) = {4, -12, -15, -8};
Plane Surface(26) = {25};
Line Loop(27) = {5, 9, -16, 12};
Plane Surface(28) = {27};
Line Loop(29) = {6, -10, -17, -9};
Plane Surface(30) = {29};

// Mesh parameters
ndiv = 10;
Transfinite Line {10, 7, 11, 8, 12, 9} = ndiv Using Progression 1;
Transfinite Line {6, 17} = ndiv Using Progression 1;
Transfinite Line {5, 16} = ndiv Using Progression 1;
Transfinite Line {4, 15} = ndiv Using Progression 1;
Transfinite Line {3, 14} = ndiv Using Progression 1;
Transfinite Line {13, 2} = ndiv Using Progression 1;
Transfinite Line {18, 1} = ndiv Using Progression 1;
Transfinite Surface {30};
Transfinite Surface {20};
Transfinite Surface {22};
Transfinite Surface {24};
Transfinite Surface {26};
Transfinite Surface {28};
Recombine Surface {30, 28, 26, 24, 22, 20};
