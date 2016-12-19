class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if self.n ==0:
            return 0
        elif self.n ==1:
            return 1
        else:
            u=list()
            u.insert(0,0)
            u.insert(1,1)
            for i in range(2,self.n):
                u.insert(i,u[i-1]+u[i-2])
            return u[self.n-1]

f=Fibonacci(13)
k=f.run()
print(k)
