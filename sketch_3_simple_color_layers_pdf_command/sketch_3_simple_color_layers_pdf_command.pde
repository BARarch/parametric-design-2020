import processing.pdf.*;

void setup() {
size(800, 800, PDF, "sketch_3_simple_color_layers.pdf");
}
void draw() {
smooth();
strokeWeight(2);
stroke(22, 75, 240);
for (int s = 20; s < 800; s += 30) {
  line(s, 0, s + s/2, 800); 
}
stroke(0);
strokeWeight(2);
for (int j = 100; j < 4000; j += 100) {
  line(0, 800, j + j/2, 0);
}
stroke(249, 22, 22);
for (int i = 90; i < 4000; i += 90) {
  line(0, 0, i + i/2, 800);
}
exit();
}
