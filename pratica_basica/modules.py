



def fib(n):
    a,b = 0, 1
    while a < b:
        print(a, end=' ')
        a, b = b, a + b
        print("Se ejecuto fib1")
        
        
def fib2(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
        return result    
    
    
    
fib(50)
fibo2 = fib2(1000)    

