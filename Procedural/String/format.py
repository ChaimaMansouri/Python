#exmple1
def exmple1():
    print("Hello {}".format("World"))
    print("{} {}".format("Hello","World"))
    print("{1} {0}".format("Hello","World"))
    print("{a} {b}".format(a="Hello",b="World"))
    print("{b} {a}".format(a="Hello",b="World"))
    print("{a} {b} {c}".format(a="Hello",b="World",c="!"))
    
#exmple2
def exmple2():
    s="hi , my name is {}"
    print(s.format("Chaima"))

#exmple3
def exmple3():
    s="hi , my name is {name} age is {age}"
    print(s.format(name="Chaima",age=20))

#***main
if __name__=="__main__":
    exmple1()
    exmple2()
    exmple3()