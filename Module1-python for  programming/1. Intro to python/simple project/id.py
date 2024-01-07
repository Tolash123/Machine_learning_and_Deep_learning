sentence = input('Input any sentence > ')
for letter in sentence:
    if letter.lower()== 'r':
        print('\033[33m', end='')
    elif letter.lower()=='b' or 'g' or 'p' or 'y':
        print('\033[32m', end='')
    else:
        print('\033[0m', end='')
    print(letter, end='')
print()
    
    


