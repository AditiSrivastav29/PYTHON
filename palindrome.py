n = int(input("ENTER THE NUMBER:"))
original = n
reversed = 0
while(n>0):
    remainder = n % 10
    reversed = reversed * 10 + remainder
    n= n//10

if(original == reversed):
    print("the number is palindrome.")
else:
    print("the number is not a palindrome.")
    