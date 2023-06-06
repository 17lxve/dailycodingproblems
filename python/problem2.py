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
    print(mult([1, 2, 3, 4, 5]))
    # If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    print(mult([3,2,1]))
    # Also we didn't have to use division at all! (And it actually made more sense to me, to be honest)

if __name__ == '__main__':
    test()