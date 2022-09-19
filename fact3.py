#재귀 호출을 통하여 1부터 n까지의 합 구하기

def fact(n):
    if n <= 1:
        return 1
    return n + fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))