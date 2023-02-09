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
    beginning = 0
    dashF = False
    if args[0] == "-f":
        dashF = True
        beginning += 1
    columns = 1
    if len(args) >= 2:
        columns = args[1]
        beginning += 1
    files = args[beginning:]
    colList = []
    if columns == 1:
        colList = [1]
    elif dashF and columns != 1:
        arr = columns.split(",")
        colList = [int(x) for x in arr if int(x) > 0]
        colList.sort()
    if len(colList) == 0:
        print("Error: A comma-separated field specification is required")
    for file in files:
        f = open(file)
        for line in f:
            line = line.strip()
            arr = line.split(",")
            for i in range(len(colList)):
                if i <= len(colList) - 2:
                    print(arr[colList[i] - 1], end=",")
                else:
                    print(arr[colList[i] - 1], end="")
            print()


def paste(args):
    allArrays = []
    for file in args:
        array = []
        f = open(file)
        for line in f:
            string = line.strip()
            array.append(string)
        allArrays.append(array)
    maxLines = 0
    for array in allArrays:
        if len(array) > maxLines:
            maxLines = len(array)
    lineNum = 0
    while lineNum < maxLines:
        for array in allArrays:
            if lineNum < len(array):
                if array == allArrays[len(allArrays) - 1]:
                    print(array[lineNum])
                else:
                    print(array[lineNum], end=",")
            else:
                if array == allArrays[len(allArrays) - 1]:
                    print()
                else:
                    print("", end=",")
        lineNum += 1
