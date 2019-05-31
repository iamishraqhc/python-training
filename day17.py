class InputError(Exception):
    pass


class Calculator:

    def __init__(self):
        pass

    def power(self, n, p):
        if n < 0 and p < 0:
            raise InputError("n and p should be non-negative")

        else:
            return pow(n, p)


myCalculator = Calculator()
T = int(input())
for i in range(0,T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)

    except Exception as e:
        print(e)
