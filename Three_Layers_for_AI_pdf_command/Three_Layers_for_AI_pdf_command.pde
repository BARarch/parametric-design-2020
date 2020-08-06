import processing.pdf.*;

void setup () {
size(1700, 1100, PDF, "Three_ Layers_for_AI.pdf");
}
void draw() {
smooth();
strokeWeight(15);
stroke(22, 75, 240);
noFill();
triangle(10, 10, 250, 10, 10, 250);
triangle(250, 10, 500, 10, 260, 350);
triangle(250, 10, 260, 350, 10, 250);
triangle(500, 10, 800, 10, 650, 500);
line(650, 500, 260, 350);
line(10, 250, 10, 400);
line(10, 400, 650, 500);
triangle(650, 500, 10, 900, 10, 400);
triangle(10, 900, 10, 1090, 500, 1090);
line( 500, 1090, 650, 500);
triangle(650, 500, 1100, 1090, 1500, 300);
line(500, 1090, 1100, 1090);
line(800, 10, 1500, 300);
line(1400, 10, 1500, 300);
line (800, 10, 1400, 10);
line(1400, 10, 1690, 10);
line(1690, 10, 1500, 300);
line(1500, 300, 1690, 500);
line(1690, 10, 1690, 500);
line(1690, 500, 1100, 1090);
line(1100, 1090, 1690, 1090);
line(1690, 1090, 1690, 500);
stroke(0);
strokeWeight(4);
for (float x = 15; x < 1700; x *= 1.1) {
line(x, 10, x, 1090);
}
strokeWeight(8);
stroke(249, 22, 22);
for (int i = 70; i < 2400; i += 70) {
line(i, 10, i + i/2, 800);
line(i + i/2, 800, i*1.2, 1090);
}
exit();
}
