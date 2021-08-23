/*
Cube for testing tetrahedral elements.
*/
SetFactory("OpenCASCADE");

// Geometry
Box(1) = {-1, -1, -1, 2, 2, 2};

Physical Volume(1) = {1};

// Transfinite entities
Transfinite Line {1:12} = 2 Using Progression 1;

For cont In {1:6}
    Transfinite Surface {cont};
EndFor

Transfinite Volume {1};
