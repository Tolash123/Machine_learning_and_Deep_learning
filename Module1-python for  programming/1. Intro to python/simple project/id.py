import os, time

def pretty():
    print('-'*10, 'List of Names' ,'-'*10)
pretty() 
firstname = []
lastname = []  
Name = []
while True:
    name = input('Enter your firstname: ').capitalize().strip()
    sname = input('Enter your lastname: ').capitalize().strip()
    fullname = name + ' ' +sname
    if fullname in Name:
        Name.remove(fullname)
        print('The name is in the list')
        time.sleep(3)
    else:
        pass
    os.system('clear')
    pretty()
    Name.append(fullname)
    for item in Name:
        print(item)
    