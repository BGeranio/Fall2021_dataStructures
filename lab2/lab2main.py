# Brendan Geranio
# CIS22 Fall 2021
# lab 2
# A lab focusing on multi file class inheritance and polymorphism with a simple object manipulator calculator

from dollar import dollar
from pound import pound


def main():
    """
    This method gets inputs from user and runs input checks before updating/printing created objects
    post: 
    Return: None
    Not an algorithm so no need for pseudocode
    """

    # create 2 objects
    do = dollar()
    po = pound()

    # put objects in array
    primArr = [po, do]

    # while loop to get inputs, can be cancelled after each input
    while True:
        # print the numbers stored in each object 
        primArr[0].print(), primArr[1].print()

        # get the command input 
        new = input('What would you like to do?\n').split()

        # error checks for correct inputs
        if len(new) < 4:
            print('Woah, that input wont work!')
            break

        # this reduces need for copies of later statements by making a new variable
        # == to the required method
        if new[3].lower() == 'dollar':
            method = primArr[1]
        if new[3].lower() == 'pound':
            method = primArr[0]
        if new[3].lower() != 'dollar' and new[3].lower() != 'pound':
            print('Invalid currency.')
            continue
        
        
        check1 = (new[1].lower() == 'd' and new[3].lower() != 'dollar') or (new[1].lower() != 'd' and new[3].lower() == 'dollar')
        check2 = (new[1].lower() == 'p' and new[3].lower() != 'pound') or (new[1].lower() != 'p' and new[3].lower() == 'pound')
        #

        # what is the input doing with the objects, add/subtract/equal/greater 
        # as a/s/e/g

        if new[0].lower() == 'a':

            # check inputs
            if check1 or check2:
                print('Invalid Addition\n')
                continue

            # call method if everything checks out
            method.add(float(new[2]))  

        if new[0].lower() == 's':            
            if check1 or check2:
                print('Invalid subtraction\n')
                continue 
            method.sub(float(new[2]))

        if new[0].lower() == 'e':
            if check1 or check2: 
                print('Invalid is equal to\n')
                continue
            if method.isEqual(float(new[2])):
                print('Those values are equal.')
            else:
                print('Those values are not equal.')     

        if new[0].lower() == 'g':
            if check1 or check2:
                print('Invalid is greater than\n')
                continue
            if method.isGreater(float(new[2])):
                print('That value is greater than the one stored.') 
            else:
                print('That value is less than the one stored.') 

        # end while loop if done with inputs
        nex = input('Another input? Enter y/n\n')
        if nex == 'n' or nex == 'no':
            print('End of Inputs.')
            primArr[0].print(), primArr[1].print()
            break

if __name__ == '__main__':
    main()
