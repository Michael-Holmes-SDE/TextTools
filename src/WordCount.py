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


def wc(files):
    allNewLines = []
    allWords = []
    allCharacters = []
    for file in files:
        f = open(file)
        newLines = 0
        words = 0
        characters = 0
        for line in f:
            newLines += 1
            wordsList = line.split()
            words += len(wordsList)
            characters += len(line)
        allNewLines.append(newLines)
        allWords.append(words)
        allCharacters.append(characters)
    for i in range(len(allNewLines)):
        print(str(allNewLines[i]).rjust(7), end="")
        print(str(allWords[i]).rjust(7), end="")
        print(str(allCharacters[i]).rjust(7), end="")
        print(str(files[i]).rjust(20))
    if len(allNewLines) > 1:
        print(str(sum(allNewLines)).rjust(7), end="")
        print(str(sum(allWords)).rjust(7), end="")
        print(str(sum(allCharacters)).rjust(7), end="")
        print("total".rjust(12))
