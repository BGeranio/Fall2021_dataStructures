"""
Brendan Geranio
lab 3 for CIS22

This lab focuses on implemented three classes that utilize a fourth node class to create
ADTs in the form of a linked list, stack, and queue.
"""
from SinglyLinkedList import node

class Stack:
    def __init__(self, start=None, end=None) -> None:
        self.start = start
        self.end = end
        self.count = 0
    
    def setCount(self):
        """
        This functions updates the stacks count value
        pre: 
        post: updated count variable
        Return: 
        PSEUDOCODE:
            copy start node
            set an int to 0
            while node exists
                int + 1
                node.next
            self.count = count
        """
        cur = self.start
        count = 0
        while cur:
            count += 1
            cur = cur.next
        self.count = count
    
    def countCurrency(self):
        self.setCount()
        return self.count
    
    def isStackEmpty(self):
        """
        This function checks if the stack has any values
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            return boolean of start 
        """
        return self.start == None

    def createStack(self, start=None, end=None):
        """
        This function adds values to an invoked stack
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            if stack exists:
                start, end = start_inp, end_inp
            else error
        """
        if self.isStackEmpty():
            self.start = start
            self.end = end
        raise ValueError('Destroy list first.')

    def destroyStack(self):
        """
        This functions deletes the Stack
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            start, end = None, None
        """
        self.start = None
        self.end = None

    def push(self, currObject):
        """
        This function adds an item to the f of the stack
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            new node = node(passedObj)

            if start doesnt exist:
                start = new node

            else:
                new node.next = start
                start = newNode
         
        """
        newNode = node(currObject)
        if self.start == None:
            self.start = newNode

        else:
            newNode.next = self.start
            self.start = newNode

    def peek(self):
        return self.start.getData()

    def findCurrency(self, currObject):
        """
        This is my search function
        pre: 
            post: Currency object
            Return: Found or Not Found
            PSEUDOCODE:
                copy = start
                i int for index
                found = boolean
                while copy exists and found is false:
                    if its the data we are looking for:
                        found = True
                if found:
                    return found
                return not found
        """
        cur = self.start
        i = 0
        found = False
        while cur and (found == False):
            if cur.getData().getTotal() == currObject.getTotal():
                found = True

            cur = cur.getNext()
            i+=1

        if found:
            return 'Found'
        else:
            return 'Not Found'

    def pop(self):
        copyNode = self.start
        self.start = self.start.next
        return copyNode.getData()

    def printStack(self):
        """
        This is my major print function for the lab, its in every non main file.
        pre: 
        post: print outs
        Return: 
        PSEUDOCODE:
            copy start
            string0, string1, string2 = ''

            while node exists:
                string1 = formatted (node object's get data function that gets currency objects get total function)
                string2 = node objects get data function that gets the name of the currency object
                string0 = string1 + string2
                copy moves to next node
            
            print string0
        """
        cur = self.start
        string0 = ''
        string1 = ''
        string2 = ''
        while cur:
            string1 = '{:.2f}'.format(cur.getData().getTotal())
            string2 = cur.getData().name
            string0 += string1
            string0 += ' '
            string0 += string2
            string0 += '    '
            cur = cur.getNext()
        print(string0)
        print('\n')