import time
from functools import wraps


def dec_fun(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        '''
        装饰器内部函数
        :param args:
        :param kwargs:
        :return:
        '''
        begin_time = time.time()

        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"运行时间：{end_time - begin_time}s")
        return res

    return wrap_func


@dec_fun
def test(a, b):
    '''
    test
    :param a:
    :param b:
    :return:
    '''
    time.sleep(1)
    return a + b


res = test(3, 5)
print(res)
print(test.__doc__)



