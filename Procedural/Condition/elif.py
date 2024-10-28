#date naissance
def date(a,b,c):
    if a==06 :
        if b==07 :
            if c==2004 :
                return True
            else:
                return False
        else:
            return False


#**********************main****************
def main():
    a=int(input("saisir le jour :"))
    b=int(input("saisir le mois :"))
    c=int(input("saisir l'annee :"))
    if date(a,b,c):
        print("date valide")
    else:
        print("date invalide")
        
        
    
if __name__=="__main__":
    main()