size(850, 550);
smooth();
strokeWeight(1);
for (int i = 20; i < 850; i += 30) {
line(i, 0, i + i/2, 550);
}
strokeWeight(3);
for (int i = 15; i < 850; i += 35) {
line(i, 550, i + i/2, 0);
}
smooth();
noFill();
stroke(102);
for (int y = 100; y <= height-20; y += 100) {
for (int x = 100; x <= width-20; x += 100) {
ellipse(x, y, 50, 50);
// Draw a line to the center of the display
strokeWeight(2);
line(x, y, 425, 275);
}
}
