def binary_numbers(n:int) -> list:
    rems = []
    while True:
        rems.append((n % 2))
        if n < 2:
            break
        n = int((n-(n % 2))/2)
    binNum = rems[::-1]
    return binNum

def countMaxOnes(binNum: list[int]) -> None:
    oldcount, newcount = 0, 0
    for num in binNum:
        if num == 1:
            newcount += 1
            if newcount > oldcount:
                oldcount = newcount
        else:
            newcount = 0

    print(oldcount)

if __name__ == '__main__':
    #n = int(input().strip())
    n = 439
    binNum = binary_numbers(n)
    countMaxOnes(binNum)