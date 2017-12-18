import random
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#count = 0

while True:
    #print(count)
    
    x = random.randint(-127,127)
    y = random.randint(50, 64)
    z = random.randint(-127,127)

    mc.setBlock(x,y,z,8)

    print("loop Finished")
