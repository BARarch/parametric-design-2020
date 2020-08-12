void setup() {
 size(1600, 1300);
 smooth();
 noLoop();
 fill(129,130,87,102);
 background(134,216,270);
 }
 void draw() {
 for (int i = 0; i < 20; i++) { // Draw 20 X shapes
 drawX(int(random(255)), int(random(30)),
 int(random(width)), int(random(height)), 100);
 }
 }
 void drawX(int gray, int weight, int x, int y, int size) {
 stroke(gray);
 strokeWeight(12);

rect(x, y, x+size, y+size);
 

 }
