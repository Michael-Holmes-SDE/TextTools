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

"""
You are only allowed to use sys.argv in this file. You should be passing the necessary information from
sys.argv in the tt.py driver program to the Python functions you defined
"""

if len(sys.argv) < 2:  	  	  
    usage()  	  	  
    sys.exit(1)  	  	  
else:  	  	  
    print("TODO: determine which tool the user has invoked")  	  	  
    print("TODO: call on that tool, forwarding any remaining arguments to it")
    tool = sys.argv[2]
    print(tool)  # TEST
    args = []
    i = 3
    while i < len(sys.argv) - 1:
        args.append(sys.argv[i])

    if tool == "cat":
        cat(args)
    # if cat:
    #    cat(["Concatenate.py"])  # Prelim
