
def reverseInt(n):
    reverse = 0
    while n > 0:
        a = n % 10
        reverse = reverse * 10 + a
        n = n // 10
    return reverse

def isPalindrome(s):
    if s < 0:
        return False
    if s > 99999:
        return False    
    reverseS = reverseInt(s)
    return s==reverseS

def main():    
    array = [int(i) for i in input().split()]
    y = []

    if len(array) > 8:
        array = array[:9]

    for item in array:
        if item == -1:
            break
        if isPalindrome(item):
            y.append(item)

    y.sort(reverse=True)
    print(y)

if __name__ == '__main__':
    main()