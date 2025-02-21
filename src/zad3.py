def is_perfect(n):
    if n == None:
        return None
    if n <= 0:
        return False

    i = 1
    s = 0
    while i < n:
        if n % i == 0:
            s = s + i
        i = i + 1

    if s == n:
        return True
    else:
        return False