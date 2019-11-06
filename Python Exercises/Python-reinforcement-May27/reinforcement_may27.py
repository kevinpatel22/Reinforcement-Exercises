digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

dictionary = {}

for digit in range(0, len(digits)):
    dictionary[digits[digit]] = {
        'french': fr[digit],
        'english': en[digit]
    }


print(dictionary)


 