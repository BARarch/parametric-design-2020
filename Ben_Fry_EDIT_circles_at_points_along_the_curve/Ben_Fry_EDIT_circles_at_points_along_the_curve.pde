size(650, 700);
// Draw circles at points along the curve z = x^4
noFill();
smooth(); for (int x = 0; x < 155; x += 5) {
  float n = norm(x, 0.0, 90.0); // range 0.0 t0 1.0
  float y = pow(n, 4); // Calculate curve
  y *= 100; //Scale z to range 0.0 to 100.0
  strokeWeight(n * 2); // Increase thickness
  ellipse(x, y, 160, 120);
}
noFill();
stroke(150);
smooth(); for (int x = 0; x < 535; x += 8) {
  float n = norm(x, 0.0, 490.0); // range 0.0 t0 1.0
  float y = 1-pow(n, 2); // Calculate curve
  y *= 500; //Scale z to range 0.0 to 100.0
  strokeWeight(n * 2); // Increase thickness
  ellipse(x, y, 160, 120);
}
