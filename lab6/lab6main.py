"""
Brendan Geranio
lab 6 for CIS22

This is an Extra Credit lab. It is a MinHeap derived from my BST class created in lab4. It adds a simple minHeapify function
that maintains the order of the tree on deletion/insertion. Plus it edits insert, delete, and search to accomodate the new function.
"""

from MinHeap import MinHeap
from dollar import dollar

def main():
    # new BST
    tree = MinHeap()

    # array of float numbers
    dollarArr = [57.12,23.44,87.43,68.99,111.22,44.55,77.77,18.36,543.21,20.21,345.67,36.18,48.48,101.00,11.00,21.00,51.00,1.00,251.00,151.00]
    
    # update above array values by making them a Dollar currency object
    for i in range(len(dollarArr)):
        dollarArr[i] = dollar(dollarArr[i])

    # insert that array into the tree
    for i in range(10):
        tree.insert(dollarArr[i])
    
    # print the tree traversals
    for i in tree.printMinHeap():
        print(i)

    # insert that array into the tree
    for i in range(10, len(dollarArr)):
        tree.insert(dollarArr[i])
    
    # print the tree traversals
    for i in tree.printMinHeap():
        print(i)

if __name__ == '__main__':
    main()