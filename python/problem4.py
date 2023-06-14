def missing(array:list[int]) -> int:
    curr = 1
    while True:
        if curr in array:
            curr += 1
        else:
            return curr
        
def test() -> None:
    # For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
    array1 = [3, 4, -1, 1]
    array2 = [1,2,0]
    assert missing(array1) == 2, "Test 1 Failed"
    assert missing(array2) == 3, "Test 2 Failed"
    print("All tests passed!")

if __name__ == '__main__':
    test()