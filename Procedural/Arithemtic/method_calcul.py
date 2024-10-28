#calcul abs
def abs(a):
    return abs(a)

#calcul la somme de deux nombres
def somme(a,b):
    return sum(a,b)

#calcul la divmod de deux nombres
def divmod(a,b):
    return divmod(a,b)

#calcul la puissance de deux nombres
def puissance(a,b):
    return pow(a,b)

#calcul la racine carre de deux nombres
def racine_carre(a):
    return pow(a,0.5)

#calcul ~~ de deux nombres
def division_entiere(a):
    return round(a,3)

#**************************************Main************************
def main():
    print("methode 1 : les nombres sont entre 2 et 3 \n")

    print("la somme de 2 et 3 est : \t",somme(2,3))
    print("la divmod de 2 et 3 est :\t",divmod(2,3))
    print("la puissance de 2 et 3 est :\t",puissance(2,3))
    print("la racine carre de 2 est :\t",racine_carre(2))       

    print("\n methode 2 : les nombres by user \n")
    a=input("saisir le premier nombre :")
    b=input("saisir le deuxieme nombre :")
    print("la somme de {} et {} est : \t".format(a,b),somme(int(a),int(b)))
    print("la divmod de {} et {} est :\t".format(a,b),divmod(int(a),int(b)))
    print("la puissance de {} et {} est :\t".format(a,b),puissance(int(a),int(b)))
    print("la racine carre de {} est :\t".format(a),racine_carre(int(a)))