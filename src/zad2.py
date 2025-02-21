def max(digits):
    i = 0
    maxd = None
    if digits == None:
        return maxd

    if len(digits) > 0:
        maxd = digits[i]
        i = i + 1
    else:
        return maxd

    while i < len(digits):
        if maxd < digits[i]:
            maxd = digits[i]
        i = i + 1
    return maxd