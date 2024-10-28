#exmple 1
def exmple1():
    print("Hello World")
    print('Hello World')           #in pyton ' and " is same
    print('''Hello World''')       
    print("""Hello World""")
    print("Hello " + "World")
    print(str(42) + " is the answer")
    s="Hello World"
    print(s)
    print(str(input("Enter your name : ")))


#exmple 2
# chaque caractere est lie par un indice
# en peut etre negatif (lire de droite a gauche)
# et en peut etre positif (lire de gauche a droite)
def exmple2():
    s="Hello World"
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[3])
    print(s[-4])
    print(s[-3])
    print(s[-2])
    print(s[-1])
    

#exmple 3
# [start:stop:step] area de la chaine a afficher
# [start:stop] area de la chaine a afficher
# [::step] step
# [start:] area de la chaine a afficher
# [:stop] area de la chaine a afficher
# [::-1] area de la chaine a afficher de droite a gauche
# [::]  and [:] is same 
def exmple3():
    s="Hello World"
    print(s[0:5])
    print(s[6:11])
    print(s[0:11:2])
    print(s[0:])
    print(s[:5])
    print(s[::2])
    print(s[::-1])
    print(s[::])


#exmple 4
def exmple4():
   print("Hello " + "World")# space between Hello and World in "  "
   print("Hello" + "23 ") #concate Hello and 23  if 23 is string 
   

#exmple 5
# * represent the number of repetitions to string
def exmple5():
    print("Hello " * 5)
    

#**************************Main************************
def main():
    exmple1()
    exmple2()
    exmple3()
    exmple4()
    exmple5()

if __name__ == "__main__":
    main()
