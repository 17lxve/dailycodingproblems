class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    def set_right(self,value):
        self.right = Node(value=value)
    def set_left(self,value) :
        self.left = Node(value=value)

def unival(node : Node) -> int:
    if node == None:
        return 0
    if node.left != None and node.right != None:
        res = node.left.value == node.right.value == node.value
    elif node.left != None:
        res = node.left.value == node.value
    elif node.right != None:
        res = node.right.value == node.value
    else:
        return 1
    return res + unival(node=node.left) + unival(node=node.right)

def test():
    # Tree setting
    root = Node(0); root.set_left(1); root.set_right(0)
    root.right.set_left(1); root.right.set_right(0)
    root.right.left.set_left(1); root.right.left.set_right(1)
    
    #Test 1
    assert unival(root) == 5, 'Test 1 Failed'
    print("All tests passed!")
if __name__ == '__main__':
    test()