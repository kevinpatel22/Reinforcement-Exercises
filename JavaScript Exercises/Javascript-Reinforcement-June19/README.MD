# JavaScript Reinforcement: June 19

## Prerequisites
* programming fundamentals

## Exercise
Given an array of strings and an integer k, your task is to return the longest string consisting of k consecutive strings from the array concatenated together.
```
longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3); // -> 'marblesmittensbye'
```
If there is a tie, return the first one.
```
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); // --> "abigailtheta"
```
Return "" if the array is empty or if k is negative or larger than the length of the array.