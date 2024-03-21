My name is Ganesh. I am a highschooler and I was interested in making a mandelbrot set. So, I made one and decided to upload it here as my first github repository.

Here's an explaination about how this design works. First, you make two arrays of each point in the complex plane. First one will contain all the complex values in it and second one will have all the values set to 0. Then, you go through each values in the first array and replace them with next value according to formula. At the end, check weather the given complex number stays bounded in given range or not. If it doesn't, add the number of current iteration in the second array. Now, you can easily skip the complex numbers that diverge by looking at their number in second array.

I wanted to see how it changes over time so I made it such that, it gives you a png file of every iteration in the same folder.

If you want, you can make some changes on line 41, by manually writting distance function and comparing it with 4 instead of 2. That way, you can make it a little faster if you are doing some heavy stuff.
