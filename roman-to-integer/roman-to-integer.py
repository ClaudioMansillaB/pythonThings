dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}


print('Write the roman number: ')
roman_number = input().upper()
cont = 0
for letter in roman_number:
    if letter in dict.keys():
        cont += 1
if cont != len(roman_number):
    while True:
        print('Wrong roman number, write again: ')
        roman_number = input().upper()
        cont = 0
        for letter in roman_number:
            if letter in dict.keys():
                cont += 1
        if cont == len(roman_number):
            break

integer_number = 0

for index_letter in range(len(roman_number) - 1):
    if dict[roman_number[index_letter]] >= dict[roman_number[index_letter + 1]]:
        integer_number += dict[roman_number[index_letter]]
    else:
        integer_number += dict[roman_number[index_letter + 1] ] - dict[roman_number[index_letter]]

print(integer_number)




