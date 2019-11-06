percent = float(input('Enter your percentage to get your Grade:'))
def grade_cal(percentage):
    if percentage >= 97:
        return ('A+')
    elif percentage >= 93:
        return ('A')
    elif percentage >= 90:
        return ('A-') 
    elif percentage >= 87:
        return ('B+') 
    elif percentage >= 83:
        return ('B') 
    elif percentage >= 80:
        return ('B-') 
    elif percentage >= 77:
        return ('C+') 
    elif percentage >= 73:
        return ('C')
    elif percentage >= 70:
        return ('C-') 
    elif percentage >= 67:
        return ('D+') 
    elif percentage >= 63:
        return ('D')
    elif percentage >= 60:
        return ('D-') 
    elif percentage <= 60:
        return ('You failed :)')
    else:
        return ('Try Again!')

def result():
    return (f"Your grade is: {grade_cal(percent)}")

print(result())

