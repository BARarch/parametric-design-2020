import processing.pdf.*;

void setup() {
  beginRecord(PDF, "Export Final.pdf");
 size(1600, 1300);
 smooth();
 noLoop();
 fill(242,204,47,102);
 rectMode(CORNER);

 background(56,90,94);
  
 }

 
 void draw() {
 for (int i = 0; i < 20; i++) { // Draw `10 X shapes
 drawX(int(random(255)), int(random(30)),
 int(random(width)), int(random(height)), 100);
 }
 endRecord();
 print("Done");
 noLoop();
 }
 void drawX(int gray, int weight, int x, int y, int size) {
 stroke(gray);
 strokeWeight(weight);
 stroke(174,221,60);

rect(x, y, x+size, y+size);

 }
