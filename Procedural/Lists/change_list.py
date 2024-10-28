#add 


#ajout par index
#si la case non vide crase les elements qui existe
def ajout_par_index():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste[0]=0
    print(liste ,"la taille de la liste",len(liste))
    
#ajout par append ajout a la fin 
#exemple 1
def ajout_par_append():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.append(11)
    print(liste ,"la taille de la liste",len(liste))
    
#ajout par insert ajout a la position souhaitee
#fait décalage des elements
#exemple 2
def ajout_par_insert():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.insert(3,12)
    print(liste ,"la taille de la liste",len(liste))

#ajout par extend
#ajout de plusieurs elements
#exemple 3
def ajout_par_extend():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.extend([11,12,13])
    print(liste ,"la taille de la liste",len(liste))


#supprimer

#supprimer par index
def supprimer_par_index():
    liste=[1,2,3,4,5,6,7,8,9,10]
    del liste[0]
    print(liste ,"la taille de la liste",len(liste))

#supprimer par remove
def supprimer_par_remove():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.remove(5)         #supprimer le 5
    print(liste ,"la taille de la liste",len(liste))

#supprimer par pop
#retourne le dernier element si pop()
#retourne le element en position souhaitee aprés supprimer
def supprimer_par_pop():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.pop(0)
    print(liste ,"la taille de la liste",len(liste))

#supprimer par clear

#cherecher l'index d'un element
def chercher_l_index():
    liste=[1,2,3,4,5,6,7,8,9,10]
    print(liste.index(5))

#copier une liste
def copier_liste():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste2=liste
    liste3=liste.copy()
    print(liste2)
    print(liste3)
    
#reverser une liste
def reverser_liste():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.reverse()
    print(liste)

#couter le nombre d'occurence d'un element
def couter_occurence():
    liste=[1,2,3,4,5,6,7,8,9,10]
    print(liste.count(5))

#trier une liste
def trier_liste():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.sort()
    print(liste)
    
#clear une liste
def clear_liste():
    liste=[1,2,3,4,5,6,7,8,9,10]
    liste.clear()
    print(liste)
    
#**************************Main************************
def main():
    print("add\n ajout par index:\n")
    ajout_par_index()
    print("ajout par append:\n")
    ajout_par_append()
    print("ajout par insert:\n")
    ajout_par_insert()
    print("ajout par extend:\n")
    ajout_par_extend()
    print("supprimer\n supprimer par index:\n")
    supprimer_par_index()
    print("supprimer par remove:\n")
    supprimer_par_remove()
    print("supprimer par pop:\n")
    supprimer_par_pop()
    print("chercher l'index d'un element:\n")
    chercher_l_index()
    print("copier une liste:\n")
    copier_liste()
    print("reverser une liste:\n")
    reverser_liste()
    print("couter le nombre d'occurence d'un element:\n")
    couter_occurence()
    print("trier une liste:\n")
    trier_liste()
    print("clear une liste:\n")
    clear_liste()

if __name__ == "__main__":
    main()


    