def longest_substring(k:int, s:str) -> int:
    sub = ''
    counter = 0
    subs, lengths = [], []
    while len(s) > k:
        for x in s:
            if x in sub:
                sub += x
            else:
                counter += 1
                sub += x
            if counter > k:
                subs.append(sub[:-1])
                lengths.append(len(sub[:-1]))
                s = s[1:]
                sub = ''
                counter = 0
                break
    return max(lengths)
       
       

def test():
    assert longest_substring(2, 'abcba') == 3, 'Test 1 failed'
    print("All Tests Passed!")

if __name__ == '__main__':
    test()