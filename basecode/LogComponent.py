from functools import wraps

def fun_fillter(func):
    '''

    :param func:
    :return:
    '''
    @wraps(func)
    def wrap_func(*arg,**kwargs):
        '''
        日志组件
        :param arg:
        :param kwargs:
        :return:
        '''
        write_file("函数运行前")
        res = func(*arg,**kwargs)
        write_file("函数运行后")
        return res
    return wrap_func

LogFilePath = "log/log20221130.txt"

def write_file(msg):
    with open(LogFilePath,"a+",encoding='utf-8') as fp:
        fp.write(msg+'\n')

def read_file(path):
    with open(path,"r",encoding='utf-8') as fp:
        return fp.readlines()

@fun_fillter
def test(x,y):
    return x+y

print(test(4,7))

txt = read_file(LogFilePath)
for elem in txt:
    print(elem)
