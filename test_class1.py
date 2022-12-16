
class Student(object):
    def __init__(self,name,age,addr):
        '''
        构造函数
        :param name:
        :param age:
        :param addr:
        '''
        print(f"构造函数 Student")
        self.__name = name
        self.__age = age
        self.__addr = addr

    def __del__(self):
        print(f"析构函数 Student")

    def study(self):
        print(f"{self.__name} studing")

stu = Student("jack",18,"shanghai")
stu.study()