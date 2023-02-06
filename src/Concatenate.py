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


def cat(args):  	  	  
    # concatenate files and print on the standard output
    for file in args:
        f = open(file)
        for line in f:
            print(line, end='')
        f.close()


def tac(args):  	  	  
    # concatenate and print files in reverse
    allLines = []
    for file in args:
        f = open(file)
        for line in f:
            allLines.append(line)
        f.close()
    lStart = len(allLines) - 1
    while lStart > -1:
        print(allLines[lStart], end='')
        lStart -= 1


# TESTS (SEEMS TO CHECK OUT COMPLETELY)
#cat(["Concatenate.py"])
#tac(["Concatenate.py"])
