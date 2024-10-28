#affiche les nombre 1 a 10
def affiche1a10():
    for i in range(1,11):
        print(i)
        
#Somme des nombres naturels
def sommanat():
    somme=0
    for i in range(1,11):
        somme+=i
    print(somme)

#Itérer sur les caractères d'une chaîne de caractères
def iteratestring():
    c="chaima"
    for i in c :
        print(i)

#boucle liste
def boucleliste():
    liste=[1,2,3,4,5,6,7,8,9,10]
    for i in liste:
        print(i)
        

#exmple for rang(start , end , step)   
def exmpleforrang():
    for i in range(1,11,2):
        print(i)

#Itérer sur les clés d'un dictionnaire
def iteratekeys():
    d={1:"a",2:"b",3:"c"}
    for i in d:
        print(i)

#Itérer sur les valeurs d'un dictionnaire
def iteratevalues():
    d={1:"a",2:"b",3:"c"}
    for i in d.values():
        print(i)

#Itérer sur les couples d'un dictionnaire
def iterateitems():
    d={1:"a",2:"b",3:"c"}
    for i in d.items():
        print(i)
        
#tuples
def tuples():
    t=(1,2,3,4,5,6,7,8,9,10)
    for i in t:
        print(i)
#enumerate
def enumerate_function():
    
    colors = ("rouge", "vert", "bleu")
    for index, color in enumerate(colors):
      print(f"Index {index}: {color}")



#******************main******************
def main():
    affiche1a10()
    sommanat()
    iteratestring()
    boucleliste()
    exmpleforrang()
    iteratekeys()
    iteratevalues()
    iterateitems()
    tuples()
    enumerate_function()
    

if __name__=="__main__":
    main()