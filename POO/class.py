#class name :
#def __init__(self,................):
#self = attribute ajout dans toute les methode de class et constructeur
#le nom de constructeur est __init__
#self.var = var  #ajout d'un attribut dans le constructeur
#en peut acceder aux attribut de la classe avec object.var

class Personne:
    annee=2023
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def afficher(self):
        print("nom :",self.nom)
        print("prenon :",self.prenom)
        print("age :",self.age)
    
def main():
    p = Personne("Chaima","Said",20)
    p.afficher()
    print("annee :",p.annee)

main()
