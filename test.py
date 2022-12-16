
a = input("dwewee:")

print(a)

def fun_test(a, **kwargs):
    '''

    :param a:
    :return:
    '''
    key = kwargs.get('key',0)
    print(key)
add = lambda a,b:a+b

if __name__ == "__main__":
    print(add(1,2))
    fun_test(4,key = 5)
