n=int(input("Enter the integer: "))
n1, n2=0,1
next= 0
#check if the nuo. of term is valid
if n<=0:
    print("not valid")
elif n==1:
    print("fibo series: ", n)
    print (n1)
###now generate fibo 
else:
    print("fibo series:  ")
    while next<=n:
        print(n1)
        nth= n1+n2
         
        n1=n2
        n2=nth
        next+=1

