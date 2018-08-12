void setup() 
{
  size(500,500);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  background(200);
  float x, y;
  float r = min(width,height)*0.45;
  float cx = width/2;
  float cy = height/2;
  translate(cx,cy);
  fill(255);
  ellipse(0,0,2*r,2*r);
  float tt = 20; // tamanho do traco das horas
  float tm = 10; // tamanho do traco dos minutos
  for(int i=0; i<60; i++)
  {
    float alpha = i*PI/30-HALF_PI;
    x = cos(alpha);
    y = sin(alpha);
    if(i % 5 != 0)
    { 
      line(x*(r-tm),y*(r-tm),x*r,y*r);
    }
    else
    {
      fill(0);
      if(i == 0)
      {
       text("12",x*(r-tt), y*(r-tt));
      }
      else
      {
         text((i/5)+"",x*(r-tt), y*(r-tt));
      }
      line(x*(r-tt),y*(r-tt),x*r,y*r);
    }
    float div = second() / 60.0;
    float malpha = (i + div) *PI/30-HALF_PI;
    float mx = cos(malpha);
    float my = sin(malpha);
    
    div = 5 * (minute() / 60.0);
    float halpha = (i + div) *PI/30-HALF_PI;
    float hx = cos(halpha);
    float hy = sin(halpha);
    
    if((hour() % 12) * 5 == i) line(hx, hy, hx*(r-60), hy*(r-60));
    if(second() == i) line(x, y, x*r, y*r);
    if(minute() == i) line(mx, my, mx*(r-30), my*(r-30));
  }
}
