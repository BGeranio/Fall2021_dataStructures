# Brendan Geranio
# Lab 1 for CIS 22C Fall 2021

def IsArrayPrimeIter(arr, numInts):
    """
    This algorithm checks if all numbers are prime within an array with a loop.
    pre: arr - an array of integers
    post: 
    Return: Boolean
    PSEUDOCODE
    function is array prime (array)
        print entering function
        new boolean = True
        for item in array:
            if item is == 2 keep boolean same
            if item cant be divided by 2 or 3 make boolean false
            create integer to test for primes

            **the while loop below is adapted from the idea that all primes greater than
            ** 3 are of the form 6k+/-1

            loop while integer(originally equal to 5) is less than or equal to item
                if item cant be divided by integer or integer + 2 make boolean false
                add 6 to integer
        print leaving function
        return boolean
    """
    print("Entering Is Array Prime Iterative")
    truth = True
    for x in range(numInts):
        if 1 < arr[x] <= 3:
            break
        if arr[x] % 2 == 0 or arr[x] % 3 == 0:
            truth = False
        i = 5
        while i ** 2 <= arr[x]:
            if arr[x] % i == 0 or arr[x] % (i + 2) == 0:
                truth = False
            i += 6
    
    print("Leaving Is Array Prime Iterative")
    return truth 

def IsPrimeRecur(num, i = 2):  
    """
    This algorithm checks if all numbers in an array are prime recursively(no loops)
    pre: array of integers
        number identifying the index in the array
        number representing the integer i
    post: 
    return: boolean
    PSEUDOCODE
    function is array prime recursive ( array, index, i)
        if item is == 2 
            call same function with index + 1
        if item cant be divided by 2 or 3 
            return False

        **the if statement below is adapted from the idea that all primes greater than
        ** 3 are of the form 6k+/-1

        if i (originally equal to 5) is less than or equal to array at index
            if the item at the current index of the array cant be divided by i or i + 2 
                return False
            call same function with i + 6
        
        if the index is less less than the len(array) call function with index + 1
        otherwise return True
    """
    print("Entering Is Prime Recursive")
    if 1 < num <= 3:
        print("Leaving Is Prime Recursive")
        return True
    if num % 2 == 0 or num % 3 == 0:
        print("Leaving Is Prime Recursive")
        return False
    if i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            print("Leaving Is Prime Recursive")
            return False
        print("Leaving Is Prime Recursive")
        return IsPrimeRecur(num, i + 6)
    print("Leaving Is Prime Recursive")
    return True           

def IsArrayPrimeRecur(arr, numInts, num = 0):
    """
    This function calls the recursive prime function
    Pre: array of integers
        number representing index of array
    Post:
    returns: Boolean
    PSEUDOCODE:
        prints entering the recursive function 
        if is number prime ( passing array at index num):]
            print prime array using recursion
        else:
            print not a prime array using recursion
        if num is less than numInts - 1:
            call IsArrayPrimeRecur( array, numInts, num + 1)        
            
    """
    print("Entering Is Array Prime Recursion")

    if IsPrimeRecur(arr[num]):
        print("Prime Array using recursion")
    else:
        print("Not a Prime Array using recursion")

    if num < numInts - 1:
        print ("Leaving Is Array Prime Recursion")
        return IsArrayPrimeRecur(arr, numInts, num + 1)
    return 
def main():
    """
    The main function that gets input from the user and operates on the data with
    previously made functions
    Pre:
    Post: An array of integers 
        a number representing the size of the array
    Returns: 
    PSEUDOCODE:
        input from user for size of array
        input for integers of array
        edit the array input to remove white spaces and add to an existing array
            error check for numbers less than 0
        call recursive and iterative functions with new array
            error check for size of array being > 16
        if they are true print a positive message otherwise negative
    """
    numInts = int(input('Enter the number of integers (0<=16):'))
    arr = input('Enter the numbers in your array separate by spaces:')
    tokens = arr.split()

    newArr = []
    for x in tokens:
        if int(x) < 0:
            print("Numbers need to be >= 0.")
            main()
        newArr.append(int(x))

    if numInts == len(newArr) or numInts <= 16:
        if IsArrayPrimeIter(newArr, numInts):
            print("Prime Array using iteration")
        else:
            print("Not a Prime Array using iteration")
        IsArrayPrimeRecur(newArr, numInts)
    else:
        print("Number of integers must be <= 16.")
        main()

main()