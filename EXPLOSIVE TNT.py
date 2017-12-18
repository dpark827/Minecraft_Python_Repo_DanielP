from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

#while True:
#block = 51
#mc.setBlocks(-1,20,-1,11,30,11,block)
pos = mc.player.getPos()
block = 46
state = 1
mc.setBlocks(pos.x+10,pos.y+10,pos.z+10,pos.x-10,pos.y+20,pos.z-10,block,state)
#sleep(3)
#mc.postToChat("EVACUATE TACTICLE NUKE INCOMING")
#mc.player.setTilePos(100,100,50)
