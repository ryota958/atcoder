def make_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors
print(make_divisors(12)) # [1, 2, 3, 4, 6, 12]
print(make_divisors(13)) # [1, 13]