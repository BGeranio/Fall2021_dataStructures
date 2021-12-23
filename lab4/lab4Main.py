"""
Brendan Geranio
lab 4 for CIS22

This lab is about implementing a BST node and BST class through a main file. BST stands
for Binary Search Tree. A type of tree where all nodes have a left and right child
with the left being less than their value and the right being greater than their value.
It handles a complicated traversal print out with the Queue() class from lab 3.
"""
from dollar import dollar
from BST import BST

def main():
    """
    This is my main class. It completes everything asked for in the lab in terms of
    presentation, print outs for errors, and ui. Lots of error checks with some short BST
    operations functionality towards the end.
    """
    # new BST
    tree = BST()

    # open output file
    outputFile = open('output.txt', 'w')

    # array of float numbers
    dollarArr = [57.12,23.44,87.43,68.99,111.22,44.55,77.77,18.36,543.21,20.21,345.67,36.18,48.48,101.00,11.00,21.00,51.00,1.00,251.00,151.00]
    
    # update above array values by making them a Dollar currency object
    for i in range(len(dollarArr)):
        dollarArr[i] = dollar(dollarArr[i])

    # insert that array into the tree
    for i in range(len(dollarArr)):
        tree.insert(dollarArr[i])
    
    # print the tree
    for i in tree.printBST():
        print(i)

    # write tree to output
    outputFile.writelines(tree.printBST())
    
    # print intro/commands
    print('Above you will find a variety of traversals of the BST at the start. They are also in output.txt.')
    print('You may edit the tree with commands insert, delete, and search followed by a space and a value')
    
    # while for input
    while True:        

        # get input (search, add, del)
        new = input('What would you like to do?\n').split()

        # if not enough inputs
        if len(new) < 1: 
            outputFile.write('Need an input next time!')
            print('Need an input next time!')
            continue
        
        # if too many inputs
        if len(new) > 2:
            outputFile.writelines('\nToo many inputs on this one')
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
        
        # if its not a int/float call error
        if valCheck == False:
            outputFile.writelines('\nThats not an appropriate number!')
            print(ValueError('Thats not an appropriate number!'))
            continue

        # allows commands
        goodComm = ['search', 'Search', 'find', 
                    'ins', 'insert', 'Insert', 'add', 
                    'delete', 'Delete', 'del']
        commCheck = False 

        # check if its an allowed command
        if (new[0] == i for i in goodComm):
            commCheck = True

        # if the command is not allowed print error
        if commCheck == False:
            outputFile.write('Sorry, thats not a valid first command.')
            print('Sorry, thats not a valid first command.')
            continue
        
        # if first word is one of the allowed search keywords
        if new[0] == 'search' or new[0] == 'Search' or new[0] =='find':
            outputFile.writelines(tree.search(float(new[1])))
            # search the BST
            print(tree.search(float(new[1])))

        # if first word is one of the allowed insert keywords
        if new[0] == 'ins' or new[0] == 'insert' or new[0] == 'Insert'or new[0] == 'add':
            outputFile.write('Inserted: ' + new[1])
            print('Inserted: ' + new[1])  
            # insert the value into the tree
            tree.insert(dollar(float(new[1])))

        # if first word is one of the allowed delete keywords
        if new[0] == 'delete' or new[0] == 'Delete' or new[0] =='del':      
            outputFile.write('Deleted: ' + new[1])
            print('Deleted: ' + new[1])     
            # delete the value from the tree
            tree.delete(float(new[1]))

        # check if the want to print the traversals of the BST
        prnt = input('Would you like to print the BST? Enter y/n\n')
        if prnt == 'y'or prnt == 'yes' or prnt == 'Yes':
            for i in tree.printBST():
                print(i)
            outputFile.writelines(tree.printBST())

        # check if they want to exit. Also will print traversals.
        exit = input('Exit the program and print the BST? Enter y/n\n')
        if exit == 'yes'or exit == 'Yes' or exit == 'y':
            for i in tree.printBST():
                print(i)
            outputFile.writelines(tree.printBST())
            break

    # close outputfile
    outputFile.close()


if __name__ == '__main__':
    main()