str= input("ENTER THE STRING: ")
vowels = 0
constants = 0

for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or  i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
        vowels = vowels+1
    else:
        constants = constants+1

print("THE NUMBER OF VOWELS: ",vowels)
print("THE NUMBER OF CONSTANTS: ",constants)
