from collections import OrderedDict
d = OrderedDict(a=11, b=2, c=3)
print(d) #会排序
s = sorted(d.items())
print(s)