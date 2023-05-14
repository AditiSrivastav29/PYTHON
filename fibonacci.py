def fibo(rang):
    first = 0
    sec = 1
    next = 0
    for i in range(0,rang+1):
        if i ==0 and i==1:
            print(i)
        else:
            next = first + sec
            print(first)
            first,sec = sec,next


fibo(10)