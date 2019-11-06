dict = {}

def function():
    for n in range(1, 51):
        if n % 2 == 0 and n % 7 == 0:
            dict[n] = n * 2
        elif n % 2 == 0:
            dict[n] = n + 1
        elif n % 7 == 0:
            dict[n] = n - 1
        else:
            dict[n] = n 
    return dict

print(function()) 