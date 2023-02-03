def cat(args):
    """
    for each filename in args
        open a file
        for each line in the file
            print(line), but don't add an extra \n
        close the file
    """

    for file in args:
        f = open(file)
        i = 0
        for line in f:
            if i > 9:
                break
            print(line, end='')
            i += 1
        f.close()


cat(["notes from class.py"])
