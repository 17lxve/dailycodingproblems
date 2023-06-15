def schedule(f, n:int) -> None:
    from time import sleep
    sleep(n/1000)
    f()

def test():
    schedule(print, 1000)

if __name__ == '__main__':
    test()