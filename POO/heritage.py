#Dans l'heiritage  child class en declare comme NOM(parent class)
#utilise constructeur du parent class super().__init__(self)
#en peut fait multi-heritage class(parent1,parent2)

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
        
   
    
#*****************main********************
def main():
    e = Eleve("Chaima","Said",20,"2eme")
    e.afficher()


main()