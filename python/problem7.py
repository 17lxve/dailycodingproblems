# Stuck, but i'll also skip for now
# Keep studying

from string import ascii_lowercase as lw

def isDecodable(mapping:dict, message:str):
    return True if int(message) in mapping.keys() else False

def ways(mapping:dict, message: str) : 
    res = []
    for i in range(len(message) - 1):
        if isDecodable(mapping,message[i:i+2]):
            res.append(message[i:i+2])
    print(res)
    return (len(res)  + 1 ) 
            
def test():
    mapping = dict([(int(lw.index(letter))+1,letter) for letter in lw])
    assert ways(mapping=mapping, message='111') == 3, 'Test 1 Failed'
    print('All Tests Passed!')

if __name__ == '__main__':
    test()