
void setup() {
 size(1600, 1300);
 background(0);
 smooth();
 noLoop();
 noFill();
 noStroke();
 }
 void draw() {
 for (int i = 0; i < 50; i++) { // Draw 50  shapes
 drawX(int(random(255)), int(random(30)),
 int(random(width)), int(random(height)), 100);
 }
 }
 void drawX(int red, int weight, int x, int y, int size) {
 stroke(red);
 strokeCap(ROUND);
 strokeWeight(12);
 line(x, y, x, y);
 line(x+size, y, x, y+size);
 
 }
