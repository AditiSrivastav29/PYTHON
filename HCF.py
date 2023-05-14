n1 = int(input("ENTER THE NUMBER:"))
n2 = int(input("ENTER THE NUMBER:"))

if n1>n2:
    mn=n1
else:
    mn=n2

for i in range(1,mn+1):
    if(n1%i == 0) and (n2%i ==0):

        hcf = i

print("HCF OF TWO NUMBER IS :", hcf)