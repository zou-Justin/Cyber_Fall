# CTF Guide Walkthrough by Justin Zou
In this walk through you would learn how to solve the CTF room provided by the site TRYHACKME. Lets get started!

## Task 1
This Task involves the Author Note, please click the accept button to continue
## Task 2
Task 2 gives us a str of letters and numbers and asks us to decode this problem. Looking at this string, we see it ends with a double "==" which is typically seen in base 64. As a result, it is likely it should be encoded in base 64 and we should use a base 64 decoder accordingly. This can be found by simply googling a calculator online. Pasting in the text that they give us and decoding it should give us the correct answer.

## Task 3
This task gives you a simple description, Meta Meta Meta and a bunch of task files to download. Downloading them in, you see that you get an image file. This should get you to think about something known as metadata. It is something that every image that you take with your phone contains and is on most images online unless they were stripped away by the website. Depending on what OS you are using there are different ways of getting the meta data from this image. (something something something) After you get that you should be able to find the flag inside the image.
## Task 4

## Task 5
This task is a bit obscure since it only gives you close to no hints about it. Perhaps if you were bored, you may have been highlighting around the Task and you may see something interesting.
## Task 6
## Task 7
## Task 8
This task is very similar to task 2, which gave a message that was decodable with base 64. Since the title of this task is `Another decoding stuff` and gives us a similar string of numbers then we can assume that we should do something similar to task 2 to solve the problem. Simplying looking at the string given, `3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L` it is not easy to tell what base we should be converting to. We can use the hint system to see that what we should use is base58, which is actually a common base and often used in Cryptocurrencies. Plugging it into a base58 decoder gives us our answer.
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