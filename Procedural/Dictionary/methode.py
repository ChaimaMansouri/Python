#update
#exemple1
#affiche {'a': "a", 'aa': "b", 'aaa': "c", 'b': "b", 'bb': "c", 'bbb': "d"} 
# role de add si cles n'existe pas et update si cles existe
"""
fait meme methode de liste
"""
def exmple1():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d.update({'b': "b", 'bb': "c", 'bbb': "d"})
    print(d)

#clear
#supprime tout le dictionnaire
def exmple2():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d.clear()
    print(d)

#copy
#copie le dictionnaire
def exmple3():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d1 = d.copy()
    print(d1)

#pop
#supprime un element du dictionnaire    
def exmple4():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d.pop('a')
    print(d)

#popitem
#supprime le dernier element du dictionnaire
def exmple5():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d.popitem()
    print(d)

#setdefault
#affiche {'a': "a", 'aa': "b", 'aaa': "c", 'b': "b"}
def exmple6():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    d.setdefault('b')
    print(d)
    
#*******************main***********************
def main():
    print("update")
    exmple1()
    print("clear")
    exmple2()
    print("copy")
    exmple3()
    print("pop")
    exmple4()
    print("popitem")
    exmple5()
    print("setdefault")
    exmple6()

if __name__ == "__main__":
    main()
