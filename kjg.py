from mcpi.minecraft import Minecraft
mc = Minecraft.create

password = "cats"
attempt = input("Please enter the password: ")
if attempt == password:
    print("Password is correct")
print("Program finished")
