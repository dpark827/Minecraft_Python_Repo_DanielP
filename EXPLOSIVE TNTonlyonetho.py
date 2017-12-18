from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

#while True:
#block = 51
#mc.setBlocks(-1,20,-1,11,30,11,block)
pos = mc.player.getPos()
block = 46
state = 1
mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x,pos.y-1,pos.z,block,state)
