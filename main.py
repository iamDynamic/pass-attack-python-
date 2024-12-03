import random
import time

Pass = 354

i = list("01234567890")

i1 = random.choice(i)
i2 = random.choice(i)
i3 = random.choice(i)

res = i1+i2+i3

while int(res) != int(Pass):
    
    if int(res) == int(Pass):
        break
    else:
      i = list("01234567890")
  
      i1 = random.choice(i)
      i2 = random.choice(i)
      i3 = random.choice(i)
      
      res = i1+i2+i3
      print(res)
      time.sleep(0.1)
    