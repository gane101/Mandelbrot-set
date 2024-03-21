My name is Ganesh. I am a highschooler and I was interested in making a mandelbrot set. So, I made one and decided to upload it here as my first github repository.

Here's an explaination about how this design works. First, you make two arrays of each point in the complex plane. First one will contain all the complex values in it and second one will have all the values set to 0. Then, you go through each values in the first array and replace them with next value according to formula. At the end of every iteration, check weather the given sequence stays bounded in given range or not. If it doesn't, add the number of current iteration in the second array. Now, you can easily skip the numbers that diverge by looking at their number in second array.

I wanted to see how it changes so I made it such that, it gives you a png file of every iteration in the same folder.
