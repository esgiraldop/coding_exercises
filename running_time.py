import math
def prime_notPrime(data):
    if data < 2:
        print("Not prime")
        return

    for i in range(2, int(math.sqrt(data)) + 1):
        if data % i == 0:
            print("Not prime")
            return

    print("Prime")
T = 3
datas = [12, 5, 7]
for data in datas:
    prime_notPrime(data)