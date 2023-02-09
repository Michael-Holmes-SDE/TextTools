#!/usr/bin/env python  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  


import sys  	  	  

from Concatenate import cat, tac  	  	  
from CutPaste import cut, paste  	  	  
from Grep import grep  	  	  
from Partial import head, tail  	  	  
from Sorting import sort  	  	  
from WordCount import wc  	  	  
from Usage import usage  	  	  


if len(sys.argv) < 2:
    usage()  	  	  
    sys.exit(1)  	  	  
else:
    tool = sys.argv[1]
    if tool == "cat":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        cat(sys.argv[2:])
    if tool == "tac":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        tac(sys.argv[2:])
    if tool == "cut":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        cut(sys.argv[2:])
    if tool == "paste":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        paste(sys.argv[2:])
    if tool == "grep":
        dashV = False
        send = 3
        if len(sys.argv[send:]) == 0:
            print("Error: Too few arguments")
        else:
            if sys.argv[2] == "-v":
                send += 1
                dashV = True
            grep(sys.argv[send:], sys.argv[send - 1], dashV)
    if tool == "head":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        else:
            if sys.argv[2] == "-n":
                head(sys.argv[4:], int(sys.argv[3]))
            else:
                head(sys.argv[2:], 10)
    if tool == "tail":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        else:
            if sys.argv[2] == "-n":
                tail(sys.argv[4:], int(sys.argv[3]))
            else:
                tail(sys.argv[2:], 10)
    if tool == "sort":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        sort(sys.argv[2:])
    if tool == "wc":
        if len(sys.argv[2:]) == 0:
            print("Error: Too few arguments")
        wc(sys.argv[2:])
