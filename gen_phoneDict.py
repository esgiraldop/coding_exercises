# Enter your code here. Read input from STDIN. Print output to STDOUT

def gen_phoneDict(n:int) -> None:
    phone_dict = dict()

    phone_dict = dict(input().split() for x in range(n))

    name = "Hola"
    while True:
        try:
            name = input().strip()
            if name not in phone_dict.keys():
                print("Not found")
                continue
            print(name + "=" + phone_dict[name])
        except:
            break

if __name__ == "__main__":
    n = int(input())
    gen_phoneDict(n)