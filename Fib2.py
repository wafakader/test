class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if (self.n ==1) or (self.n==0):
        	return 1

        else:
            return ((Fibonacci(self.n-1).run())+(Fibonacci(self.n-2).run()))


f=Fibonacci(13)
k=f.run()
print(k)
