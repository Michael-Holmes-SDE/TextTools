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
    # print("TODO: determine which tool the user has invoked")
    # print("TODO: call on that tool, forwarding any remaining arguments to it")
    tool = sys.argv[1]
    print(tool)  # TEST
    print(type(sys.argv[2]))

    if tool == "cat":
        cat(sys.argv[2:])
    if tool == "tac":
        tac(sys.argv[2:])
    if tool == "cut":  # possibly needs -f
        """print("made it in") # test
        print(sys.argv)
        length = len(sys.argv)
        beginning = 2
        if "-f" in sys.argv:
            f = True
            beginning += 1
        else: f = False
        columns = False
        if "," in sys.argv:
            print("',' found") # test
            columns = sys.argv[:length - 1]
            beginning += 1
        print("',' not found") # test
        print("length = " + str(length))  # test
        print("beginning is: " + str(beginning))  # test
        files = sys.argv[beginning:length]
        print("files: " + str(files)) # test
        if columns:
            cut(files, f, columns)
        else: cut(files, f)"""
        cut(sys.argv[2:])
    if tool == "paste":
        paste(sys.argv[2:])
    if tool == "grep":  # possible needs -v
        grep(sys.argv[3:], sys.argv[2])
    if tool == "head":
        sys.argv[2] = int(sys.argv[2])
        #if int(sys.argv[2]) is int:
        head(sys.argv[3:], int(sys.argv[2]))
        #else: head(sys.argv[2:])
    if tool == "tail":
        if sys.argv[2] is int:
            tail(sys.argv[3:], int(sys.argv[2]))
        else:
            tail(sys.argv[2:])
