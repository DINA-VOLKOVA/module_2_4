my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
primes = []
not_primes = []

for i in range(len(my_list)):
    is_prime = True
    n = my_list[i]
    if n < 2:
        print(n, '- не простое и не составное число')
        continue
    else:
        f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break

    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True
print('Primes', primes)
print('Not Primes', not_primes)
