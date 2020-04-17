#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(nlog(n))


c) O(n)

## Exercise II
- stories = n
- stories >= f == egg broken
- stories < f == egg intact

+ My plan would be to set F to n/2 and check if the egg breaks from there. I would have a condition where while the egg == broken, decrement F. When the broken condition is not met I would break out of that condition and set F to whatever is was decremented to. Run time complexity would be O(n).
