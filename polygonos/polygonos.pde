void setup() 
{
  size(300,300);
  background(155);  
}

void draw()
{
  int x = width/2;
  int y = height/2;
  translate(x, y);
  
  int raio = 100;
  int lados = 3;
  
  if(keyPressed){
    lados = key-48;
    if(lados > 2 && lados <= 9){
      background(155);
      forma(lados, raio);
    }
  }  
}

void forma(int lados, int raio){
print(lados);
  rotate(HALF_PI*3);
  float angulo = TWO_PI/lados;
  
  beginShape();
  for(float i = 0; i <= TWO_PI; i += angulo){
     float x = cos(i)* raio;
     float y = sin(i)* raio;
     vertex(x, y);  
  }
  endShape(CLOSE);
}
