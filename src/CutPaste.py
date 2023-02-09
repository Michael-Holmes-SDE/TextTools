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
    # print("This isn't ready yet")
    # dashF=False, columns=1
    print(args)  # test
    beginning = 0
    if args[0] == "-f":
        dashF = True
        beginning += 1
    else:
        dashF = False
    if len(args) >= 2:
        if "," in args[1]:
            columns = args[1]
            beginning += 1
    else:
        columns = 1
    files = args[beginning:]
    print("files are: " + str(files)) # test

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
    colList = []
    if columns == 1:
        colList = [1]
    elif dashF and columns != 1:
        arr = columns.split(",")
        colList = [int(x) for x in arr if int(x) > 0]
        colList.sort()
        print("colList is: " + str(colList))  # test
    if len(colList) == 0:
        print("Error: A comma-separated field specification is required")
    for file in files:
        f = open(file)
        for line in f:
            line = line.strip()
            arr = line.split(", ")
            for i in range(len(colList)):
                #print("arr" + str(arr)) # test
                if i <= len(colList) - 2:
                    #print("i <=") # test
                    print(arr[colList[i] - 1], end=", ")
                else:
                    # print("else")  # test
                    print(arr[colList[i] - 1], end="")
            print()
# TEST BELOW
# cut(["CUT TEST FILE"])

def paste(args):  	  	  
    # merge lines of files
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
                    print(array[lineNum], end=", ")
            else:
                if array == allArrays[len(allArrays) - 1]:
                    print()
                else:
                    print("", end=", ")
        lineNum += 1

