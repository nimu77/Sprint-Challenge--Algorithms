#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It is O(n).


b) It is O(nlogn)


c) It is O(n).

## Exercise II

# Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

- n represents story of the building.
- here since we would like to minimized the number of dropped + broken eggs
    - start from the floor 1, if it breaks u know it breaks there and it will break if you go higher
    - this way the value of f will be minimized.
    - if the egg does not break in floor one, you incremently go up to see if the eggs breaks to find the value of f.
    - runtime complexity will be O(n).