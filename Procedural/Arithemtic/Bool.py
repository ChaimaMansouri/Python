#the first exmple 
def simple():
    x = 5
    y = 8
    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x < y:", x < y)
    print("x > y:", x > y)
    print("x <= y:", x <= y)
    print("x >= y:", x >= y)
    S = "Sammy"
    s = "sammy"
    print("Sammy == sammy: ", S== s) 

#the second example (logique mathematique)
def simple2():
    print("\nLogique mathematique\n")
    print("\n True and True:", (1<3) and 1==1)   #and
    print("True or False:", True or False)    #or
    print("Not True:", not True)              #not
    print("Not false and true", not (1>3) and 1==1)
    
def main():
    simple()
    simple2()

if __name__ == "__main__":
    main()
