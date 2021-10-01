def indexLocator (char,cipherKeyMatrix):
    indexOfChar = []

    # convert the character value from J to I
    if char=="J":
        char = "I"

    for i,j in enumerate(cipherKeyMatrix):
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']), 
        #   (2, ['H', 'I', 'L', 'M', 'O']), 
        #   (3, ['P', 'Q', 'S', 'T', 'U']), 
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]


        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
        for k,l in enumerate(j):

            # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar