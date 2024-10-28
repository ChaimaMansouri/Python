"""
{key:value}
{key1:value1,key2:value2}
d={1:"a",2:"b",3:"c"}

key represents comme index
value represents comme element


"""
#exemple 1

def exemple1():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    print(d)
    print(d[a]) # type: ignore
  

#key  values items
def exemple2():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    print(d.keys())
    print(d.values())
    print(d.items())

#utilise for
def exemple3():
    d = {'a': "a", 'aa': "b", 'aaa': "c"}
    for i in d:
        print(i)
    for i in d.keys():
        print(i)
    for i in d.values():
        print(i)
    for i in d.items():
        print(i)
        

#**************main*************
def main():
    print("dictionary")
    exemple1()
    print("key values items")
    exemple2()
    print("utilise for")
    exemple3()
    
if __name__ == "__main__":
    main()