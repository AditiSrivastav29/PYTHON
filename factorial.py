num = int(input("enter the number: "))

factorial = 1

if num < 0:
    print("factorial do not exists for negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i

print("factorial=",factorial)