import java.util.Arrays;


  String reassemble(ArrayList<Integer> parts){
    String ans = "";
    for (int i =0; i < parts.size();i++){
       ans += (char)((parts.get(i) & 0));
    }
    return ans;
  }
  
  
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
    int greenM = (int)green(d);
    //64+32+16+8+4+2+1
    //last 4 for blue
    // if the img has a 000 in the blue it can be modified. New blue has a 1 on it 
    //the message we get is an img and we can save it as a img and opne it up
     
    if (c != d){
      
      //if((blue & 7) == 0 && (blue != blueM)){
      //  img.pixels[i] = color(0,255,0);
      //}
      //else{
      //  img.pixels[i] = color(255,0,255);
      //}
      
      println("blue " +  binary((blue)) + " " + binary(blueM)  );
      //println("green " +  binary((green)) + " " + binary(greenM)  );
      if (blue == blueM){
       println("hoi"); 
      }
      else{
       println("sad"); 
      }

      //if (red == redM && blue == blueM){
      //  img.pixels[i] = color(0,(green&3) * 255/2,0);
      //}
      //else{
      //  img.pixels[i] = color(255,0,255);
      //}      
    }
    else{
      img.pixels[i] = color(255);
    }
  }
  img.updatePixels();
  image(img,0,0);
}
