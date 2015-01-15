#gives fibonacci sequence of a given number
#verilen sayinin fibonacci serisini verir
def createFib(x):
    liste=[]
    for i in range (x):
        liste.append(i)
    a=0
    b=1
    for i in range(len(liste)):
        if i<len(liste):
            c=a+b
            a=b
            b=c
            print c
            
createFib(15)
        
