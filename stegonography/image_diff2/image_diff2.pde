import java.util.Arrays;

  boolean lastThree(int value){
   return (value & 7) == 0;
  }

 String reassemble(ArrayList<Integer> parts){
    String ans = "";
    for (int i =0; i < parts.size()-4;i+=4){
       ans += (char)((parts.get(i) << 6) + (parts.get(i+1) << 4) + (parts.get(i+2) << 2) + (parts.get(i+3)));
    }
    return ans;
  }
  
  
void setup(){
  size(1200,600);
  PImage img = loadImage("space.png");
  PImage img2 = loadImage("modifiedSpace.png");
  img.loadPixels();
  img2.loadPixels();
  int count = 0;
  ArrayList<Integer> data2 = new ArrayList<Integer>();
  int[] data = new int[img.pixels.length];
  for (int i =0; i < data.length; i++){
    color c = img.pixels[i];
    color d = img2.pixels[i];
    int red = (int)red(c);
    int green = (int)green(c);
    int blue = (int)blue(c);
    int redM = (int)red(d);
    int blueM = (int)blue(d);
    int greenM = (int)green(d);
    //64+32+16+8+4+2+1
    //last 4 for blue
    // if the img has a 000 in the blue it can be modified. New blue has a 1 on it 
    //the message we get is an img and we can save it as a img and opne it up
    if (c != d){
      if((blue & 7) == 0 && (blue != blueM)){
        img.pixels[i] = color(0,255,0);
      }
      else{
        img.pixels[i] = color(255,0,255);
      }
    }
    else{
      img.pixels[i] = color(255);
    }
    if((blue & 7) == 0 && (blue != blueM)){
      int partOfValue = blueM & 15;
      data2.add(partOfValue);
      count++;
    }
  }
  println(reassemble(data2));
  String[] aArray = new String[1];
  aArray[0] = reassemble(data2);
  
  saveStrings("image.jpg", aArray);
  img.updatePixels();
  image(img,0,0);
}
