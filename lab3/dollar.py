# Brendan Geranio
# CIS22 Fall 2021
# lab 2
# A lab focusing on multi file class inheritance and polymorphism with a simple object manipulator calculator
"""
Brendan Geranio
lab 3 for CIS22

This lab focuses on implemented three classes that utilize a fourth node class to create
ADTs in the form of a linked list, stack, and queue.
"""
# CHANGES:
# edited line 19 to get the print statements off the same line
from currency import currency

class dollar(currency):
    name = 'Dollar'    
    def print(self):
        """
        This function updates the inherited print method
        post: 
        Return: none
        PSEUDOCODE
            print a formatted string with 2 trailing zeros equivalent to the total of the
            objects two integers
        """
        print('{:.2f}'.format(self.getTotal()), self.name) 

   

    

