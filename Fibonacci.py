# Pour calculer Fibonacci(13), on commence par tester : 13<>0 et 13<>1 alors on crée la liste u pour enregistrer les éléments u[i]
# il faut calculer Fibonacci(2) et Fibonacci(3) ... jusqu'à arriver à Fibonacci(13)
# on affiche alors l'élément n-1 de la liste u qui correspond au résultat demandé

class Fibonacci1:
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




#on utilisa la récursivité dans cette implémentation 
#exemple Fibonacci(4)= Fibonacci(3)+Fibonacci(2)
#                    = (Fibonacci(2)+Fibonacci(1)) + Fibonacci(2)
#                    = ( (Fibonacci(1)+Fibonacci(0)) + Fibonacci(1) ) + Fibonacci(2)
#                    = ( (Fibonacci(1)+Fibonacci(0)) + Fibonacci(1) ) + (Fibonacci(1)+Fibonacci(0))
#                    = ( (1+1) + 1 ) + (1+1)
#                    = 5

class Fibonacci2:
    def __init__(self,n):
        self.n = n

    def run(self):
        if (self.n ==0) :
            return 0
        elif (self.n==1):
        	return 1

        else:
            return ((Fibonacci2(self.n-1).run())+(Fibonacci2(self.n-2).run()))



#Dans ce cas, on utilise aussi une boucle, à chaque fois on calcule l'élément f(i) et on affecte f(i-1) à a et f(i-2) à b
#jusqu'à arriver à la fin de la boucle

class Fibonacci3:
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
                #print ("Fibonacci(",i,")= ",x)
                b=a
                a=x
                i+=1
            return x

#Dans cette méthode on se base sur l'algorothme logarothmique
#Si n est pair alors , f(n) = carré(f(n/2+1))-carré(f(n/2-1)
#Sinon f(n)= carré(f((n-1)/2+1))+carré(f((n-1)/2))

class Fibonacci4:
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
                
            

var = int(input("Entrez le nombre n :"))

f=Fibonacci1(var)
a=f.run()
print("Fibonacci1",a)

f=Fibonacci2(var)
b=f.run()
print("Fibonacci2",b)

f=Fibonacci3(var)
c=f.run()
print("Fibonacci3",c)

f=Fibonacci4(var)
d=f.run()
print("Fibonacci4",d)
