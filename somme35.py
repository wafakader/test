class Somme35:
    def __init__(self, n):
        self.n= n

    def run(self):
        i= 1
        somme= 0
        while i<=self.n:
            if i%5 == 0 or i%3==0 :
                somme+= i
	    i+= 1

        return somme

    def getclasses(self):
        l =list()
        l.append(self)
        return l