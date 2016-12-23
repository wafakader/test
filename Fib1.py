class Fibonacci:
    def __init__(self,n):
        self.n = n

    def run(self):
        if (self.n ==0) :
            return 0
        elif (self.n == 1):
            return 1
        else:
            u= []
            u.append(0)
            u.append(1)
            for i in range(2,self.n+1):
                x= u[i-1]+u[i-2]
                u.append(x)
                i+=1
            return u[self.n]

f=Fibonacci(13)
k=f.run()
print(k)

# Pour calculer Fibonacci(13), on commence par tester : 13<>0 et 13<>1 alors on crée la liste u pour enregistrer les éléments u[i]
# il faut calculer Fibonacci(2) et Fibonacci(3) ... jusqu'à arriver à Fibonacci(13)
# on affiche alors l'élément n-1 de la liste u qui correspond au résultat demandé
