# Software Development Plan

## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
    *   The customer wants us to create Unix text-processing tools using Python. The main program 'tt.py' will take input from the command line in the form 'python src/tt.py TOOL [OPTIONS] FILENAME...' and use its input to choose which tool should be used, passing on the rest of the input to that tool.
    *   The tools should do the following: 
	1. cat: Connects the inputted files and prints them to the command line top to bottom(line-by-line)
	2. tac: Connects the inputted files and prints them to the command line bottom to top(line-by-line)
	3. cut: Extracts columns from a CSV file, only the first column unless columns are specified. The -f flag should be used, and the columns should be printed comma separated if multiple columns are specified.  
	4. paste: Opens each file and stores each file object in a list, then a for loop reads one line from one file and prints with a comma instead of a newline, then prints a line from the other file with a comma instead of a newline, and if those are all the files there is a newline and it starts with printing line two from the first file with a comma at the end, then the second line from file two with a newline if that is the last file 
	5. grep: Prints all lines from inputted files that contain the exact string given in '[OPTIONS]'
        6. head: Prints the top 10 lines of the file(s) (unless another amount is specified with -n in '[OPTIONS]')
	7. tail: Prints the bottom 10 lines of the file(s) (unless another amount is specified with -n in '[OPTIONS]')
	8. sort: Prints the lines of all file(s) in lexical order (use built in 'sort()' function and make a list of all lines to sort, then print the sorted list)
	9. wc: Prints the number of lines, words, and characters (lines are based on the number of '\n' + 1, words are the amount of white-spaces + 1, and characters are the length of all the arrays minus the whitespace or amount of words)
*   [X] Explain the problem this program aims to solve.
    *   A "good" solution is one where running each of these Python tools will yield similar ouputs to ones that the Unix text-tools output given similar inputs, with those being defined above. There should be no crashing and no error messages if input is correct. Ouput should be into the command line and not create a new file unless specified. 
    *   I already know how to do for loops, while loops, prints, debugging, create SDP's, and think my way through a problem.
    *   Some challenges I see coming up are finding out how to get paste and cut to work, as well as getting the arguments from the command line, running the correct function with that, sending the remaining arguments to that function and splitting up those arguments so the function runs as intended
*   [X] List all of the data that is used by the program, making note of where it comes from.
*   **INPUT**	
	1. cat: files 
	2. tac: files
	3. cut: files, -f identifier, [OPTIONAL] columns to print(non-inclusive of end number, and separated by a comma)
	4. paste: files 
	5. grep: files and the string to search for, inputted before the file names
	6. head: files
	7. tail: files 
	8. sort: files
	9. wc: files
*   **OUTPUT**
	1. cat: the text of the two files printed top-to-bottom
	2. tac: the text of the two files printed bottom-to-top, line-by-line
	3. cut: specified or the first column of the file(s) given, comma separated if multiple columns
	4. paste: one row from each file in each row, separated by commas(file1row1, file2row1, \n, file1row2, file2row2, etc.)
	5. grep: all the lines in the file(s) that contain that exact string
	6. head: the first 10 (or another specified amount) of lines of those combined files
	7. tail: the last 10 (or another specified amount) of lines of the combined files
	8. sort: lines from those files sorted in lexical order
	9. wc: the number of lines, words, and characters in those files

*   [X] List the algorithms that will be used (but don't write them yet).
    *   sort()
    *   usage()

## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [X] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    	1. cat
	def cat(args):  # Prints each file passed into args
		for each filename in args
			open a file
			for each line in the file
				print(line), with end='' so no newline
			close the file

	2. tac    
	def tac(args):  # Prints each file passed into args bottom to top
		create empty array allLines
		for file in args
			open file
			for line in file
				append line to allLines array
			close file
		create int variable lStart equal to the length of allLines array - 1
		while int lStart is greater than -1
			print allLines[lStart] with end=""
			decrement lStart by 1
		
	3. cut 
	def cut(args):  # Prints specified columns from a CSV file, specified lines and files passed into args
		initiate int var beginning = 0
		set new boolean var dashF = False
		if the first element in args is "-f"
			set new var dashF = True
			increment beginning by 1
		set new int var columns = 1
		if the length of args is greater than or equal to 2
			set var columns to the 2nd element in args
			increment beginning by 1
		make new list files = args[beginning:]
		create new empty list colList
		if var columns is 1
			colList = [1]
		else if dashF is True and columns is not 1
			var arr = columns split by ","
			colList is all values in arr that are greater than 0
			sort colList
		if colList is empty
			print "Error: A comma-separated field specification is required"
		for file in args
			open file
			for line in file
				set the line equal to itself stripped of whitespace
				set var arr to line splitted by ","
				for all values in colList
					if not the last column
						print value of line from the selected column with line end =","
					if the last column 
						print value of line from the selected column with line end = ""
				print newline
		
	4. paste
	def paste(args):   # Prints files passed into args with comma-separated lines, each line containing the corresponding line of the file
		create blank array allArrays
		for files in args
			create blank array for file
			open a file
			for lines in file
				create string equal to the line stripped using line.strip()
				append line to array
			append array to allArrays
		create int variable maxLines = 0
		for all arrays in allArrays
			if length of array for file is greater than maxLines
				maxLines = length of array
		create int variable lineNum = 0
		while lineNum is less than maxLines
			for all arrays in allArrays
				if lineNum < length of array
					if array is the last in allArrays
						print array[lineNum] with a newline
					else
						print array[lineNum] with end=", "
				else
					if array is the last in allArrays
						print a newline
					else
						print blank with end=", "
			increment lineNum by 1			
		
	5. grep  
	def grep(args, search):  # Prints all lines of files passed into it with args that contain what's in the 'search' parameter
		for each filename in args
			open a file
			for each line in the file
				if line contains 'search';
					print(line), with end='' so no newline
			close the file

	6. head  (same as cat but up to 10 lines, or another specified amount)
	def head(args, lines = 10):	
		for each filename in args
	                open a file
			initialize counting variable 'count' equalling 0
                        for each line in the file
                                if count is greater than or equal to lines
					break
				print(line), with end='' so no newline
				increment 'count' by 1
                        close the file

	7. tail  (same as head but the bottom 10 lines, or another specified amount)
	def tail(args, lines = 10):
		initialize list called allLines
		for each filename in args
			open a file
			for each line in the file
				append line
			close the file
		for line in range(len('allLines) - 11, len(allLines) - 1):
			print(allLines[line]), with end=''
			
	8. sort
	def sort(args):  # Prints lines of files in order according to ASCII value of first character in the line
		initialize list called allLines
		for each filename in args
			open a file
			for each line in the file
				append line
			close the file
		sort the list 'allLines' using Python's sort()
		for line in range(len(allLines)):
			print(allLines[line]), with end=''
	
	9. wc 	 
	def wc(args)  # prints newline, word, and byte counts for each file
		All getting amounts will be done at the same time, but for better readability
			here they will be defined separately
		
		for each file in args
			open file
			initiate var newLines = 0
			initiate var words = 0
			initiate var characters = 0
	
		how to get newline amount
			initialize empty list allNewLines
			for each filename in args
				open file
				initialize int var newLines equal to 0
				for each line in file
					newLines += 1
				append var newLines to list allNewLines
		
		how to get word count
			initialize empty list allWords
			for each filename in args
				open file
				initialize int var words equal to 0
				for each line in file
					initiate var wordsList = the line splitted
					add length of wordsList to var words
				append var words to list allWords
	
		how to get character count
			initialize empty list allCharacters
			for each filename in args
				open file
				initialize int var characters equal to 0
				for each line in file
					characters += getsizeof() the line
				append var characters to list allCharacters
		
		printing everything
			for i in range(allNewLines)
				formatted print allNewLines[i] with no newline, right justed 7 spaces
				formatted print allWords[i] with no newline, right justed 7 spaces
				formatted print allCharacters with no newline, right justed 7 spaces
				formatted print args[i] with newline, right justed 15 spaces
			if length of allNewLines list is greater than 1
				formatted print the sum of allNewLine with no newline, right justed 7 spaces
				formatted print the sum of allWords with no newline, right justed 7 spaces
				formatted print the sum of allCharacters with no newline, right justed 7 spaces
				formatted print "total" with no newline, right justed 12 spaces
			

	10. tt  # The driver program
	set tool string to sys.argv[1]
	if variable tool is equal to "TOOL NAME" (for every tool)
		call tool(args for tool)
		
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
    *   When there is good input, everything goes as expected as outlined in Phase 0
    *   Where there is bad input, Usage() will give an error and end the program

## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [X] More or less working code.
*   [X] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
    *   I learned that sys.argv is a list, which helped with separating parameters given into the command line, I learned again that strings can be separated into a list through a given value, and I learned how to make python files run from the command line correctly and given different parameters


## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [X] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

    *   I ran the test cases in the scripts directory to test my modules
    *   How to access the test cases:
	1. Navigate to the main directory of the program(/cs1440-assn2) in 2 separate command lines
	2. In one of the command lines, type without quotation marks "cd scripts" and press ENTER
	3. In the same command line, type without quote marks "ls" and press ENTER
	4. From the other command line, type without quote marks "scripts/" then the name of one of the files that shows up that includes the name of the module you want to test, including the .sh at the end, and press ENTER
	5. Compare the output to the test cases in GitHub

## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [X] Your repository is pushed to GitLab.
*   [X] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [X] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [X] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   I feel like I know how everything in this program works
	*   If a bug is reported in a few months, it would take me about 30 minutes to find out why
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
	*   I believe so
        *   ...yourself in six month's time?
	*   Definitely
    *   How easy will it be to add a new feature to this program in a year?
	* It should be quite easy to add a new feature because everything is separated into modules
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
	*   This program will continue to work after upgrading any or all of the above
*   [X] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [X] Respond to the **Assignment Reflection Survey** on Canvas.
