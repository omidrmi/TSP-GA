import random


c = 0
c2 = 0
c3 = 0

for i in range(1000000):
    x = random.randint(0, 99)
    if x < 5:
        c += 1 
    if x > 94:
        c2 += 1 
    if 39 <  x < 45:
        c3 += 1  
      
print("c {}".format(c))
print("c2 {}".format(c2))
print("c3 {}".format(c3))