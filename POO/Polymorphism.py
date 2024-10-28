#en peut utiliser la meme methode pour different classes et meme nom de methode
#overriding (surcharge de methode)
#en peut insert nom de class dans methode et utilise object de autre classe page 366


#class parent
class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def afficher(self):
        print("nom :",self.nom)
        print("prenon :",self.prenom)
        print("age :",self.age)

#class child    
class Eleve(Personne):
    def __init__(self,nom,prenom,age,classe):
        super().__init__(nom,prenom,age)
        self.classe = classe

    def afficher(self):
        super().afficher()
        print("classe :",self.classe)
        

#**************Main**************
def main():
    e = Eleve("Chaima","Said",20,"2eme")
    e.afficher()


main()
