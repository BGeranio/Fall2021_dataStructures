# Brendan Geranio
# CIS22 Fall 2021
# lab 2
# A lab focusing on multi file class inheritance and polymorphism 
# with a simple object manipulator calculator

"""
Brendan Geranio
lab 3 for CIS22

This lab focuses on implemented three classes that utilize a fourth node class to create
ADTs in the form of a linked list, stack, and queue.
"""
# CHANGES
# lines 50 - 56: According to the comments on lab 2 the add/sub functions 
# needed to properly add to both whole and fractional

from abc import ABC

class currency(ABC):
    def __init__(self, whole=int(0), fractional=float(.00)):
        self.whole = whole
        self.fractional = fractional

    def getTotal(self):
        """
        This function gets the total from the intitialized values
        post: None
        Return: integer
        PSEUDOCODE
            return (whole + fractional value)
        """
        return self.whole + self.fractional
    
    def checkType(self, num):
        """
        This function checks if you are being passed an object or a value
        pre: passed value may be an object, integer, or float
        post: if its an object it becomes an integer 
        Return: passed value
        PSEUDOCODE
            if the type of number is not float or int (ie its an object)
                call the gettotal fucntion of that object
            return number
        """
        if type(num) != float and type(num) != int:
            return num.getTotal()
        return num

    def add(self, num):
        """
        This function adds the passed value to the whole value initialized
        pre: integer or float
        post: whole increases
        Return: 
        PSEUDOCODE
            Call check of passed value type
            whole += value
        """
        number = self.checkType(num)

        # properly separates the number into a Fractional and Whole piece
        numberFractional = number % 1
        numberWhole = number // 1

        # adds them separately
        self.whole += numberWhole
        self.fractional =+ numberFractional
    
    def sub(self, num):
        """
        This function subtracts the passed value from the whole value initialized
        pre: integer or float
        post: whole decreses
        Return: 
        PSEUDOCODE
            Call check of passed value type
            whole -= value
        """
        number = self.checkType(num)        
        if self.getTotal() - number < 0:
            print('Invalid subtraction')
            return
        numberFractional = number % 1
        numberWhole = number // 1

        self.whole += numberWhole
        self.fractional =+ numberFractional
    
    
    def isEqual(self, num):
        """
        This function checks if the passed value is equal to the combined values of whole
        and fractional. 
        pre: integer or float
        post: 
        Return: boolean
        PSEUDOCODE
            Call check of passed value type
            return boolean check if total = number
        """
        number = self.checkType(num)
        return self.getTotal() == number           
    
    def isGreater(self, num):
        """
        This function checks whether the passes value is greater than the total.
        pre: integer or float
        post: 
        Return: boolean
        PSEUDOCODE
            Call check of passed value type
            return boolean of value > total
        """
        number = self.checkType(num)  
        return number > self.getTotal()
    
    def print(self):
        #basic print function
        print(self.getTotal() + 'Currency')

