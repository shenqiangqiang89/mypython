
def Fib(max_num):
    i = 0
    a,b = 1,1
    while i < max_num:
        yield a
        a,b = b, a+b
        i = i+1

def test_endless_iter():
    '''
    生成无限序列
    :return:
    '''
    from itertools import count
    counter = count(start=3)
    print(next(counter))
    print(next(counter))
    print(next(counter))

def test_cycle_iter():
    '''
    从一个有限序列中生成无限序列
    :return:
    '''
    from itertools import cycle
    colors = cycle(['red', 'white', 'blue'])
    print(next(colors))
    print(next(colors))
    print(next(colors))

fib = Fib(10)
print(next(fib))
for x in fib:
    print(x)
print("xxxxxxxxxxxxxxxxxxxxxxxx")
test_endless_iter()

print("xxxxxxxxxxxxxxxxxxxxxxxx")
test_cycle_iter()
