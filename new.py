__author__ = 'Brendan'
#!/usr/bin/env python

from gimpfu import *
import random
import sys
from BasicOperations import *
import traceback

def Generative() :
    try:
        img,layer=initalize(2000,2000)
        finalize(img)
    except: #if program fails, print traceback information to gimp error console
        tb=traceback.format_exc()
        pdb.gimp_message(tb)


register(
    "python_fu_GenerativeScript",
    "GenerativeScript",
    "GenerativeScript",
    "Brendan Degrafft",
    "Brendan Degrafft",
    "2016",
    "Generative",
    "",      # Create a new image, don't work on an existing one
    [],
    [],
    Generative, menu="<Image>/Generative")

main()
