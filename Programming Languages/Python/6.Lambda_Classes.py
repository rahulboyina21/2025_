class iamrahul:

    var1= lambda x,y:(x+2)/2
    print(var1(2,4))

# iamrahul

class proper:

    def __init__(self,args):
        self.args=args
    
    def saymyname(args):
        print(args)

# proper("rahul")


# Python class

#1. basic classes 

class base:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.saymyname()
        #Automatic execution in a construcor in a function
    
    def saymyname(self):
        print(f"My name is {self.name} and age is {self.age}")

base("rahul",16)

#2. class methods 

# Yoooo any of the methods which requires @on them is a decorator method you know

class iamgodofants:

    university = "All Mighty University of Central Missouri (UCM) "

    def __init__(self,*args):
        if(len(args)>=2):
            self.name=args[0]
            self.age=args[1]
            self.strength=args[2:]
            self.show()
        else:
            raise Exception("You are welcome to the HELL")
    @classmethod
    def update(cls,newUNI):
        cls.university= f" All Mighty Central Missouri State University (CMSU) and {newUNI} "
    def show(self):
        print(f"My Name is {self.name}\n My Age is {self.age}\n My Strength are {self.strength}\n I am from {self.university}")

def instances():
    x=iamgodofants("Rahul",21,"Best","Power","Programmer")
    x=iamgodofants("a",21,"Best","Power","Programmer")
    x=iamgodofants("Rvdahul",21,"Best","Power","Programmer")
    x=iamgodofants("Rahdveul",21,"Best","Power","Programmer")
    x=iamgodofants("Raeewefhul",21,"Best","Power","Programmer")
    x=iamgodofants("Rawweggweghul",21,"Best","Power","Programmer")
    x=iamgodofants("Rahuweegwegewl",21,"Best","Power","Programmer")
    x=iamgodofants("Rawgewgewgwegewgewgwhul",21,"Best","Power","Programmer")

instances()

iamgodofants.update("TTU")

instances()
 
 # Static Methods 

class SM:
    var = lambda a,b,c: (a**b)/c

    # def __init__(self):
        
    @staticmethod
    def mn(a):
        print(f"{a}")

print(SM.var(20,31,5))
SM.mn("RAHUL BOYINA")

# Public / Private / Protected 
# None / __         / _

class am:
    __pvtvar="Private here"
    _ptdvar="Protected here"


    def __init__(self):
        self.myname="Rahul"
        
    def _ptd():
        print("Protected access granted")

am._ptd()

print(am._ptdvar)


