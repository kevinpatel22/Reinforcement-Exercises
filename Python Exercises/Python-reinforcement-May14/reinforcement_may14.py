# Exercise 1 
def sumodds(n):
    total = 0
    for num in n:
        if num % 2 == 1:
            total += num
    return total

print(sumodds([1,2,3,4,5,6,7,8,9,10]))

# Exercise 2

animals = ['panda', 'lion', 'python']
name = input("Enter your name here!\n")

def message():
    if name in animals:
        print(f"Hello {name}!")
    else: 
        print("Who goes there?")
message()
