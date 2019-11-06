def function():
    numb = int(input("Enter a number: "))
    if numb <= 20:  # determining suffix for < 20
        if numb == 1:
            suffix = 'st'
        elif numb == 2:
            suffix = 'nd'
        elif numb == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    print(str(numb) + suffix)

function()