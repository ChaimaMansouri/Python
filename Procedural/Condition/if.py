#maximum 
def max(a,b):
    if a>b:
        return a
    else:
        return b

#minimum
def min(a,b):
    if a<b:
        return a
    else:
        return b
    
#admin
def admin(a):
    if a=="admin":
        return True
    else:
        return False

#write python program to check if the number entered by user is even or odd
def evenodd(a):
    if a%2==0:
       print("Even")
    else:
       print("Odd")

#write python program to check if the number entered by user is positive or negative
def posneg(a):
    if a>0:
        return True
    else:
        return False
    
#write python program to check if the number entered by user is greater than 100
def greater(a):
    if a>100:
       print("Greater")
    else:
       print("Less")
       
#************************************Main************************
def main():
    print("maximum of 2 and 3 is :",max(2,3))
    print("minimum of 2 and 3 is :",min(2,3))
    print("admin of admin is :",admin("admin"))
    evenodd(int(input("saisir un nombre :")))
    print("posneg of 2 is :",posneg(2))
    greater(int(input("saisir un nombre :")))

if __name__ == "__main__":
    main()
    
       
