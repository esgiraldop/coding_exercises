def riverSizes(matrix):
    # Write your code here.
    already_counted = [[], []]  # pairs containing positions of 1's already counted
    river_sizes = list()
    river_size = 0
    numrows, numcols = len(matrix), len(matrix[0])
    for i in range(numrows):
        for j in range(numcols):
            if matrix[i, j] == 1 and i not in already_counted[0] and j not in already_counted[1]:
                # found the first 1 of a river
                pend2sweeparound = [[i], [j]]
                river_size = 0
                already_counted[0].append(i)
                already_counted[1].append(j)
                river_size += 1
                # sweep around
                dirs = [[i, j + 1], [i + 1, j], [i, j - 1], [i - 1, j]]  # right, down, left and up

                while len(pend2sweeparound[0]) > 0:
                    for x, y in dirs:
                        if matrix[x, y] == 1 and x not in already_counted[0] and y not in already_counted[1]:
                            river_size += 1
                            pend2sweeparound[0].append(x)
                            pend2sweeparound[1].append(y)