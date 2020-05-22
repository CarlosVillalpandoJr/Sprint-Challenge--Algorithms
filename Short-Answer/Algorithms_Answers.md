#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
O(n) because its constanstly grows depending on input size

b) O(n^2)
having two loops nested causes n squared time

c) O(n)
The time increase when the number of inputs does
## Exercise II
- stories = n
- stories >= f == egg broken
- stories < f == egg intact

+ My plan would be to set F to n/2 and check if the egg breaks from there. I would have a condition where while the egg == broken, decrement F. When the broken condition is not met I would break out of that condition and set F to whatever is was decremented to. Run time complexity would be O(n).
