import java.util.Arrays;

void setup(){
  size(1200,600);
  PImage img = loadImage("cat.png");
  PImage img2 = loadImage("modifiedCat.png");
  img.loadPixels();
  img2.loadPixels();
  int[] data = new int[img.pixels.length];
  for (int i =0; i < data.length; i++){
    color c = img.pixels[i];
    color d = img2.pixels[i];
    if (c != d){
      img.pixels[i] = color(0,0,0);
    }
    else{
      img.pixels[i] = color(255);
    }
    //int red = (int)red(c);
    //int green = (int)green(c);
    //int blue = (int)blue(c);
    //int redM = (int)red(d);
    //int greenM = (int)green(d);
    //int blueM = (int)blue(d);
  }
  img.updatePixels();
  image(img,0,0);
}
