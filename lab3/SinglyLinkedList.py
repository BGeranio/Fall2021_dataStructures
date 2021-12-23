from dollar import dollar

# the all important node class used throughout the assignment
# according to specs it has a data attribute and a pointer to the next node value
# both of these values have getters/setters
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
    
class SinglyLinkedList:
    def __init__(self, start=None, end=None) -> None:
        self.count = 0
        self.start = start
        self.end = end

    def setCount(self):
        """
        This functions updates the linked lists count value
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

    def isListEmpty(self):
        return self.start == None

    def createList(self, start=None):
        """
        This function adds a value to an invoked linked lists head node
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            if list exists:
                start = start_inp
            else error
        """
        if self.isListEmpty():
            self.start = start
        raise ValueError('Destroy list first.')

    def destroyList(self):
        """
        This functions deletes the list
        pre: 
        post: 
        Return: 
        PSEUDOCODE:
            start, end = None, None
        """
        self.start = None
        self.end = None
   
    def addCurrency(self, currObject, index):
        """
        This function adds an item to the list at the index location passed
        pre: currency Object, int_inp
        post: new list node
        Return: None
        PSEUDOCODE:
            int i = 1
            new node = node(passedObj)

            if index_inp is 0:
                new node.next = start
                start = new Node
                return

            if start exists:
                node copy = start

                while i < index and copy exists:
                    if copy.next exists:
                        copy = copy.next
                    i= i + 1

                if copy = start:
                    end = new node
                
                if copy.next:
                    new node.next = copy.next
                
                else:
                    copy.next = new node
            else start doesnt exist:
                start = new node
                end = new node         
        """
        i = 1
        newNode = node(currObject)

        if index == 0:
            newNode.setNext(self.start)
            self.start = newNode
            return

        if self.start:
            nodeAtIndex = self.start

            while i < index and nodeAtIndex:
                
                if nodeAtIndex.getNext():
                    nodeAtIndex = nodeAtIndex.getNext()
                i += 1
                
            if nodeAtIndex == self.end:
                self.end = newNode
            if nodeAtIndex.getNext():
                newNode.setNext(nodeAtIndex.getNext())

            nodeAtIndex.setNext(newNode)
        else:
            self.start = newNode
            self.end = newNode      
    
    def removeCurrency(self, currObject: object):
        """
        This function removes the object data equal to the one passed from the 
        linked list.
        pre: linked list, currency object input
        post: new list
        Return: None
        PSEUDOCODE:
            current = start
            previous = none
            found = boolean
            while current exists and found is False:
                if current.data = object.data:
                    found is True
                else:
                    previous = current
                    current = current.next
            if current is None:
                raise error
            if previous doesnt exist:
                start = current.next
            else previous exists:
                previous.next = current.next
        """
        cur = self.start
        previous = None
        found = False
        while cur and (found is False):
            if cur.getData().getTotal() == currObject.getTotal():
                found = True
            else:
                previous = cur   
                cur = cur.getNext()
        if cur is None:
            raise ValueError('value not found')
        if previous is None:
            self.start = cur.getNext()
        else:
            previous.setNext(cur.getNext())

    def removeCurrencyIndex(self, index: int):
        """        
        This function removes the object data at the index passed for the linked list.
        pre: linked list, int index
        post: new list
        Return: None
        PSEUDOCODE:
            current = start
            int i = 0
            previous = none
            while i less than index:
                previous = current
                current = current.next
                i += 1
            if current is None:
                raise error
            if previous doesnt exist:
                start = current.next
            else previous exists:
                previous.next = current.next        
        """
        cur = self.start
        i = 0
        previous = None
        while i<index:
            previous = cur   
            cur = cur.getNext()
            i+=1
        if cur is None:
            raise ValueError('value not found')
        if previous is None:
            self.start = cur.getNext()
        else:
            previous.setNext(cur.getNext())

    
    def findCurrency(self, currObject):
        """
        This is my search function that looks for a currency objects data 
        within the linked list

        pre: 
        post: Currency object
        Return: Found or Not Found
        PSEUDOCODE:
            copy = start
            i int for index
            found = boolean
            while copy exists and found is false:
                if copy.data == passed object.data:
                    found = True
                    break
                copy = copy.next
                i += 1
            if copy is None:
                return not Found
            return i
        """
        cur = self.start
        i = 0
        found = False
        while cur and (found == False):
            if cur.getData().getTotal() == currObject.getTotal():
                found = True
                break  
            cur = cur.getNext()
            i+=1

        if cur is None:
            return 'Not Found'
        else:
            return i
            
    def getCurrency(self, index):
        """
        This is my search function that looks for a value based on index 
        in the linked list

        pre: index value
        post: 
        Return: not found or node.data
        PSEUDOCODE:
            copy = start
            i = 0
            while i < index:
                copy = copy.next
                i+=1
            if copy doesnt exist:
                return not found
            return copy.data's print function
        """
        cur = self.start
        i = 0
        while i < index:
            cur = cur.getNext()
            i+=1

        if cur is None:
            return 'Not Found'
        else:
            return cur.getData().print()

    def printList(self):
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
    
    def printStart(self):
        self.start.getData().print()
        print('\n')
    
    def printEnd(self):
        self.end.getData().print()
        print('\n')

    def countCurrency(self):
        self.setCount()
        return self.count
        
       
        

        
            