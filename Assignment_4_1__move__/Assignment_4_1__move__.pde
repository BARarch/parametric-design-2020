int dragx, dragy, movex, movey;
void setup() {
 size(1600, 1300);
 background(0);
 smooth();
 noLoop();
 noFill();
 noStroke();
 }
 void draw() {
 for (int i = 0; i < 50; i++) { // Draw 50 x shapes
 drawX(int(random(255)), int(random(30)),
 int(random(width)), int(random(height)), 100);
 }
 }
 void drawX(int red, int weight, int x, int y, int size) {
 stroke(red);
 strokeCap(ROUND);
 strokeWeight(12);
 
 line(movex, movey, dragx, dragy);
 line(x, movey, dragx, y);
 }
 void mouseMoved() { 
 movex = mouseX;
 movey = mouseY;
 }
 void mouseDragged() {
 dragx = mouseX;
 dragy = mouseY;
 }
