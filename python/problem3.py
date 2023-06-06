import ctypes
import json
# Data given for the problem
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root:Node) -> str:
    return json.dumps(str(vars(root)))         

def deserialize(s:str) -> Node:
    obj = json.loads(s).replace("<__main__.Node object at ", "").replace(">","").lstrip("{").rstrip("}").split(',')
    vals = obj[0].split(':')[1]
    lefts = ctypes.cast(int(obj[1].split(':')[1], base=16), ctypes.py_object).value 
    rights = ctypes.cast(int(obj[2].split(':')[1], base=16), ctypes.py_object).value  
    return Node(val=vals, left=lefts, right=rights)

def test() -> None:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left', "Wrong"

if __name__ == '__main__':
    test()