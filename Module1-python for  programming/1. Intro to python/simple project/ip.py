import random
print('-'*10,'🌟Hangman🌟','-'*10)
lst = 'b a g'
live = 6
ls = input('Guess the letter > ')
if ls in lst and ls=='b':
    print('correct')
    print('b _ _')
elif ls in lst and ls=='a':
    print('correct')
    print('_a_')
elif ls in lst and ls=='g':
    print('correct')
    print('_ _ g')
elif ls not in lst:
    print('Not there!')
    print(live - 1, 'left')
else:
    pass
print('bag')


