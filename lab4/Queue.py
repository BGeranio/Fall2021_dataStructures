"""
Brendan Geranio
lab 3 for CIS22

This lab focuses on implemented three classes that utilize a fourth node class to create
ADTs in the form of a linked list, stack, and queue.
"""
"""
Brendan Geranio
lab 4 for CIS22

This lab is about implementing a BST node and BST class through a main file. BST stands
for Binary Search Tree. A type of tree where all nodes have a left and right child
with the left being less than their value and the right being greater than their value.
It handles a complicated traversal print out with the Queue() class from lab 3.
"""
# edited in node class for lab 4 to get rid of extra file
# edited print to return the string instead of printing

class node:
    def __init__(self, value, next = None) -> None:
        self.data = value
        self.next = next

    def setNext(self, value):
        self.next = value

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def getData(self):
        return self.data
    
class Queue:
    def __init__(self, start=None, end=None) -> None:
        self.start = start
        self.end = end
        self.count = 0
    
    def setCount(self):
        """
        This functions updates the queues count value
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

    def isQueueEmpty(self):
        """
        This function checks if the queue has any values
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            return boolean of self.start 
        """
        return self.start == None

    def createQueue(self, start=None, end = None):
        """
        This function adds values to an invoked queue
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            if queue exists:
                start, end = start_inp, end_inp
            else error
        """
        if self.isQueueEmpty():
            self.start = start
            self.end = end
        raise ValueError('Destroy list first.')

    def destroyQueue(self):
        """
        This functions deletes the queue
        pre: self.start, self.end == something
        post: self.start, self.end == None
        Return: 
        PSEUDOCODE:
            start, end = None, None
        """
        self.start = None
        self.end = None

    def enqueue(self, currObject):
        """
        This function adds an item to the end of the queue
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            new node = node(passedObj)
            if queue is <2 in size 
                make new node = start, end
            else
                    set end.next = new node
                    self.end = new node

        """
        newCurr = node(currObject)
        if self.end == None:
            self.start = self.end = newCurr
            return
        self.end.setNext(newCurr)
        self.end = newCurr
    
    def dequeue(self):
        """
        This methode removes the item at the front of the queue
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            if queue is empty:
                return error msg
            copy start
            start = copy.next
            if start doesnt exist:
                empty self.end
                
        """
        
        if self.isQueueEmpty():
            return 'List is empty'
        copy = self.start
        self.start = copy.getNext()

        if(self.start == None):
            self.end = None
        return copy.getData()

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

    def peekRear(self):
        return self.end

    def peekFront(self):
        return self.start
    
    def printQueue(self):
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
            string1 = '{:.2f}'.format(cur.getData().getData().getTotal())
            string2 = cur.getData().getData().name
            string0 += string1
            string0 += ' '
            string0 += string2
            string0 += ' '
            cur = cur.getNext()
        return string0