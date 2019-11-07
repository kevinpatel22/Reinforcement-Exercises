# JavaScript Reinforcement: June 24

## Prerequisites
* Programming fundamentals

## Exercise
In some countries of the former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to possess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:
```
003111 # 3 = 1 + 1 + 1
813372 # 8 + 1 + 3 = 3 + 7 + 2
17935 # 1 + 7 = 3 + 5
56328116
```
Your task is to write a method `luckCheck(str)`, which returns `true` if argument is string decimal representation of a lucky ticket number, or `false` for all other numbers. It should handle errors for empty strings or strings which don't represent a decimal number