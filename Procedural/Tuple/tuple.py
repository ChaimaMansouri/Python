"""
# ( )
#comme les enregstrments d'un C fixe
#pas de changement possible
#pas de modification possible
#pas de supression possible
#en peut utilise tous les fonction de liste sauf les fonction qui modifient le tuple
"""
#exemple 1
def exmple1():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(tuple)

#exmple 2
def exmple2():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(tuple[0])
    print(tuple[1])
    print(tuple[2])
    print(tuple[3])
    print(tuple[4])
    print(tuple[5])
    print(tuple[6])
    print(tuple[7])
    print(tuple[8])
    print(tuple[9]) 

#exmple 3
def exmple3():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(tuple[0:5])
    print(tuple[6:9])
    print(tuple[0:9:2])
    print(tuple[0:9:3])

#exmple 4
def exmple4():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(tuple[0:])
    print(tuple[:5])
    print(tuple[::2])
    print(tuple[::-1])
    print(tuple[::])

# en peut fait concatenation et repetation pour autre variable
#exmple 5
def exmple5():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    A=tuple+tuple
    print(A)
    A=tuple*5
    print(A)

#max and min 
#exmple 6
def exmple6():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(max(tuple))
    print(min(tuple))

#transformation en liste
#exmple 7
def exmple7():
    tuple=(1,2,3,4,5,6,7,8,9,10)
    print(list(tuple))
    
#************************main************************
def main():
    print("exmple 1")
    exmple1()
    print("exmple 2")
    exmple2()
    print("exmple 3")
    exmple3()
    print("exmple 4")
    exmple4()
    print("exmple 5")
    exmple5()
    print("exmple 6")
    exmple6()
    print("exmple 7")
    exmple7()

if __name__=="__main__":
    main()
