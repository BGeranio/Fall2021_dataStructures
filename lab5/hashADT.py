"""
Brendan Geranio
lab 5 for CIS22

This lab is about implementing a hash Table ADT with a single main file that allows a user to search the 
table.
"""

class hashTable:
    def __init__(self, size=29):
        self.size = size
        self.table = None
        self.collisions = 0
        self.count = 0

    def makeTable(self):
        """
        This function populates an array with -1 to the size specified on creation. 
        pre: value (int/float)
        post: new self.table
        Return: none
        PSEUDOCODE
            newArray = [0] * size + 1
            for i in range(siez + 1):
                newArray[i] = -1
            self.table = newArray
        """
        newArr = [0] * (self.size+1)
        for i in range(self.size+1):
            newArr[i] = -1
        self.table = newArr

    def delTable(self):
        self.table = None
            
    def quadHash(self, key):
        """
        This function creates an index for the specified key with a quadratic search in case of collision.
        pre: value (int/float)
        post: int index
        Return: index
        PSEUDOCODE:
            keyFractional = key % 1
            keyWhole = key // 1
            index = (2*keyWhole + 3*keyFractional) % size
            index = int(index)

            if table[index] == -1:
                return index

            else:
                collisionCount = 1
                i = 1
                while table[(ind + (i*i)%self.size)] does not equal -1:
                    collisionCount + 1
                    i + 1
                    if (ind + (i*i)%self.size) > 29:
                        break
            
                setCollissions(collisioncount)
                return (ind + (i*i)%self.size)
        """
        keyFractional = key % 1
        keyWhole = key // 1
        ind = (2*keyWhole + 3*keyFractional) % self.size
        ind = int(ind)

        if self.table[ind] == -1:
            return ind

        else:
            coll = 1
            i = 1
            while self.table[(ind + (i*i)%self.size)] != -1:
                coll += 1
                i+=1
                if (ind + (i*i)%self.size) > 29:
                    break
            self.setCollisions(coll)
            return (ind+(i*i))%self.size

    def insert(self, key):
        """
        This function inserts a dollar object at the key created from the objects data.
        pre: dollar object
        post: new table
        Return: none
        PSEUDOCODE
            index = quadHash(key.data)
            table[index] = key
        """
        ind = self.quadHash(key.getTotal())
        self.table[ind] = key

    def search(self, key):
        """
        This function searches the table for a value and returns its index or invalid data if not found.
        pre: int/float value
        post: none
        Return: index value(int) or 'Invalid Data.'
        PSEUDOCODE
            keyFractional = key % 1
            keyWhole = key // 1
            index = (2*keyWhole + 3*keyFractional) % size
            index = int(index)

            if self.table[index].data == key:
                return index

            i = 0  
            if self.table[index].data != key:         
                while self.table[(index+(i*i)%self.size)] != -1:   
                    i + 1
            
            if self.table[(index+(i*i)%self.size)] is -1:
                return "Invalid Data"
            elif self.table[(ind+(i*i)%self.size)].data equals key:
                return (ind+(i*i)%self.size)
            return "Invalid Data"
            
        """
        keyFractional = key % 1
        keyWhole = key // 1
        ind = (2*keyWhole + 3 * keyFractional) % self.size
        ind = int(ind)
        if ind > 29:
            return 'Invalid Data'

        if self.table[ind].getTotal() == key:
            return ind

        i = 0  
        if self.table[ind].getTotal() != key:      
            while self.table[(ind+(i*i)%self.size)] != -1:   
                if self.table[(ind+(i*i)%self.size)].getTotal() == key:
                    break
                i+=1
        
        if self.table[(ind+(i*i)%self.size)] == -1:
            return "Invalid Data"
        elif self.table[(ind+(i*i)%self.size)].getTotal() == key:
            return (ind+(i*i)%self.size)
        return "Invalid Data"
    
    def setCollisions(self, value):
        #modifies the number of collisions
        self.collisions += value

    def getCollisions(self):
        # returns the number of collisions
        return self.collisions

    def getCount(self):
        # returns the number of objects in the array
        count = 0
        for i in range(self.size):
            if self.table[i] != -1:
                count += 1
        self.count = count
        return count 

    def getSize(self):
        # returns the arrays capacity
        return self.size

