class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if self.n ==0:
            return 0
        elif self.n ==1:
            return 1
        else:
            a=1
            b=0
            for i in range(2,self.n+1):
                x= a+b
                print ("Fibonacci(",i,")= ",x)
                b=a
                a=x
                i+=1
            return x

f=Fibonacci(13)
k=f.run()
print(k)




#Dans ce cas, on utilise aussi une boucle, à chaque fois on calcule l'élément f(i) et on affecte f(i-1) à a et f(i-2) à b
#jusqu'à arriver à la fin de la boucle