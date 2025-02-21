import src.zad2 as z2

def perfect_test():
    assert z2.max(None) == None, "should be None"
    assert z2.max([]) == None, "should be None"
    assert z2.max([1]) == 1, "should be 1"
    assert z2.max([3,3,6,2,8,3]) == 8, "should be 8"
    print("Testy się powiodły")

if __name__ == "__main__":
    perfect_test()