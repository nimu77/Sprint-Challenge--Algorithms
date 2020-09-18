#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It is O(n). It is O(n) because while loop iterates through input value of n and increases the value of (a). If the value of a is higher than 3*n then the loop ends.


b) It is O(nlogn). For this, the first for loop iterates through the given input making it O(n). The while loop has a condition which increments by multiplication of 2 which decreases the number of times it iterates making it O(logn). Overall, it is O(nlogn).


c) It is O(n). In this recursive function, the function is being called n times until it reaches the base case, which makes this linear, so it is O(n).

## Exercise II

# Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

- n represents story of the building.
- here since we would like to minimized the number of dropped + broken eggs
    - start from the floor 1, if it breaks u know it breaks there and it will break if you go higher
    - this way the value of f will be minimized.
    - if the egg does not break in floor one, you incremently go up to see if the eggs breaks to find the value of f.
    - runtime complexity will be O(n).