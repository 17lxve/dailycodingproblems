class Recorder:
    def __init__(self) -> None:
        self.log = []
    
    def record(self, order_id:int) -> None: 
        #adds the order_id to the log
        self.log.append(order_id)
    def get_last(self, i): 
        #gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
        return self.log[-i]

def test():
    logger = Recorder()
    for i in range(10): logger.record(i+1)
    assert logger.get_last(2) == 9, 'Test 1 Failed'
    print('All Test Passed!')

if __name__ == '__main__':
    test()