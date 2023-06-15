def largest_sum(array:list[int]) -> int:
    arr = []
    m = max(array)
    i = array.index(m)
    arr.append(m)
    if len(array)> 2:
        if i > 1:
            array1, array2 = array[:i-1], array[i+2:]
        else :
            array1, array2 = [0], array[i+2:]
        return largest_sum(array1) + largest_sum(array2) + sum(arr)
    return sum(arr)

def test():
    assert largest_sum([2, 4, 6, 2, 5]) == 13, 'Test 1 Failed'
    assert largest_sum([5, 1, 1, 5]) == 10 , 'Test 2 Failed'
    print('All Tests Passed!')

if __name__ == '__main__':
    test()