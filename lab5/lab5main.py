"""
Brendan Geranio
lab 5 for CIS22

This lab is about implementing a hash Table ADT with a single main file that allows a user to search the 
table.
"""

from dollar import dollar
from hashADT import hashTable

def main():
    # make a hash table
    hash = hashTable()
    # populate it
    hash.makeTable()
    # array of float numbers
    dollarArr = [57.12,23.44,87.43,68.99,111.22,44.55,77.77,18.36,543.21,20.21,345.67,36.18,48.48,101.00,11.00,21.00,51.00,1.00,251.00,151.00]
    
    # update above array values by making them a Dollar currency object
    for i in range(len(dollarArr)):
        dollarArr[i] = dollar(dollarArr[i])

    # insert the values into the hash array
    for i in range(len(dollarArr)):
        hash.insert(dollarArr[i])

    # printouts
    # Number of objects in the table
    str0 = 'Data items loaded: ' + '{:.2f}'.format(hash.getCount())
    # number of objects divided by capacity
    str1 = 'Load factor of the table: ' + '{:.2f}'.format((hash.getCount()/hash.getSize()))
    # number of collisions during insertions
    str2 = 'Number of collisions: ' + '{:.2f}'.format(hash.getCollisions())
    print(str0)
    print(str1)
    print(str2)
    
    # print intro/commands
    print('Above you will find the number of data items loaded, load factor of the hash table, and the number of collisions.')
    print('You may search the table with: search [value]')
    
    # while for input
    while True:        

        # get input (search/find)
        new = input('What would you like to do?\n').split()

        # if not enough inputs
        if len(new) < 1: 
            print('Need an input next time!')
            continue
        
        # if too many inputs
        if len(new) > 2:
            print(KeyError('Too many inputs on this one'))
            continue

        # this checks whether the second input is an int/float
        valCheck = True
        try:
            int(new[1])           
        except ValueError:
            try:
                float(new[1])
            except ValueError:
                valCheck = False

        # if its not an int/float call error
        if valCheck == False:
            print(ValueError('Thats not an appropriate number!'))
            continue

        # allowed commands
        goodComm = ['search', 'Search', 'find']

        commCheck = False 
        # check if its an allowed command
        if (new[0] == i for i in goodComm):
            commCheck = True

        # if the command is not allowed, print error
        if commCheck == False:
            print('Sorry, thats not a valid first command.')
            continue

        # if first word is one of the allowed search keywords
        if new[0] == 'search' or new[0] == 'Search' or new[0] =='find':
            # search the table
            print(hash.search(float(new[1])))


        # check if they want to exit
        exit = input('Exit the program? Enter y/n\n')
        if exit == 'yes'or exit == 'Yes' or exit == 'y':
            break

if __name__ == '__main__':
    main()


