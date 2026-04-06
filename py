def superPow(a, b):
    MOD = 1337
    
    def power(x, n):
        res = 1
        x %= MOD
        for _ in range(n):
            res = (res * x) % MOD
        return res
    
    result = 1
    for digit in b:
        result = power(result, 10) * power(a, digit) % MOD
    
    return result


a, n = map(int, input().split())
b = [int(input()) for _ in range(n)]

ans = superPow(a, b)
print(ans)
