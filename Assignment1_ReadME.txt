Given two arrays for geo locations this program will match the every geo location in array 1 with its closet pair in array 2.  

This is done by first having a double for loop, which will take an element in array 1 and compute its distance with every element in array 2.
Then when that element is exhuasted, it will move on to the second element in array 1 and so on.  All the distances will be saved in an array
called "distances".

From now we have a big array of distances.  Element 0 to element len(arr1) in this array correspond to the distances computed using the first 
element in array 1.  In other words, to select the smallest distance that corresponds to each element in array 1, we need to iterate through 
the array in steps of len(arr1) at a time.  From there we will analyze each subarray and save the index of the smallest distance.  This index 
corresponds directly to the index of the element in array 2 which is shortest distance away from the element in array 1.  These indexs will be 
saved in an array called "closetPoints".

Lastly we will have a for loop print out sentences which will describe will element in array 1 is closet to each element in array 2.
