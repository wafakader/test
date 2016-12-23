class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if self.n ==0:
            return 0
        elif self.n ==1:
            return 1
        else:
            u=[]
            u.append(0)
            u.append(1)
            u.append(1)
            for i in range(3,self.n+1):
                
                if (i%2==0):
                    j = int ((i/2)+1)
                    k = int ((i/2)-1)
                    x = (u[j])**2-(u[k])**2
                    u.append(x)
                    
                else :
                    m = int(((i-1)/2)+1)
                    p = int((i-1)/2)
                    x = (u[m])**2+(u[p])**2
                    u.append(x)
                   
                i+=1
                    
            return (u[self.n])
                
            

f=Fibonacci(13)
k=f.run()
print(k)
