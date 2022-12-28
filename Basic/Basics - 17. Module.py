#Modules are useful to store functions that you have created. This allows you tp call upon these modules whilst keeping your main code focusing on the higher logic
#Modules is common practice and allows programmers to share modules

#To create a module, just create a new folder and add .py to the namedef greet():

def greet():
    print("Hello Tom")

#The function greet() is now stored in module.py

import Module

Module.greet()

#To use your module, you have to import it before it can be used