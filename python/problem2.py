def mult(integers:list[int]) -> list[int]:
    initial, result = 1, []
    for i in integers:
        temp = integers.copy(); temp.remove(i)
        for j in temp: initial *= j
        result.append(initial)
        initial = 1
    return result

def test():
    # If our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    assert mult([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], "Test 1 failed"
    # If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    assert mult([3,2,1]) == [2, 3, 6], "Test 2 failed"
    # Also we didn't have to use division at all! (And it actually made more sense to me, to be honest)
    print("All test passed!")

if __name__ == '__main__':
    test()