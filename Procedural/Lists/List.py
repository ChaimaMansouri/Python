#liste 
#syntaxe [ ]
#exemple 1
def exemple1():
    liste=[1,2,3,4,5,6,7,8,9,10]
    print(liste)
    liste=["hello","world"]
    print(liste)
    liste=["hi my name is chaima","i am 20 years old"]
    print(liste)

#exemple 2
#chaque element lie par un indice
#les indices commencent par 0 gauche a droite (positif)
#les indices commencent par -1 gauche a droite (negatif)
def exemple2():
    liste=["hello","world"]
    print(liste[0])
    print(liste[1])
    print(liste[-1])
    print(liste[-2])

#exemple 3
#taille de la liste
def exemple3():
    liste=["hello","world"]
    print(len(liste))

#exemple 4
# [start:stop:step] area de la chaine a afficher   (meme chose de string)
def exemple4():
    liste=["hello","world"]
    print(liste[0:2])
    print(liste[0:1])
    print(liste[::])
    print(liste[0:])
    print(liste[:1])
    
#exemple 5
#les operations sur les listes
# + concate
# * repetition
def exemple5():
    liste=["hello","world"]
    l=["hi","world"]
    l2=liste+["hi","my","name","is","chaima"]
    print(liste+liste)
    print(liste*2)
    print(l)
    print(l2)
    
#exemple 6
#supprimer un element d'une liste
def exemple6():
    liste=["hello","world"]
    del(liste[0])
    print(liste)

#exemple 7
#liste dans une autre liste
def exemple7():
    liste=[[1,2,3],[4,5,6],[7,8,9]]
    print(liste)
    print(liste[0])
    print(liste[1])
    print(liste[2])
    print(liste[0][0])  #indice de la liste global en suite de la liste interieur 
    print(liste[0][1])
    print(liste[0][2])
    print(liste[1][0])
    print(liste[1][1])
    print(liste[1][2])
    print(liste[2][0])
    print(liste[2][1])
    print(liste[2][2])

#exemple 8
#liste vide
def exemple8():
    liste=[]
    print(liste)
    liste=[1,2,3,4,5,6,7,8,9,10]
    print(liste)
    

#*****************main*************************
def main():
    exemple1()
    exemple2()
    exemple3()
    exemple4()
    exemple5()
    exemple6()
    exemple7()
    exemple8()


#*****************main*************************
if __name__=="__main__":
 main()
   