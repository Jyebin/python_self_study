def gcd(a,b):
    print("gcd : ",a,b)
    if b == 0:
        return a
    return gcd(b, a%b) #좀 더 작은 값으로 자기 자신을 호출

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))