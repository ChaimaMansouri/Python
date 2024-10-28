#add plusiaure element dans une liste
#for
def add_plusiaure_element_dans_une_liste(*args):
    liste=[1,2,3,4,5,6,7,8,9,10]
    for i in args:
        liste.append(i)
    print(liste)
    

#iterable
#for
def add_plusiaure_element_dans_une_liste2(*args):
    liste=[i for i in args] #i = args lire les elements de args et les ajouter dans la liste
    print(liste)
#for avec condition
def add_plusiaure_element_dans_une_liste3(*args):
    liste=[i for i in args if i%2==0] # ajout les nombres pairs
    print(liste)   

#exmple 1 
#les paires carre
def exmple1():
    liste=[i**2 for i in range(1,11) if i%2==0]
    print(liste)
    
#exmple 2
#plusieur for
def exmple2():
    liste=[[i,j] for i in range(1,3) for j in range(1,3)]
    print(liste)
    
#************************main************************
def main():
    print("add plusiaure element dans une liste")
    add_plusiaure_element_dans_une_liste(1,2,3,4,5,6,7,8,9,10)
    print("add plusiaure element dans une liste2")
    add_plusiaure_element_dans_une_liste2(1,2,3,4,5,6,7,8,9,10)
    print("add plusiaure element dans une liste3")
    add_plusiaure_element_dans_une_liste3(1,2,3,4,5,6,7,8,9,10)
    print("exmple 1")
    exmple1()
    print("exmple 2")
    exmple2()

if __name__=="__main__":
    main()