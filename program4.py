#Write Fibonacci Series Upto n through function defining and put them into a list

def fib(n):
    fib_list=[]
    a, b = 0, 1 #First two numbers of Fibonacci Series in a list 
    while a < n:
        fib_list.append(a) #append only a into the list
        a, b = b, a+b    #update a and b
    return fib_list

fib(2000)
