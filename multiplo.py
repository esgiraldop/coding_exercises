Num1 = 10
Num2 = 2

if Num1 < Num2:
    print("Num1 no es múltiplo de Num2")
else:
    Count = 1
    while Num1 > Num2 * Count:
        if Num2 * Count == Num1:
            break
        Count += 1

    if Num2 * Count == Num1:
        print("Num1 es múltiplo de Num2")
    else:
        print("Num 1 no es múltiplo de Num2")