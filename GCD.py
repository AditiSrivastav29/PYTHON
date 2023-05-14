n1=int(input("Enter the integer:"))
n2=int(input("Enter the integer: "))

if n1>n2:
    mn=n1
else:
    mn=n2
for i in range(1 , mn+1):
    if n1%i==0  and  n2%i==0:
        
        gcd= i
print("GCD/ HCF of n1 & n2 is: ", gcd)