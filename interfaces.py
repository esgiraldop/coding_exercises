class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        is_divisor = [1]
        for i in range(2, n+1):
            if n%i == 0 and i not in is_divisor:
                is_divisor.append(i)

        return sum(is_divisor)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)