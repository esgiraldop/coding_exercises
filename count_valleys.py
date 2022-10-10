def countingValleys(steps, path):
    level = 0
    num_valleys = 0
    num_mountains = 0
    for step in path:
        prev_level = level
        if step == 'D':
            level -= 1
        else:
            level += 1
        print(level)
        if prev_level == -1 and level == 0:
            num_valleys += 1
        elif prev_level == 1 and level == 0:
            num_mountains += 1

    return num_valleys

if __name__ == '__main__':
    steps = 8
    path =  'UDDDUDUU'
    num_valleys = countingValleys(steps, path)
    print('The number of valleys is: ', num_valleys)