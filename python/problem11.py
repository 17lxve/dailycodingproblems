def predict(query:str, d:list[str]):
    return [x for x in d if x[:len(query)] == query]

def test():
    assert predict('de', ['dog', 'deer', 'demon']) == ['deer', 'demon'], 'Test 1 Failed'
    print('All Test Passed!')

if __name__ == '__main__':
    test()