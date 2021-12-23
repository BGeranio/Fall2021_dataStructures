"""
Brendan Geranio
lab 3 for CIS22

This lab focuses on implemented three classes that utilize a fourth node class to create
ADTs in the form of a linked list, stack, and queue.
"""
from dollar import dollar
from SinglyLinkedList import SinglyLinkedList 
from Stack import Stack
from Queue import Queue

def main():
    q = Queue()
    q.enqueue(dollar(1))
    q.enqueue(dollar(2))
    q.enqueue(dollar(3))
    q.enqueue(dollar(4))
    q.dequeue()
    front = q.peekFront()

    q.enqueue(front.getData())
    q.enqueue(dollar(5))
    q.dequeue()
    q.enqueue(dollar(6))
    q.printQueue()
    """
    This is my main function that calls and uses each of the required ADTs
    pre: 
        post: 
        Return: 
        PSEUDOCODE:
            No algorithms beyond basic object manipulation and for loops.
    """
    """
    #welcome message print outs
    welcomeMsg = 'Hello! This is Brendan Geranios lab 3 main function.'
    llistMsg = 'Beginning of linked list portion.'
    stackMsg = 'Beginning of stack portion.'
    queueMsg = 'Beginning of queue portion.'
    leavingMsg = 'Thats the end of all the sections for this lab.'

    
    print(welcomeMsg)
    
    print(llistMsg)

    # array of float numbers
    dollarArr = [57.12, 23.44, 87.43 , 68.99, 111.22, 44.55 ,77.77 ,18.36 
    ,543.21, 20.21,345.67,36.18,48.48,101.00,11.00,21.00,51.00,1.00,251.00
    ,151.00]

    # update above array values by making the a Dollar currency object
    for i in range(len(dollarArr)):
        dollarArr[i] = dollar(dollarArr[i])
    
    # make linked list

    linkedList = SinglyLinkedList()
    
    # A .Add the first seven (7) objects from the array into the linked 
    # list in order such that they end up in the reverse order in the 
    # linked list, i.e. the seventh element as first node and first element 
    # as seventh node. 
    # If it is easier,  you are allowed to insert copies of the objects.

    #make a shorter array to avoid object
    sevenList = [0] * 7

    for i in range(7):
        sevenList[i] = dollarArr[i]
        
    # reverse shorter list
    sevenList.reverse()

    #feed linked list
    for i in range(7):   
        linkedList.addCurrency(sevenList[i], i)
    
    # B. Search for $87.43 followed by $44.56 - print the results of each.
    print(linkedList.findCurrency(dollar(87.43)))
    print(linkedList.findCurrency(dollar(44.56)))

    # C. Remove the node containing $111.22 followed by the node at index 2.
    linkedList.removeCurrency(dollar(111.22))
    linkedList.removeCurrencyIndex(2)

    # D. Print the contents of the list. 
    linkedList.printList()

    # E. Then add the next four (4) objects (#9 thru 12) such that their 
    # index in the linked list is calculated as (index in array % 5).
    for i in range(8, 12):
        linkedList.addCurrency(dollarArr[i], ((i+1)%5))

    # F. Remove two (2) objects at indexes (countCurrency % 6) and 
    # (countCurrency / 7) in that order.
    linkedList.removeCurrencyIndex((linkedList.countCurrency()%6))
    linkedList.removeCurrencyIndex((linkedList.countCurrency()/7))

    # G. Print the contents of the list.
    linkedList.printList()


    print(stackMsg)

    # make stack 
    stackOne = Stack()

    # A. Push seven (7) objects starting from the array index 13 onwards to the stack.
    for i in range(12, 19):   
        stackOne.push(dollarArr[i])

    # B. Peek the top of the stack - print the result.
    stackOne.peek().print()
    print('\n')

   
    # C. Find the object $3.14 in the stack - print the result.
    print(stackOne.findCurrency(dollar(3.14)))
    

    # D. Perform three (3) pops in succession.
    stackOne.pop()
    stackOne.pop()
    stackOne.pop()

    # E. Print the contents of the stack.
    stackOne.printStack()

    # F. Push five (5) more objects from the start of the objects array to the stack
    for i in range(5):   
        stackOne.push(dollarArr[i])

    # G. Pop twice in succession.
    stackOne.pop()
    stackOne.pop()

    # H. Print the contents of the stack.
    stackOne.printStack()

    print(queueMsg)

    # make queue
    q = Queue()

    # A. Enqueue the seven (7) objects at odd indexes starting from index 5 in the array.
    for i in range(4, 18, 2):   
        q.enqueue(dollarArr[i])
    # B. Peek the front and end of the queue - print the results.
    q.peekFront().getData().print()
    q.peekRear().getData().print()

    # C. Perform two (2) dequeues in succession.
    q.dequeue()
    q.dequeue()

    # D. Print the contents of the queue.
    q.printQueue()

   
    # E. Find the object $3.14 in the queue - print the result.
    print(q.findCurrency(dollar(3.14)))
    

    # F. Enqueue five (5) more objects from the index 10 in the array.
    for i in range(9, 14):   
        q.enqueue(dollarArr[i])

    # G. Dequeue three times in succession.
    q.dequeue()
    q.dequeue()
    q.dequeue()

    # H. Print the contents of the queue.
    q.printQueue()

    # clean up
    linkedList.destroyList()
    stackOne.destroyStack()
    q.destroyQueue()

    print(leavingMsg)
    """

if __name__ == '__main__':
    main()