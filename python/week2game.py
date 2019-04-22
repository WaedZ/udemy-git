print('GUESSING NUMBER GAME')
print('NUMBERS FROM 1 TO 10')

number1=5
number2 = int(input('GUESS THE NUMBER:'))
while number1 != number2:
    number2 = int(input('GUESS THE NUMBER again:')) 
    continue

print('Great! You Did It!')
