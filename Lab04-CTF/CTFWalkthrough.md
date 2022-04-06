# CTF Guide Walkthrough by Justin Zou
In this walk through you would learn how to solve the CTF room provided by the site TRYHACKME. Lets get started!

## Task 1
This Task involves the Author Note, please click the accept button to continue
## Task 2
Task 2 gives us a str of letters and numbers and asks us to decode this problem. Looking at this string, we see it ends with a double "==" which is typically seen in base 64. As a result, it is likely it should be encoded in base 64 and we should use a base 64 decoder accordingly. This can be found by simply googling a calculator online. Pasting in the text that they give us and decoding it should give us the correct answer.

## Task 3
This task gives you a simple description, Meta Meta Meta and a  task file to download. Downloading it in, you see that you get an image file. This should get you to think about something known as metadata. It is something that every image that you take with your phone contains and is on most images online unless they were stripped away by the website. The easiest way to do this would be to search up a tool like EXIF tool, which reads in image data and gives it back to you in a readable manner. You should download the file accordingly for your OS and then drag your image file onto the executable. This should open up a terminal with information about the image. Go to the Owner part and you should see your answer.
## Task 4
This task also requires the knowledge of what Steganography is. Steganography is the practice of hiding a secret message in common files such as images, text files or video files. Here we are given an image file and we have to find something that is hidden inside of it. Here we would use Steghide which is a Steganography tool that helps us to extract data from images and files. To get this you would first have to download Steghide from online which can be found [Windows](http://steghide.sourceforge.net/download.php) or [Linux](https://wiki.bi0s.in/steganography/steghide/)
1. Cd into the same directory as the Extinction.jpg file you got. 
2. Then you can do `steghide extract -sf Extinction.jpg` which will automatically extract the data from Extinction.jpg into txt file. More knowledge of what these commands are can be found with `steghide --help`. 
3. You can then cat or open up the file and get the flag.

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
Task 10 is very intersting and may remind you of Task 5. Essentially the trick around this Task is to go into the HTML of the site and look at the div under Task 10. To do this press `ctrl + shift + I` which will open up the web console. Go to the inspector tab and open up the tag for this question which should be Task 10. Look down far enough and you will be able to find the key you need in a paragraph tag. 

## Task 11
This task is much more complicated than a lot of the tasks taht we have been doing so far but I believe in you! Essentially this revolves around the usage of being able to edit PNG files and fix them so you can display them. 
1. First, you must realize that Images files are made up of a bunch of hexadecimals that can be found with the `xxd` command

2. Second, every image file starts with the same header in the same order as shown in the table below, and without these values would fail to work properly. If you xxd the image file they give us, you would realize that the header is messed up and we need to fix it.

| Values (hex) | Purpose |
| ----------- | ----------- |
| 89      | Has the high bit set to detect transmission systems that do not support 8-bit data and to reduce the chance that a text file is mistakenly interpreted as a PNG, or vice versa.       |
| 50 4E 47   | In ASCII, the letters PNG, allowing a person to identify the format easily if it is viewed in a text editor        |
| 0D 0A    | A DOS-style line ending (CRLF) to detect DOS-Unix line ending conversion of the data.       |
| 1A  | A byte that stops display of the file under DOS when the command type has been used—the end-of-file character.        |
| 0A  | A Unix-style line ending (LF) to detect Unix-DOS line ending conversion.        |

3. Now for the editing portion. To do this in the easiest way possible we should save our image file to a text file so we can edit the hexadecimal easily and then convert that text file to an image file. To do this would be `xxd -p FILE.original > temp.txt` in order to convert the original file to a temp file. Then you can `nano temp.txt` or, however else you want to do it, and edit the header as shown in the table. Putting it in properly, we save temp.txt. Then we input it to a new file with `xxd -p -r temp > FILE.png` and then open up FILE.png. Here you will find your flag!
## Task 12
This task is as the prompt says, inside one of Tryhackme's social accounts. More specifically, this is in their reddit account. By googling `TryHackMe rooms Reddit` and clicking the first link that pops up you should be able to get your answer.
## Task 13
Task 13 gives a string that seems to be made up of just weird characters of pluses and minuses. People who have been on the deepest parts of the internet may recognize this to be the language `brainfuck` which uses only 8 commands, a data pointer and an instruction pointer. Googling up a brainfuck decoder and pasting this text in should give you the answer you need.
## Task 14
Task 14 gives us two strings, S1 and S2 and tells us to find the flag from the two of these values. Notice how S1 is a string of hexadecimal numbers based on the letters and number combination while S2 is binary. The most common way when it comes to these two values is XOR, which is the `exclusive or` argument. It is hard to imagine with hexadecimal so imagine both strings were binary. If the first number of each string is the same, then the output of the XOR function should be a 0, if they are different then it should be a 1. This is useful because its a function that is reversible. Plugging these two values into a XOR decoder should do the trick and give us our answer.
## Task 15
## Task 16
Task 16 uses another steganography tool, stegsolve. This a tool that allows you to input image files into it and you can look at this image file under mutiple lenses. For example you could increase the alpha, decrease the alpha, increase the amount of red, etc. This allows us to find hidden messages inside the images that may not be found normally. You can google how to download stegsolve, which can typically be found...
## Task 17
So this task gives us yet another QR code for us to scan as seen in task 6. Simply scan it, which will take you to a Sound cloud with a 4 second clip. Listen to it and jot down the letters you hear as `THM{Letters You hear from the clip}`
## Task 18
This Task's prompt says `Sometimes we need a 'machine' to dig the past` and provides us with a website and date. This is referring to the popular web archive website, the wayback machine. In case you don't know how it works, it is essentially a site where you can paste URLs of websites into it and see how the website looked like in the past. Pasting the URL given to the wayback machine and going to January 2, 2020 gives us what we need to get the flag.
## Task 19
Task 19 gives us a string that reads this: `MYKAHODTQ{RVG_YVGGK_FAL_WXF}` and tells us to crack this for the key. This is actually a Vigenere Cipher, which can be seen by clicking the hint icon or noticing how it is in the same format as the flag. A vigenre cipher is very similar to a caesar cipher but uses a polyalphabetic format to encode. This means they use mutiple substitution cipher. Putting this string into a Vigenere decoder and looking through all the possible outcomes we see only one that matches the flag key provided, that is our answer.
## Task 20
Task 20 is quite hard to grasp at first, but looking at the title of `Small Bases` shows us that we are dealing with decoding something in a much smaller base than the previous questions dealing with similar concepts. This time we get a string of numbers that go from 0-9 but not above that which shows how this is a string in base 10. We now have to convert this to ascii (numbers that represent text) somehow and then convert that to text. The easiest way to do this is by converting it to hexadecimals, which is the easiest base to conver to text for humans. You can also get this by looking at the hint which shows this natural progression path. So the steps are to 
1. Paste the string into a base10 to base16 decoder
2. And paste that new string into a base16 to text converter, which should give you your final result
## Task 21