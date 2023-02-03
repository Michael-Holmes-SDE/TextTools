# Software Development Plan

## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
    *   The customer wants us to create Unix text-processing tools using Python. The main program 'tt.py' will take input from the command line in the form 'python src/tt.py TOOL [OPTIONS] FILENAME...' and use its input to choose which tool should be used, passing on the rest of the input to that tool.
    *   The tools should do the following: 
	1. cat: Connects the inputted files and prints them to the command line top to bottom(line-by-line)
	2. tac: Connects the inputted files and prints them to the command line bottom to top(line-by-line)
	3. cut: DON'T UNDERSTAND YET
	4. paste: Opens each file and stores each file object in a list, then a for loop reads one line from one file and prints with a comma instead of a newline, then prints a line from the other file with a comma instead of a newline, and if those are all the files there is a newline and it starts with printing line two from the first file with a comma at the end, then the second line from file two with a newline if that is the last file 
	5. grep: Prints all lines from inputted files that contain the exact string given in '[OPTIONS]'
        6. head: Prints the top 10 lines of the file(s) (unless another amount is specified with -n in '[OPTIONS]')
	7. tail: Prints the bottom 10 lines of the file(s) (unless another amount is specified with -n in '[OPTIONS]')
	8. sort: Prints the lines of all file(s) in lexical order (use built in 'sort()' function and make a list of all lines to sort, then print the sorted list)
	9. wc: Prints the number of lines, words, and characters (lines are based on the number of '\n' + 1, words are the amount of white-spaces + 1, and characters are the length of all the arrays minus the whitespace or amount of words)
*   [ ] Explain the problem this program aims to solve.
    *   A "good" solution is one where running each of these Python tools will yield similar ouputs to ones that the Unix text-tools output given similar inputs, with those being defined above. There should be no crashing and no error messages if input is correct. Ouput should be into the command line and not create a new file unless specified. 
    *   I already know how to do for loops, while loops, prints, debugging, create SDP's, and think my way through a problem.
    *   Some challenges I see coming up are finding out how to get paste and cut to work (REVISE)
*   [ ] List all of the data that is used by the program, making note of where it comes from.
*   **INPUT**	
	1. cat: files 
	2. tac: files
	3. cut: DO ONCE I UNDERSTAND
	4. paste: files 
	5. grep: files and the string to search for, inputted before the file names
	6. head: files
	7. tail: files 
	8. sort: files
	9. wc: files, output is 
*   **OUTPUT**
	1. cat: the text of the two files printed top-to-bottom
	2. tac: the text of the two files printed bottom-to-top, line-by-line
	3. cut: DO ONCE I UNDERSTAND
	4. paste: one row from each file in each row, separated by commas(file1row1, file2row1, \n, file1row2, file2row2, etc.)
	5. grep: all the lines in the file(s) that contain that exact string
	6. head: the first 10 (or another specified amount) of lines of those combined files
	7. tail: the last 10 (or another specified amount) of lines of the combined files
	8. sort: lines from those files sorted in lexical order
	9. wc: the number of lines, words, and characters in those files

*   [ ] List the algorithms that will be used (but don't write them yet).
    *   sort()
    *   MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE MORE

## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    	1. cat
	def cat(args):
		for each filename in args
			open a file
			for each line in the file
				print(line), with end='' so no newline
			close the file
	2. tac  (will be cat but lowest line first, top line last)
	def tac(args):
		
	3. cut  (later)
	def cut( SOMETHING ):
		
	4. paste (later)
	def paste( SOMETHING):
		
	5. grep  (same as cat but with an if statement for the keywords searching for by the print statement
	def grep(args, search):
		for each filename in args
			open a file
			for each line in the file
				if line contains 'search';
					print(line), with end='' so no newline
			close the file
	6. head  (same as cat but up to 10 lines)
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
	7. tail  (same as head but the bottom 10 lines) (PRELIMINARY)
	def tail(args, lines = 10):
		initialize list called allLines
		for each filename in args
			open a file
			for each line in the file
				append line
			close the file
		for lines in range(len('allLines) - 10, len(allLines)):
			print(allLines[lines])
			
	8. sort
	def tail(args, lines = 10):
		initialize list called allLines
		for each filename in args
			open a file
			for each line in the file
				append line
			close the file
		sort the list 'allLines' using Python's sort()
		for lines in range(len(allLines)):
			print(allLines[lines])
	
	9. wc 	 (prints newline, word, and byte counts for each file)
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing


## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
