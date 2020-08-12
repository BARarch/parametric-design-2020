import processing.pdf.*;

void setup() {
 size(1600, 1300);
 background(255);
 smooth();
 noFill();
 beginRecord(PDF, "Trial 1.pdf");
 }
 
 void draw() {
 for (int i = 0; i < 50; i++) { // Draw 50  shapes
 drawX(int(random(255)), int(random(30)),
 int(random(width)), int(random(height)), 100);
 }
 endRecord();
 print("Done");
  noLoop();
 }
 void drawX(int red, int weight, int x, int y, int size) {
 strokeWeight(3);
 rect(x, y, x, y);

 }
