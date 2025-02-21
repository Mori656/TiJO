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

if __name__ == "__main__":
    assert max(None) == None, "should be None"
    assert max([]) == None, "should be None"
    assert max([1]) == 1, "should be 1"
    assert max([3,3,6,2,8,3]) == 8, "should be 8"