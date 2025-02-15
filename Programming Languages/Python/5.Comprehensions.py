var1 = [x**2 for x in range(1,6)]

# print(var1)

var2 = {x:"even" for x in range(61) if x%2==0}

# print(var2)

val3 = (x**2 for x in range(999999999999))

while(True):
    print(next(val3))