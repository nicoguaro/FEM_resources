/*

*/
rad = 1.0;
height = 2*rad;


// Points
Point(1) = {0, 0, 0, 1.0};
Point(2) = {-rad, 0, 0, 1.0};
Point(3) = {rad, 0, 0, 1.0};
Point(4) = {-rad, height, 0, 1.0};
Point(5) = {rad, height, 0, 1.0};
Point(6) = {-rad/2, 0, 0, 1.0};
Point(7) = {rad/2, 0, 0, 1.0};
Point(8) = {-rad/2, height, 0, 1.0};
Point(9) = {rad/2, height, 0, 1.0};
Point(10) = {-rad/2.5, -rad/2, 0, 1.0};
Point(11) = {rad/2.5, -rad/2, 0, 1.0};
Point(12) = {-rad*Cos(Pi/4), -rad*Sin(Pi/4), 0, 1.0};
Point(13) = {rad*Cos(Pi/4), -rad*Sin(Pi/4), 0, 1.0};

// Lines
Line(1) = {2, 6};
Line(2) = {6, 7};
Line(3) = {7, 3};
Line(4) = {3, 5};
Line(5) = {5, 9};
Line(6) = {9, 8};
Line(7) = {8, 4};
Line(8) = {4, 2};
Line(9) = {6, 10};
Line(10) = {10, 11};
Line(11) = {11, 7};
Line(12) = {10, 12};
Line(13) = {11, 13};
Line(14) = {6, 8};
Line(15) = {7, 9};
Circle(16) = {2, 1, 12};
Circle(17) = {12, 1, 13};
Circle(18) = {13, 1, 3};

// Surfaces
Line Loop(1) = {7, 8, 1, 14};
Plane Surface(1) = {1};
Line Loop(2) = {2, 15, 6, -14};
Plane Surface(2) = {2};
Line Loop(3) = {3, 4, 5, -15};
Plane Surface(3) = {3};
Line Loop(4) = {1, 9, 12, -16};
Plane Surface(4) = {-4};
Line Loop(5) = {10, 13, -17, -12};
Plane Surface(5) = {-5};
Line Loop(6) = {2, -11, -10, -9};
Plane Surface(6) = {-6};
Line Loop(7) = {11, 3, -18, -13};
Plane Surface(7) = {-7};


// Mesh parameters
ndiv_cent = 10;
ndiv_lat = 5;
ndiv_height = 20;
ndiv_arc = 5;
Transfinite Line {8, 14, 15, 4} = ndiv_height Using Progression 1;
Transfinite Line {7, 1, 12, 13, 3, 5} = ndiv_lat Using Progression 1;
Transfinite Line {16, 9, 11, 18} = ndiv_arc Using Progression 1;
Transfinite Line {17, 10, 2, 6} = ndiv_cent Using Progression 1;
Transfinite Surface {1};
Transfinite Surface {2};
Transfinite Surface {3};
Transfinite Surface {7};
Transfinite Surface {6};
Transfinite Surface {4};
Transfinite Surface {5};
