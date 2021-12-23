# Brendan Geranio
# CIS22 Fall 2021
# lab 2
# A lab focusing on multi file class inheritance and polymorphism with a simple object manipulator calculator

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

   

    

