'''
The dynamic programming approach used here is something i knew
back from college, and i totally understand everything 
except the correlation between the problem and the Fibonacci sequence
'''

def solution(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]                
            

def test():
    assert solution(4) == 5, 'Test 1 Failed'
    print('All Tests Passed!')
    
    
if __name__ == '__main__':
    test()