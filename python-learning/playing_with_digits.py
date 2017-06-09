def dig_pow(n, p):
    k = 0
    i = 0

    for digit in str(n):
        k += pow(int(digit), (p + i))
        i += 1

    if k % n == 0:
        return k / n

    return -1

print dig_pow(46288, 3)