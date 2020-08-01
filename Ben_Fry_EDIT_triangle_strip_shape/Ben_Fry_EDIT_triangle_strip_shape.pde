size(600, 700);
// Starting with the third vertex, connects each
// subsequent vertex to the previous two
beginShape(TRIANGLE_STRIP);
vertex(75, 40);
vertex(550, 600);
vertex(50, 150);
vertex(220, 660);
vertex(490, 70);
vertex(135, 185);
line(490, 70, 550, 600);
line(75, 40, 490, 70);
line(50, 150, 135, 185);
endShape();
