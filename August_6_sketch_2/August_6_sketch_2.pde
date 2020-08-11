void setup() {
size(850, 550);
}
void draw() {
noFill();
translate(mouseX, mouseY);
triangle(100, 0, 150, 150, 0, 100);
}
