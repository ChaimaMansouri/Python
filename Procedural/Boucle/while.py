#affiche les nombre 1 a 10
def oneto10():
    i=1
    while i<=10:
        print(i)
        i+=1

#correct password
def password():
    while password!="password":
        password=str(input("saisir le mot de passe :"))
    print("mot de passe correct")
    
#Somme des nombres naturels
def sommanat():
    i=1
    somme=0
    while i<=10:
        somme+=i
        i+=1
    print(somme)
    
#******************main******************
def main():
    oneto10()
    password()
    sommanat()

if __name__=="__main__":
    main()