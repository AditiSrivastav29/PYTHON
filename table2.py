
def table():
    num = int(input("Enter number for table : "))

    for i in range(1,11,5):                #here, 5 increments the table 
        print(i,"*",num,"=",i*num)


table()