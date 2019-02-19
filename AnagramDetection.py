def anagramSolution(s1,s2):
    if len(s1) != len(s2):
        equality = False

    alist = list(s2)

    pos1 = 0
    equality = True

    while pos1 < len(s1) and equality:


