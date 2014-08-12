x = linspace(0,10,1000);
y = sin(pi*x);

plot3(x, y, 0*x, 'g', 'LineWidth',2);
hold on
plot3(x, 0*x, y, 'b', 'LineWidth',2);

