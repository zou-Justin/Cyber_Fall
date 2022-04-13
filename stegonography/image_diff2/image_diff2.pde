import java.util.Arrays;

void setup(){
  size(1200,600);
  PImage img = loadImage("space.png");
  PImage img2 = loadImage("modifiedSpace.png");
  img.loadPixels();
  img2.loadPixels();
  int[] data = new int[img.pixels.length];
  for (int i =0; i < data.length; i++){
    color c = img.pixels[i];
    color d = img2.pixels[i];
    int red = (int)red(c);
    int green = (int)green(c);
    int blue = (int)blue(c);
    int redM = (int)red(d);
    int blueM = (int)blue(d);
    if (c != d){
      if (red == redM && blue == blueM){
        img.pixels[i] = color(0,(green&3) * 255/7,0);
      }
      else{
        img.pixels[i] = color(255,0,255);
      }      
    }
    else{
      img.pixels[i] = color(255);
    }
  }
  img.updatePixels();
  image(img,0,0);
}
