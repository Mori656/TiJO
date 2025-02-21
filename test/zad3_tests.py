import src.zad3 as z3

def perfect_test():
    assert z3.is_perfect(None) == None, "should be None"
    assert z3.is_perfect(6) == True, "should be True"
    assert z3.is_perfect(9) == False, "should be False"
    print("Testy się powiodły")

if __name__ == "__main__":
    perfect_test()
