"""
 \n = new line
 \t = tab
 \r = carriage return
"""
#len
# return the length of the string example "hello world" return 11
def taille(chaine):
    return len(chaine)

#upper
# return the string in uppercase example "hello world" return "HELLO WORLD"
def majuscule(chaine):
    return chaine.upper()

#lower  
# return the string in lowercase example "HELLO WORLD" return "hello world"
def minuscule(chaine):
    return chaine.lower()


#swapcase
# return the string in opposite case exmple "HELLO WORLD" return "hello world"
def swapcase(chaine):
    return chaine.swapcase()

#capitalize
# return the first letter of the string in uppercase exmple "hello world" return "Hello World"
def capitalize(chaine):
    return chaine.capitalize()

#title
# return the first letter of each word in uppercase exmple "hello world" return "Hello World"
def title(chaine):
    return chaine.title()


#count
# return the number of occurence of a letter
def count(chaine,lettre):
    return chaine.count(lettre)

#find
# return the index of the letter
def find(chaine,lettre):
    return chaine.find(lettre)

#replace
# return the string with the letter replaced
def replace(chaine,lettre):
    return chaine.replace(lettre,"*")

#split
# return the string in a list example "hello world" return ["hello","world"]
def split(chaine):
    return chaine.split()

#join
# return the string with the letter joined example ["hello","world"] return "hello*world"
def join(chaine):
    return "*".join(chaine)

#strip
# return the string without space example "hello world" return "helloworld"
def strip(chaine):
    return chaine.strip()

#lstrip
# return the string without space on the left example "  hello world" return "hello world"
def lstrip(chaine):
    return chaine.lstrip()

#rstrip
# return the string without space on the right example "hello world  " return "hello world"
def rstrip(chaine):
    return chaine.rstrip()

#center
# return the string in the center example "hello world" return "  hello world  "
def center(chaine):
    return chaine.center(10)

#ljust
# return the string in the center example "hello world" return "hello world  "
def ljust(chaine):
    return chaine.ljust(10)

#isalnum()
# return True if the string contains only letters and numbers
def isalnum(chaine):
    return chaine.isalnum()

#isalpha()
# return True if the string contains only letters
def isalpha(chaine):
    return chaine.isalpha()

#isnumeric()
# return True if the string contains only numbers
def isnumeric(chaine):
    return chaine.isnumeric()

#isspace()
# return True if the string contains only spaces
def isspace(chaine):
    return chaine.isspace()

#istitle()
# return True if the string is in title case
def istitle(chaine):
    return chaine.istitle()

#isupper()
# return True if the string is in uppercase
def isupper(chaine):
    return chaine.isupper()

#islower()
# return True if the string is in lowercase
def islower(chaine):
    return chaine.islower()

#************************************Main************************
def main():
    print("taille de la chaine :",taille("hello world"))
    print("chaine en majuscule :",majuscule("hello world"))
    print("chaine en minuscule :",minuscule("HELLO WORLD"))
    print("chaine en swapcase :",swapcase("HELLO WORLD"))
    print("chaine en capitalize :",capitalize("hello world"))
    print("chaine en title :",title("hello world"))
    print("nombre de fois que la lettre 'o' apparait :",count("hello world","o"))
    print("index de la lettre 'o' :",find("hello world","o"))
    print("chaine avec la lettre 'o' remplace :",replace("hello world","o"))
    print("chaine en liste :",split("hello world"))
    print("chaine avec la lettre 'o' joint :",join("hello world"))
    print("chaine sans espaces :",strip("  hello world  "))
    print("chaine avec espaces a droite :",lstrip("  hello world  "))
    print("chaine avec espaces a gauche :",rstrip("  hello world  "))
    print("chaine centre :",center("hello world"))
    print("chaine centre :",ljust("hello world"))
    print("chaine en majuscule :",isalnum("hello world"))
    print("chaine en majuscule :",isalpha("hello world"))
    print("chaine en majuscule :",isnumeric("hello world"))
    print("chaine en majuscule :",isspace("hello world"))
    print("chaine en majuscule :",istitle("hello world"))
    print("chaine en majuscule :",isupper("hello world"))
    print("chaine en majuscule :",islower("hello world"))

if __name__=="__main__":
    main()