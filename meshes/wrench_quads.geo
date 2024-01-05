/*
Wrench subdivided to create a fully quadrilateral mesh
*/

// Geometrical parameters
rad1 = 40;
rad2 = 30;
rad3 = 20;
width = 40;
length = 300;
open = 30;
open_len = 50;
ang = Pi/12;

// Mesh parameters
size = 2;

// Points without rotation
P3_x = -Sqrt(rad1^2 - open^2/4);
P3_y = -open/2;
P4_x = Sqrt(rad1^2 - width^2/4);
P4_y = -width/2;
P5_x = Sqrt(rad1^2 - width^2/4);
P5_y = width/2;
P6_x = -Sqrt(rad1^2 - open^2/4);
P6_y = open/2;
P7_x = P6_x + open_len;
P7_y = P6_y;
P8_x = P3_x + open_len;
P8_y = P3_y;
P9_x = length - Sqrt(rad2^2 - width^2/4);
P9_y = -width/2;
P10_x = length - Sqrt(rad2^2 - width^2/4);
P10_y = width/2;
P11_x = length + rad2;
P11_y = 0;

// Load side
P12_x = length + rad3;
P12_y = 0;
ang_int = Atan2(width/2, Sqrt(rad2^2 - width^2/4));
P13_x = length - rad3*Cos(ang_int);
P13_y = -rad3*Sin(ang_int);
P14_x = length - rad3*Cos(ang_int);
P14_y = rad3*Sin(ang_int);

// Encastre side
P15_x = 0;
P15_y = 5/8*rad1;
P16_x = 0;
P16_y = -5/8*rad1;
P17_x = 0.5 * (P6_x + P7_x);
P17_y = P6_y;
P18_x = P17_x;
P18_y = P3_y;
P19_x = P17_x;
P19_y = Sqrt(rad1^2 - P17_x^2);
P20_x = P17_x;
P20_y = -Sqrt(rad1^2 - P17_x^2);
P21_x = 0.5 * (P5_x + P7_x);
P21_y = 0.5 * (P5_y + P7_y);
P22_x = 0.5 * (P4_x + P8_x);
P22_y = 0.5 * (P4_y + P8_y);

// Points
Point(1) = {0, 0, 0, size};
Point(2) = {length, 0, 0, size};
Point(3) = {P3_x, P3_y, 0, size};
Point(4) = {P4_x, P4_y, 0, size};
Point(5) = {P5_x, P5_y, 0, size};
Point(6) = {P6_x, P6_y, 0, size};
Point(7) = {P7_x, P7_y, 0, size};
Point(8) = {P8_x, P8_y, 0, size};
Point(9) = {P9_x, P9_y, 0, size};
Point(10) = {P10_x, P10_y, 0, size};
Point(11) = {P11_x, P11_y, 0, size};
Point(12) = {P12_x, P12_y, 0, size};
Point(13) = {P13_x, P13_y, 0, size};
Point(14) = {P14_x, P14_y, 0, size};
Point(15) = {P15_x, P15_y, 0, size};
Point(16) = {P16_x, P16_y, 0, size};
Point(17) = {P17_x, P18_y, 0, size};
Point(18) = {P18_x, P17_y, 0, size};
Point(19) = {P19_x, P19_y, 0, size};
Point(20) = {P20_x, P20_y, 0, size};
Point(21) = {P21_x, P21_y, 0, size};
Point(22) = {P22_x, P22_y, 0, size};

// Rotate all points
Rotate {{0, 0, 1}, {0, 0, 0}, ang} {Point{2:22};}

// Lines

// Top encastre
Circle(1) = {3, 1, 20};
Circle(2) = {20, 1, 4};
// Bottom encastre
Circle(3) = {5, 1, 19};
Circle(4) = {19, 1, 6};
Circle(5) = {9, 2, 11};
Circle(6) = {11, 2, 10};
Circle(7) = {13, 2, 12};
Circle(8) = {12, 2, 14};
Circle(9) = {14, 2, 13};
Line(10) = {3, 17};
Line(11) = {17, 8};
Line(12) = {8, 7};
Line(13) = {7, 18};
Line(14) = {18, 6};
Line(15) = {4, 9};
Line(16) = {5, 10};

// Subdivision lines
Circle(17) = {4, 1, 5};
Line(18) = {18, 15};
Line(19) = {15, 19};
Line(20) = {7, 21};
Line(21) = {21, 5};
Line(22) = {21, 15};
Line(23) = {17, 16};
Line(24) = {16, 20};
Line(25) = {8, 22};
Line(26) = {22, 4};
Line(27) = {16, 22};
Circle(28) = {10, 2, 9};
Line(29) = {12, 11};
Line(30) = {9, 13};
Line(31) = {14, 10};
Line(32) = {22, 21};

// Surfaces
Curve Loop(1) = {1, -24, -23, -10};
Curve Loop(2) = {24, 2, -26, -27};
Curve Loop(3) = {23, 27, -25, -11};
Curve Loop(4) = {-12, -20, 32, 25};
Curve Loop(5) = {-32, -21, 17, 26};
Curve Loop(6) = {-13, -18, 22, 20};
Curve Loop(7) = {-14, 4, 19, 18};
Curve Loop(8) = {-22, -19, 3, 21};
Curve Loop(9) = {-17, -16, -28, 15};
Curve Loop(10) = {28, 30, -9, 31};
Curve Loop(11) = {5, -29, -7, -30};
Curve Loop(12) = {29, 6, -31, -8};

//
For cont In {1:12}
  Plane Surface(cont) = {cont};
EndFor


// Physical groups
Physical Line(1) = {10:14};
Physical Line(2) = {7, 9};
Physical Surface(3) = {1:12};

// Meshing parameters

// Line division
rad1_div1 = 20;
rad1_div2 = 20;
rad1_div3 = 20;
Transfinite Curve {1, 23, 25, 20, 18, 4} = rad1_div1 Using Progression 1;
Transfinite Curve {10, 24, 26, 21, 19, 14} = rad1_div2 Using Progression 1;
Transfinite Curve {2, 27, 11, 13, 22, 3} = rad1_div3 Using Progression 1;

width_div = 20;
len_div = 100;
Transfinite Curve {12, 32, 17, 28, 9, 7} = width_div Using Progression 1;
Transfinite Curve {16, 15} = len_div Using Progression 1;

arc2_div = 30;
rad2_div = 10;
Transfinite Curve {6, 8, 7, 5} = arc2_div Using Progression 1;
Transfinite Curve {30, 31, 29} = rad2_div Using Progression 1;

// Surface meshing
Transfinite Surface {1:12};
Recombine Surface {1:12};
