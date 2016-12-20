class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if (self.n ==0) :
            return 0
        elif (self.n==1):
        	return 1

        else:
            return ((Fibonacci(self.n-1).run())+(Fibonacci(self.n-2).run()))


f=Fibonacci(13)
k=f.run()
print(k)

#on utilisa la récursivité dans cette implémentation 
#exemple Fibonacci(4)= Fibonacci(3)+Fibonacci(2)
#                    = (Fibonacci(2)+Fibonacci(1)) + Fibonacci(2)
#                    = ( (Fibonacci(1)+Fibonacci(0)) + Fibonacci(1) ) + Fibonacci(2)
#                    = ( (Fibonacci(1)+Fibonacci(0)) + Fibonacci(1) ) + (Fibonacci(1)+Fibonacci(0))
#                    = ( (1+1) + 1 ) + (1+1)
#                    = 5
