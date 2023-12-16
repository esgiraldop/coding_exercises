def hourglass(arr: list[int]) -> None:
    hourglass_arr = []
    for i in range(1,len(arr)-1):
        for j in range(1, len(arr[0])-1):
            hourglass_arr.append(arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j-1]
             + arr[i+1][j+1])

    print(max(hourglass_arr))

if __name__ == '__main__':

    arr = []
    '''arr = [
        [1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]'''
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass(arr)