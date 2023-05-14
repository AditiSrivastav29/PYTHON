year=int(input("Enter the year:"))

if year%400==0:
    print(year,"its a leap year.", year)
elif year%100==0:
    print(year,"not a leap year")
elif year%4==0:
    print(year,"its leap year.", year)
else:
    print(year,"not leap.", year)
