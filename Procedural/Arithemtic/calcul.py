#calcul la somme de deux nombres
def somme(a,b):
    return a+b

#calcul la soustraction de deux nombres
def soustraction(a,b):
    return a-b

#calcul la multiplication de deux nombres       
def multiplication(a,b):
    return a*b

#calcul la division de deux nombres   
def division(a,b):
    return a/b      

#calcul le modulo de deux nombres
def mod(a,b):
    return a%b

#calcul la puissance de deux nombres
def puissance(a,b):
    return a**b

#calcul la racine carre de deux nombres
def racine_carre(a):
    return a**0.5

#calcul // de deux nombres
def division_entiere(a,b):
    return a//b

#change signe 
def change_signe_negatif(a):
    return -a

def change_signe_positif(a):
    return a




# ********************************************Main
def main():
    print("methode 1 : les nombres sont entre 2 et 3 \n") 
    
    print("la somme de 2 et 3 est : \t",somme(2,3))
    print("la soustraction de 2 et 3 est :\t",soustraction(2,3))
    print("la multiplication de 2 et 3 est :\t",multiplication(2,3))
    print("la division de 2 et 3 est :\t",division(2,3))
    print("le modulo de 2 et 3 est :\t",mod(2,3))
    print("la puissance de 2 et 3 est :\t",puissance(2,3))
    print("la racine carre de 2 est :\t",racine_carre(2))
    print("la division entiere de 2 et 3 est :\t",division_entiere(2,3))
    print("change_signe_negatif de 2 est :\t",change_signe_negatif(2))
    print("change_signe_positif de 2 est :\t",change_signe_positif(2))
   
    
    print("\n methode 2 : les nombres by user \n")
    a=input("saisir le premier nombre :")
    b=input("saisir le deuxieme nombre :")
    print("la somme de {} et {} est : \t".format(a,b),somme(int(a),int(b)))
    print("la soustraction de {} et {} est :\t".format(a,b),soustraction(int(a),int(b)))
    print("la multiplication de {} et {} est :\t".format(a,b),multiplication(int(a),int(b)))
    print("la division de {} et {} est :\t".format(a,b),division(int(a),int(b)))
    print("le modulo de {} et {} est :\t".format(a,b),mod(int(a),int(b)))
    print("la puissance de {} et {} est :\t".format(a,b),puissance(int(a),int(b)))
    print("la racine carre de {} est :\t".format(a),racine_carre(int(a)))
    print("la division entiere de {} et {} est :\t".format(a,b),division_entiere(int(a),int(b)))
    print("change_signe_negatif de {} est :\t".format(a),change_signe_negatif(int(a)))
    print("change_signe_positif de {} est :\t".format(a),change_signe_positif(int(a)))
    
    
    
    
    

if __name__ == "__main__":
    main()