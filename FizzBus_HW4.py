for i in range(1,101):
    if i% 3 ==0 and i% 5 !=0:
        print("Fizz")
        i+=1
    elif i% 3 !=0 and i% 5 ==0:
        print("Buss")
        i+=1
    elif i% 3 ==0 and i% 5 ==0:
        print("FizzBuss")
        i+=1