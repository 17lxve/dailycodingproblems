def addup(numbers:list, k:int) -> bool:
    for index1 in range(len(numbers)):
        for index2 in range(len(numbers)):
            if index1 == index2:
                continue
            if numbers[index1] + numbers[index2] == k:
                print(f"Solution: {numbers[index1]} + {numbers[index2]} = k({k})")
                return True
    return False

def addup_once(numbers:list, k:int) -> bool:
    for x in numbers:
        if k-x in numbers:
            print(f"Solution: {x} + {k-x} = k({k})")
            return True
    return False

def addup_once_avoid_duplication(numbers:list, k:int) -> bool:
    for x in numbers:
        temp = numbers.copy()
        temp.remove(x)
        if k-x in temp:
            print(numbers.copy().remove(x))
            print(f"Solution: {x} + {k-x} = k({k})")
            return True
    return False

def test():
    # Given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
    print(addup([10, 15, 3, 7],17))
    print(addup_once([10, 15, 3, 7],17))
    print(addup_once_avoid_duplication([10, 15, 3, 7],17))
    
    # Given [10, 15, 3, 7] and k of 20, return false since no sum amounts to 20, except for 10+10 which is just self-addition, and not what we want
    print(addup([10, 15, 3, 7],20))
    print(addup_once([10, 15, 3, 7],20))
    print(addup_once_avoid_duplication([10, 15, 3, 7],20))

test()