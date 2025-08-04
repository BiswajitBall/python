#Write Fibonacci Series Upto n through function defining

def fib(n):
    a, b = 0, 1 #First two numbers of Fibonacci Series 
    while a < n:
        print(a, end=' ') #print only a
        a, b = b, a+b    #update a and b

fib(2000)
