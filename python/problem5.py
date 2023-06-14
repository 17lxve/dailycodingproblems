# I absolutely could not figure this out by myself (And honestly i still don't quite understand)
# Big thanks to Nikita Galaiko for his answer and explanation
# You can find it on his blog at https://nikita.galaiko.rocks/posts/dcp/problem-5/

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)


def test():
    assert car(cons(3,4)) == 3, "Test 1 failed"
    assert cdr(cons(3,4)) == 4, "Test 2 failed"
    print("All tests passed!")

if __name__ == '__main__':
    test()
    
