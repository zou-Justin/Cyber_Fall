# CTF Guide Walkthrough by Justin Zou
In this walk through you would learn how to solve the CTF room provided by the site TRYHACKME. Lets get started!

## Task 1
This Task involves the Author Note, please click the accept button to continue
## Task 2
Task 2 gives us a str of letters and numbers and asks us to decode this problem. Looking at this string, we see it ends with a double "==" which is typically seen in base 64. As a result, it is likely it should be encoded in base 64 and we should use a base 64 decoder accordingly. This can be found by simply googling a calculator online. Pasting in the text that they give us and decoding it should give us the correct answer.

## Task 3
This task gives you a simple description, Meta Meta Meta and a  task file to download. Downloading it in, you see that you get an image file. This should get you to think about something known as metadata. It is something that every image that you take with your phone contains and is on most images online unless they were stripped away by the website. The easiest way to do this would be to search up a tool like EXIF tool, which reads in image data and gives it back to you in a readable manner. You should download the file accordingly for your OS and then drag your image file onto the executable. This should open up a terminal with information about the image. Go to the Owner part and you should see your answer.
## Task 4
This task also requires the knowledge of what Steganography is. Steganography is the practice of hiding a secret message in common files such as images, text files or video files. Here we are given an image file and we have to find something that is hidden inside of it. Here we would use Steghide which is a Steganography tool that helps us to extract data from images and files. To get this you would first have to download Steghide from online. *format this better* Cd into the same directory as the Extinction.jpg file you got. Then you can do `steghide extract -sf Extinction.jpg` which will automatically extract the data from Extinction.jpg into txt file. More knowledge of what these commands are can be found with `steghide --help`. You can then cat or open up the file and get the flag.

## Task 5
This task is a bit obscure since it only gives you close to no hints about it. Perhaps if you were bored, you may have been highlighting around the Task and you may see something interesting.
## Task 6
This is a very simple task that revolves around the use of the QR code. It is something you can scan with your phone simply by going to your camera app and pointing it at the QR code. This would open up a prompt that gives you an external link to a website. For this task, once you donwload the file, you will see it is a QR code. Scan it and you will get the answer.
## Task 7
This task can be quite tricky to figure it out immediately. When you download the task file, you get the file hello.hello, which is not easy to know what to do with. However, look at the title and you realize you can read this file. Simply go to your terminal and go to the directory where hello.hello is located. Then you can `cat hello.hello` and look within the file. You will see the flag located somewhere inside.
## Task 8
This task is very similar to task 2, which gave a message that was decodable with base 64. Since the title of this task is `Another decoding stuff` and gives us a similar string of numbers then we can assume that we should do something similar to task 2 to solve the problem. Simplying looking at the string given, `3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L` it is not easy to tell what base we should be converting to. We can use the hint system to see that what we should use is base58, which is actually a common base and often used in Cryptocurrencies. Plugging it into a base58 decoder gives us our answer.
## Task 9
This task is a simple decoding problem. Looking at the tool they give us they state `Left, right, left, right... Rot 13 is too mainstream.` Rot 13 is a simple Caesar Cipher that replaces each letter with a letter 13 places down in the alphabet and is what the left, right part of the clue stands for. As a result, we can deduce that we should try using a Caesar Cipher decoder to decode the string. Sure enough, we get our answer from this. 
## Task 10
Task 10 is very intersting and may remind you of Task 5. Essentially the trick around this Task is to go into the HTML of the site and look at the div under Task 10. Look down far enough and you will be able to find the key you need in a paragraph tag. 
## Task 11
## Task 12
## Task 13
## Task 14
## Task 15
## Task 16
## Task 17
## Task 18
This Task's prompt says `Sometimes we need a 'machine' to dig the past` and provides us with a website and date. This is referring to the popular web archive website, the wayback machine. In case you don't know how it works, it is essentially a site where you can paste URLs of websites into it and see how the website looked like in the past. Pasting the URL given to the wayback machine and going to January 2, 2020 gives us what we need to get the flag.
## Task 19
## Task 20
Task 20 is quite hard to grasp at first, but looking at the title of `Small Bases` shows us that we are dealing with decoding something in a much smaller base than the previous questions dealing with similar concepts. This time we get a string of numbers that go from 0-9 but not above that which shows how this is a string in base 10. We now have to convert this to ascii (numbers that represent text) somehow and then convert that to text. The easiest way to do this is by converting it to hexadecimals, which is the easiest base to conver to text for humans. You can also get this by looking at the hint which shows this natural progression path. So the steps are to 
1. Paste the string into a base10 to base16 decoder
2. And paste that new string into a base16 to text converter, which should give you your final result
## Task 21