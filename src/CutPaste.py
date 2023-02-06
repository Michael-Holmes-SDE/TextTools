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


def cut(args):  	  	  
    # remove sections from each line of files
    print("This isn't ready yet")




def paste(args):  	  	  
    # merge lines of files
    toPrint = ["Nothing appended"]  # test
    lineNum = 0
    """maxLines = 1
    for file in args:
        f = open(file)
        if len(f) > maxLines:
            maxLines = len(f)
        print(len(f))"""
    fileAmt = len(args)
    while lineNum < 30:  #(while lineNum < maxLines + 1)
        fileCrnt = 0
        while fileCrnt < fileAmt:
            f = open(args[fileCrnt])
            for line in f:
                if line == lineNum:
                    toPrint.append(line)
                    print(line)  # test
            fileCrnt += 1
            print("fileCrnt is: " + str(fileCrnt))  # test
        lineNum += 1
        print("lineNum is: "+ str(lineNum))
    for line in toPrint:
        print(line, end=", ")
