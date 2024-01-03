##  运算符和表达式 

### 1 赋值语句  

> 上节变量赋值可知，赋值语句主要用于实现给变量分配对象过程 

 python中常见赋值语句如下表：  

| 运算                | 解释                          |
| ------------------- | ----------------------------- |
| a=100               | 基本形式                      |
| a,b = 100,200       | 元组赋值                      |
| [a, b] = [100, 200] | 列表赋值（位置性）            |
| a,b,c = 'ABC'       | 序列赋值(通用性)              |
| a,b = [10,20]       | 序列赋值(通用性)              |
| a,*b = 'hello'      | 扩展的序列解包(python3中特有) |
| a = b = c = 10      | 多目标赋值                    |
| a += 1              | 增强赋值                      |

### 2 关系运算 

 关系运算就是比较运算，如果表达式成立，返回True，否则返回False。关系运算的结果是布尔值 。

| 运算符 | 示例   | 说明                                        |
| ------ | ------ | ------------------------------------------- |
| ==     | a == b | a和b相等，结果是True，a和b不相等结果为False |
| !=     | a != b | a不等于b 结果为True，否则结果为True         |
| \>     | a > b  | a大于b结果为True，否则为False               |
| \>=    | a >= b | a大于等于b结果为True，否则为False           |
| <      | a < b  | a小于b结果为True，否则为False               |
| <=     | a <= b | a小于等于b结果为True，否则为False           |

 **注意：** 

-  优先级： 比较运算符优先级相同
- 从左向右算
- 可以这样算：1 < a < 3 等价于 a > 1 and a < 3 

###  3 逻辑运算

逻辑运算符可以用于构造复杂条件。逻辑运算符包括：

- 逻辑与 and 对应汉语的意思是“并且” 、 “同时”
- 逻辑或 or 对应汉语意思为"或者"
- 逻辑非 not 对应汉语意思为”相反“

在逻辑运算中，False、None、0、0.0、‘’（空字符串）被看做假（False），其它的看做真(True) 

#### 3.1 逻辑与 

| a     | b     | a and b |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

 小结：真真为真，有假为假

逻辑与表达式的值：a and b，如果a为假,则结果是a的值，否则结果是b的值 

#### 3.2 逻辑或 

| a     | b     | a or b |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

小结：有真为真，假假为假

逻辑或表达式的值： a or b，如果a为真，则结果为a的值，否则结果是b的值 

#### 3.3 逻辑非 

| True  | False |
| ----- | ----- |
| True  | False |
| False | True  |

 小结：真则为假，假则为真

逻辑非表达式的值：!a ，如果a为真，则结果为假，否则结果为真 

#### 3.4 短路计算 

- 对于逻辑与表达式 a and b，如果a为假，则不计算b
- 对于逻辑或表达式 a or b ，如果a为真，则不计算b 

#### 3.5 注意事项 

-  优先级 not > and >or 

### 4 身份运算符 

is: 判断两个标识符是否引用自同一个实体【对象】，比较的是两个对象的id是否一样，如果相同为真，否则为假

is not：判断两个标识符是不是引用自不同的实体【对象】如果两个对象的id不同结果为真，否则为假

id()函数获取实体的id（地址）

注意:is和==的区别

is用于判断两个变量引用实体是否为同一个【id】

==用于判断两个变量的值是否相同，但id不一定相同 

### 5 成员运算符  

主要应用在列表中

in:如果在指定的列表中找到指定的值，则返回True，否则返回False

not in:如果在指定的列表中未找到指定的值，则返回True，否则返回False 

### 6 位运算符(难点，不是重点) 

#### 6.1 内存 

内存是存储数据地方，内存按字节存储二进制数据，字节是内存分配的最小单位，每一个字节存储8位二进制数据。 位是最小的数据单位，1位可以保存一个二进制数据0或1  

位 bit ---b

字节 Byte ----B

1B = 8b

1k = 1024B

1M = 1024k

1G = 1024M 

#### 6.2 二进制 

-  进制就是进制位，一种进位方法，例如:十进制逢十进一，二进制逢二进一。。。【八进制和十六进制是通过二 进制演变的】 
-  每种进制都有自己的符号集：  
  -  十进制（0,1,2,3,4,5,6,7,8,9）  
  -  二进制（0,1） 
  -  八进制（0,1,2,3,4,5,6,7） 
  -  十六进制（0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f） 

- 二进制的计算【逢二进一】 

  ```
  0 + 0 = 0
  0 + 1 = 1
  1 + 1 = 10
  11 + 1 = 100
  101110
  011101
  --------
  1001011
  ```

-  进制转 

  ```
  十进制： 123 基数是10，权重：3的权重（10的零次方） 2的权重（10的1次方） 1的权重（10的平方）
  123 = 1*10（2） + 2*10（1） + 3 * 10（0） 括号里表示10的次方
  二进制： 101 基数是2 权重 1的权重（2的0次方） 0的权重（2的1次方） 1的权重（2的2次方）
  101（B） =>十进制： 1*2（2） + 0*2（1） + 1*2（0） = 5
  二进制 =》十进制 ： 把二进制按照权展开，相加就可以得到对应的十进制
  十进制 =》二进制：
  对于整数，对十进制数进行除2运算，直到商为0为止，然后将各个步骤得出的余数倒着写出来
  对于小数：整数部分同上，对于小数，乘以2取整，直到结果为0
  11.625 =>1011.101
  二进制 =》八进制 ： 从右向左进行分组，每三位为一组，不足时需要进行补0操作
  1001 0110 -----》010 010 110-----》2 2 6------>0o226
  1010001------》001 010 001-------》121-----》0o121
  二进制 =》十六进制 ： 从右向左进行分组，每四位为一组，不足时需要进行补0操作
  1001 0110------》9 6-----》0x96
  1011 1110------》11 14-----》b e------》0xbe
  11 1011 ------》0011 1011------》3 11----》0x3b
  ```

-  原码、反码和补码 

  ```
  【原码】：将最高位设为符号位（0表示正数，1表示负数），其余位数存储数值大小，称为数字的原码。
  1 ----》0000 0001
  -1----》1000 0001
  +-----------------------------
  1000 0010 -2
  结论：原码不能正确运算，所以计算机不是以原码存储数据
  ```

   【反码】正数的反码就是原码，负数的反码是原码符号位不变，其他位按位取反(1变0，0变1) 1----》0000 0001 -1----》1111 1110 +---------------------------- 1111 1111 -0 结论：计算不以反码为存储方式 【补码】正数的原码反 码补码相同，负数的补码是反码加1 1----》0000 0001  -1----》1111 1111 +----------------------- 0000 0000 0 结论：计算机采用补码存储数据 

####  6.3 位运算 

 是通过整数的二进制位进行计算的，只有整数可以进行位运算  

| 运算符     | 说明     | 说明             |
| ---------- | -------- | ---------------- |
| &          | 按位与   | 全1为1，有0为0   |
| \|         | 按位或   | 有1为1，全0为0   |
| ^          | 按位异或 | 相同为0，不同为1 |
| ~          | 按位取反 | 1变0,0变1        |
| <<(左移)   | 按位左移 |                  |
| \>>(右移） | 按位右移 |                  |

### 7 运算符的优先级 

- 尽量不要把一个表达式写的过于复杂，如果遇到复杂的需求，则最好分步运算
- 不要过多的依赖于运算符的优先级，否则代码的可读性太差，在实际的项目开发中，一般采用（）将优先级高 的运算括起来  

### 8 数据类型的转换 

  python是一种强类型语言：要求运算符两边的操作数必须是同一个类型的，否则必须转换  

| 函数名         | 函数值                                                       |
| -------------- | ------------------------------------------------------------ |
| int(x,[基 数]) | 将数字或字符串转换为整数，如果x为浮点数，则自动截断小数部分  |
| float(x)       | 将x转换成浮点型                                              |
| str(x)         | 将x转换成字符串                                              |
| bool(x)        | 转换成bool类型 的True或 Fals                                 |
| repr(x)        | 返回一个对象的String格式                                     |
| eval(str)      | 执行一个字符串表达式，返回计算的结果                         |
| tuple(seq)     | 参数可以是元组、列表或者字典，为字典时，返回字典的key组成的集合 |
| list(s)        | 将序列转变成一个列表，参数可为元组、字典、列表，为字典时，返回字典的key组成的集合 |
| set(s)         | 将一个可以迭代对象转变为可变集合，并且去重复，返回结果可以用来计算差集x - y、并集x |
| chr(x)         | 输入一个ASCII码（0-255），返回一个对应的字符。返回值是当前整数对应的ascii字符。 |
| ord(x)         | 返回一个字符所对应的码值                                     |

 数值类型 ： int、float、bool 

 bool -> int -> float  

 **通过eval()函数来求值** 

 我们可以通过eval函数将字符串转换为python可以识别的表达式。 

 eg:  

```python
x = 10
y = 20
formula = 'x*y+10-(x-y)'
result = eval(formula)
print(result)
```

### 9 Python math库常用函数 

 math库常用函数  

 使用math库前，用import导入该库 

```python
import math
```

 取大于等于x的最小的整数值，如果x是一个整数，则返回x 

```
>>> math.ceil(5.12)
6
```

 floor()取小于等于x的最大的整数值，如果x是一个整数，则返回自身 

```
>>> math.floor(4.999)
4
```

 求x的余弦，x必须是弧度 

```
>>> math.cos(math.pi/4)
0.7071067811865476
```

 把x从弧度转换成角度 

```
>>> math.degrees(math.pi/4)
45.0
```

 fabs()返回x的绝对值 

```
>>> math.fabs(-0.5)
0.5
```

 factorial()取x的阶乘的值 

```
>>> math.factorial(3)
6
```

 对迭代器里的每个元素进行求和操作 

```
>>> math.fsum((1,2,3,4))
10.0
```

 返回x和y的最大公约数  

```
>>> math.gcd(8,6)
2
```

 得到(x2+y2),平方的值  

```
>>> math.hypot(3,4)
5.0
```

 pow()返回x的y次方，即x**y 

```
>>> math.pow(3,4)
81.0
```

 sqrt()求x的平方根 

```
>>> math.sqrt(100)
10.0
```

 **案例分析：** 

 接受一个正整数输入x，打印下述公式的输出值。  

 ![img](\img\企业微信截图_16698745583750.png) 

 输入格式: 

共一行，为一个正整数。

输出格式：

共一行，采用round函数保留10位小数 。

```python
from math import *
x=int(input('请输入正整数样例：'))
y=sin(15/180*pi)+(e**x-5*x)/sqrt(x**2+1)-log(3*x)
print('%.10f'%y)
```



## 函数 

### 1 函数定义 

> 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。 函数能提高应用的模块性，和代码的重复利用率。Python提供了许多内建函数，比如print()。也可以自己创建 函数，这被叫做用户自定义函数。 

 函数就是完成特定功能的代码块，本质上是对代码的封装。 语法格式 

```python
def 函数名（[参数1],[参数2]....[参数n]）:
函数体
```

-  函数名命名规则同变量名，要满足标识符命名规则 

- 函数定义分两部分函数头和函数体

-  函数体，就是实现功能的代码段，以：开头，必须缩进 函数名的命名风格：一般建议 用下划线分隔的小写单词组成：say_hello

-  一次编码，到处运行 

  

#### 函数的优点

- 代码可复用
- 代码可维护性高
- 容易排错
- 可读性好
- 利于团队开发

### 2 函数参数 

#### 2.1 实参和形参  

- 形参：就是函数定义时小括号里的变量
- 实参：函数调用的时候，小括号里的表达式
- 函数可以没有形参和实参 

#### 2.2 参数分类 

-  位置参数，要求实参顺序必须和形参顺序完全一致，由形参顺序决定实参顺序 

  ```python
  def say_hello(name,age,home):
  print('大家好，我是{},我今年{}岁了，我来自{}'.format(name,age,home))
  say_hello('王二妮',18,'湖北武汉') #实参个数、顺序必须和形参一致
  ```

- 关键字参数，函数调用时，实参可以是键值对，键就是形参名字，这样的调用，实参不必关心形参的顺序。 

  ```python
  def say_hello(name,age,home):
  print('大家好，我是{},我今年{}岁了，我来自{}'.format(name,age,home))
  say_hello(name='王二傻',home='大连',age=20) #三个关键字参数
  say_hello('大傻',home='美国',age=30) #两个关键字参数
  sya_hello('二傻',24,home='何方') #一个关键字参数
  ```

-  默认值，如果形参在定义的时候给定一个值，那么函数在调用时就可以不传实参，可以简化调用 

  -  默认值参数必须放到最右边
  - 如果传了实参，那么实参优先，不会使用默认值
  - 默认值只计算一次
  - 默认值必须是不可变对象 

  ```python
  def my_power(x,n=2):
  return (x) ** n
  my_power(3)
  my_power(4,0.5)
  def test(a=[]):
  a.append('end')
  print(a)
  test([1,2,3])
  test() #['end']
  test() #['end','end']
  ```

   **函数参数传递技巧：** 

   （1）一般来说，函数传递参数个数在5个以内，则可以考虑采用传递固定参数方式

   （2）如果传递的参数是一个整体信息，怎么办？类 ---- 可以考虑传递类的实例对象 

   **问题？** 

   如果函数要传递的参数个数很多怎么办，比如每次传递个数不定，如何是好？  

-  可变参数，传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。 

  ```python
  #使用*接收任意数量的位置参数
  #注意：*的不定长参数被当做元组处理
  def demo(a,b,*args):
  print(a,b,args)
  demo(12,33,90)
  demo(1,2,3,4,5)
  #使用**接收任意数量的关键字参数
  #注意:**的不定长参数被当做字典处理
  def demo1(a,**args):
  print(a,args)
  demo1(1,name='kk',age=3)
  ```

  

#### 2.3 参数组合  

 形参顺序须按照以下顺序：位置参数、默认值参数、*argt,**argkw 

### 3 函数调用  

-  函数调用必须在函数定义之后

- 函数调用必须能够正确传递实参  

  ```python
  def demo(a,b,c=0,*arg1,**arg2):
  print(a,b,c,arg1,arg2)
  demo(1,3,k=4)
  demo(1,2,3,4,5)
  demo(1,b=3,c=3,d=5)
  demo(*(1,2,3),**{'name':12}) #任何函数都可通过这种形式传递参数
  ```

  

### 4 返回值 

可以通过return语句返回计算结果。语法： return 表达式

- return的作用一个是终止函数的执行，所有执行了return后，其后的语句不会被执行

- 如果没有return语句，则默认返回的是None

- return还可以返回给调用者数值

- return可以返回一个值，如果要返回多个值，那么返回的是一个元组 

  ```python
  def demo2():
  return 1
  def demo3():
  return 1,2,3
  print(demo2())
  print(demo3()) #(1,2,3)
  ```

判断一个函数返回值 

```python
#判断是否能被2整除 传入函数
def even(n):
return n % 2 == 0
#能被3整除 传入函数
def divid_by3(n):
return n % 3 == 0
```



### 5 文档字符串 

 函数文档字符串documentation string （docstring）是在函数开头，用来解释其接口的字符串。简而言之：帮助文 档

- 包含函数的基础信息
- 包含函数的功能简介
- 包含每个形参的类型，使用等信息

文档字符串书写规则：

- 必须在函数的首行

- 使用三引号注解的多行字符串(''' ''') 或(""" """) 

- 函数文档的第一行一般概述函数的主要功能，第二行空，第三行详细描述。 

  ```python
  def test():
  '''
  函数名：test
  功能：测试
  参数：无
  返回值：无
  '''
  print("函数输出成功")
  #使用__doc__属性查看文档字符串
  print(test.__doc__)
  ```

  

### 6 参数传递  

 python的参数传递是简单的值传递，当然这里的值是指变量的引用（地址），不是变量的值。不存在值传递和引用 传递的区分。简而言之，python的参数传递可以称之为对象引用传递，对象可以分为：

- 不可变对象：int、float、None、complex、bool、tuple、str
- 可变对象: dict、list 

### 7 空函数 

 借助于pass语句实现，函数体不完成任何功能，只有一个pass语句 

```python
def test():
pass
```



### 8 匿名函数 

不再使用def 函数名()这种形式定义函数，而是使用lambda来创建匿名函数

特点：

- lambda只是一个表达式，函数体比def简单的多
- lambda的函数体不再是代码块
- lambda只有一行，增加运行效率

语法： 

```python
lambda [arg1,arg2....argn]:函数体
add = lambda a,b:a + b
print(add(3,5))
```



### 9 函数类型 

 函数也是一种类型，我们自定义的函数就是函数对象，函数名保存了函数对象的引用（地址）  

```python
def test():
print('我是测试函数')
print(test) #函数名是变量，指向了函数对象
pf = test #pf变量也指向了函数对象，所以也可以通过pf调用test函数
pf()
```



### 10 传入函数 

 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数，也可以称之为传入函数。可以实现通用编 程，排序等复杂功能  

```python
#通用求和函数
def sum1(n, callback):
'''
功能：求满足callback规定条件的数的和
:param n: 大于0的整数
:param callback: 用于判断一个数是否满足指定条件，由调用者传入,有一个参数，形如：def callback(n)
:return: 求和的结果
'''
sum = 0
for i in range(1,n+1):
if callback(i):
sum += i
return sum
print(sum1(100,lambda x:x%2==0))
print(sum1(100,lambda x:x%7==0))
print(sum1(100,lambda x:x%15==0 and x % 7 != 0))
```



### 偏函数  

 当一个函数有大量参数，调用的时候非常不方便，可以使用偏函数技术，将一些参数固定（给默认值），达到简化函 数调用的目的。 

```python
# -*- coding: utf-8 -*-
__author__ = 'sunnychou'
__date__ = '2019/5/12 9:54'
import functools
def test(a,b,c,d):
print(a, b, c, d)
#从前面固定参数，使用位置参数就行，1=>a，2=>b
test1 = functools.partial(test,1,2)
test1(3,4) #3=>c 4=>d
#从后面固定参数，需要使用关键字参数
test2 = functools.partial(test,c=3,d=4)
test2(1,2) #1=>a 2=>b
#如果固定的参数不连续，则需使用关键字参数固定
test3 = functools.partial(test,b=2,d=4)
test3(a=1,c=3) #需要使用关键字参数，否则会报错
```



###  常用的高阶函数

 如果一个函数的参数是另外一个函数，那么这个函数就可以称为高阶函数 

####  **1 map** 

 map是系统内置函数，map函数接收两个参数，一个是函数，一个是可迭代对象(Iterable)，map将传入的函数依次 作用到序列的每个元素，并把结果作为新的Iterator返回。 

```python
"""
map(function,iterable)
参数1：function，函数,函数的参数个数取决于后面序列的个数
参数2：iterable，一个序列或多个序列
功能：将传入的函数依次作用于序列中的每一个元素，并把结果作为新的Iterator返回
"""
#1.传入函数一个参数
def fun(x):
return x ** 2
#需求：获取一个列表中每个元素的平方，生成一个新的列表
l1 = map(fun,[1,2,3,4])
print(l1) #<map object at 0x000001E86D3DA6D8> #返回的是迭代器
print(list(l1)) #[1, 4, 9, 16] #将迭代器转换为迭代对象
#传入函数2个参数
l1 = [1,2,3,4]
l2 = [2,3,4,5,6,7]
def mul(x, y):
return x * y
#注意如果两个列表长度不一样，以短的为主计算，函数是平行取值，也就是说x取l1的值，y取l2的值
gen1 = map(mul,l1,l2) #可以使用lambda表达式
print(list(gen1)) #[2, 6, 12, 20]
#提取字典的键
gen3 = map(lambda x:int(x),{'1':10,'2':20})
print(list(gen3)) #[1,2]
#元组
gen4 = map(lambda x,y:(x,y),[1,2,3,4,5],[1,2,3])
print(list(gen4)) #[(1, 1), (2, 2), (3, 3)]
```

####  **2 reduce** 

 reduce()函数也是functools模块中的一个高阶函数。需要引入functools模块才能使用。 

```python
'''
functools.reduce(f, iterable[, initializer])
参数1：函数，这个函数需要两个参数。
参数2：可迭代对象
参数3：可选，是默认值
返回值：f函数计算的结果
'''
from functools import reduce
#1.累加求和
def add(x,y)
return x + y
print(reduce(f,[1,2,3,4,5],5)) #f = add
计算过程：
（1）a = f(1,2) #将1赋值给x，2赋值给y
（2）a = f(a,3) #a赋值给x，3赋值给y
（3）a = f(a,4)
(4）a = f(a,5)
(5）f(d,10) = 20
#将序列变成整数
print(reduce(lambda x,y:x*10+y,[9,0,7,8])) #9078
```

####  3 filter 

 filter是内建函数，可以对可迭代对象进行过滤，去除不满足条件的元素 

```python
filter(function, iterable)
参数： function 确定是否保留元素，为真保留，为假去除元素,function的值可以None
iterable 可迭代对象
返回值：一个新的迭代器或迭代对象
#1 过滤掉非字符串数据
print(filter(lambda x:isinstance(x,str),['1',8,'2',3,True,0.9]))
等价于:
[s for s in ['1',8,'2',3,True,0.9] if isinstance(s,str)]
#2 回文数
#回文数判断
def is_palindrome(n):
l1 = list(str(n)) #将数字转换为字符串，再将字符串转为列表
l2 = l1[::-1] #获取反向列表
if l1 == l2: #列表比较,长度相同，每一个元素都相同则为真
return True
return False
#找出1-1000内所有的回文数
print(list(filter(is_palindrome,range(1,1001))))

```

#### 4 sorted 

 sorted是内建函数，用于对有序序列进行排序，生成一个新序列 

```python
sorted(iterable[, key][, reverse])
参数：iterable 排序对象，可以列表、元组、字符串等有序序列
key 一个函数，作用于序列的每一个元素，根据函数返回值进行排序，
具体的函数的参数就是取自于可迭代对象中，
reverse 默认从小到大排序，如果reverse为True则从大到小排序
返回值： 新的序列
#字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) #指定把元素变为小写后再排序
#多维数据排序
l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
print(sorted(l,key=lambda x:x[1])) #使用元组的第二个元素排序
students = [{'name':'abc','gender':'男','age':23} ,
{'name': 'kkd', 'gender': '男', 'age': 19} ,
{'name': 'ccxsbc', 'gender': '男', 'age': 20}]
print(sorted(students,key=lambda elem:elem['age'])) #指定用age排序
```

## 装饰器 

> 装饰器(Decorators)是 Python 的一个重要部分。 
>
> python装饰器本质上就是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能， 装饰器的返回值也是一个函数对象（函数的指针）。  

Python中装饰器采用的是类似java语言中的AOP(面向切面编程)思想。是属于python语法糖规则。

装饰器函数的外部函数传入我要装饰的函数名字，返回经过修饰后函数的名字；内层函数（闭包）负责修饰被修饰函 数。 

### **装饰器本质** 

是一个函数

参数：是你要装饰的函数名（并非函数调用）

返回：是装饰完的函数名（也非函数调用）

作用：为已经存在的对象添加额外的功能

特点：不需要对对象做任何的代码上的变动 

### 装饰器(decorator)功能 

1. 引入日志 
2. 函数执行时间统计
3. 执行函数前预备处理
4. 执行函数后清理功能
5. 权限校验等场景
6. 缓存 

 首先看一个例子： 

```python
def hi(name="andy"):
	return "hi " + name

print(hi())
```

从函数中返回函数

其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

  

```python
def say_hello(name="andy"):
	def greet():
		return "now you are in the greet() function"
    
	def welcome():
		return "now you are in the welcome() function"
    
	if name == "dehua":
		return greet
	else:
		return welcome
    
a = say_hello()
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
```

再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？这 是因为当你把一对小括号放在后面，这个函数就会执行 

**提出问题**

我们直接采用返回函数本身就行了啊，为什么还要引入装饰器呢？

比如如下一段代码：  

```python
def decorate(func):
	print("before myfunc() called.")
	func()
	print(" after myfunc() called.")
	return func

@decorate
def myfunc():
	print(" myfunc() called.")
    
myfunc()
myfunc()
```

这是一个最简单的装饰器的例子，但是这里有一个问题，就是当我们两次调用myfunc()的时候，发现装饰器函数只被 调用了一次。为什么会这样呢？ 

要解释这个就要给出破解装饰器的关键钥匙了。 

**注意：** 

 这里@decorate这一句，和myfunc = decorate(myfunc)其实是完全等价的，只不过是换了一种写法而已  

**在Python中函数名是一个指向函数首地址的函数指针** 

 而decorate(myfunc)的返回值就是函数myfunc()的地址，两次调用，第一次被执行，第二次不会进入装饰内部函数 执行。 

 问题： 

 如何保证两次调用myfunc(), 装饰器都能被调用呢？  

 解决方案： 

 采用装饰器  

### 引入装饰器 

```python
'''示例2: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco(func):
	def _deco():
		print("before myfunc() called.")
		func()
		print(" after myfunc() called.")
    	# 不需要返回func，实际上应返回原函数的返回值
    return _deco
@deco
def myfunc():
	print(" myfunc() called.")
	return 'ok'

myfunc()
myfunc()
	#两次调用myfunc()的时候，发现装饰器函数只被调用了一次。为什么会这样呢？
# 要解释这个就要给出破解装饰器的关键钥匙了。
```

执行此代码，就会发现调用两次myfunc()， 装饰器都会进入，结果正确。 

**带参数装饰器** 

让装饰器带参数，和上一示例相比在外层多了一层包装 

```python
def deco(arg):
	print(f"1,outer, ######################")
	def _deco(func):
		print("2, inner,#######################")
		def __deco():
			print("before %s called [%s]." % (func.__name__, arg))
			func()
			print("after %s called [%s]." % (func.__name__, arg))
			return __deco
		return _deco
    
@deco("mymodule")
def myfunc():
	print(" myfunc() called.")
    
@deco("module2")
def myfunc2():
	print(" myfunc2() called.")
    
print("start....")
myfunc()
print("$$$$$$$$$$$$$$$$$")
myfunc2()
print("end....")
```

运行结果如下： 

```python
1,outer, ######################
2, inner,#######################
1,outer, ######################
2, inner,#######################
start....
before myfunc called [mymodule].
myfunc() called.
after myfunc called [mymodule].
$$$$$$$$$$$$$$$$$
before myfunc2 called [module2].
myfunc2() called.
after myfunc2 called [module2].
end....
```

 通过以上运行结果分析可知： 

1. 先执行装饰器外层和中间层逻辑。
2. 通过参数可以控制装饰器里面函数流程是否往下走
3. 装饰器可以在原有函数基础上加上特定逻辑。 

**案例分析：** 

 通过分析 小明和baby的爱情故事 的故事扩展部分功能，掌握装饰器用法 

### 装饰器-高级 

#### 装饰器模板

装饰器函数的外部函数传入我要装饰的函数名字，返回经过修饰后函数的名字；内层函数（闭包）负责修饰被修饰函 数。 

```python
from functools import wraps

def fn_wrapper(func): #外部函数
	print("##################")
    @wraps(func) #此处加上@wraps包裹被装饰函数，目的是为了让被装饰的函数文档对外可见
    def _wrapper(*args, **kwargs): #内部函数
        '''
        装饰器内部函数说明文档
        :param args:
        :param kwargs:
        :return:
        '''
        print(f"before {func.__name__} called, can add some functions.")
        res = func(*args, **kwargs) #在此处真正的被调用, 调用在这里！！！！！
        print(f"after {func.__name__} called., can also add some other functions.")
        return res
	return _wrapper
```

 以上就是一个标准的装饰器模板。（不带参数）  



#### 带参数装饰器 

为何要引入带参数装饰器？  

因为有时候我们想通过装饰器传入一些参数在外部来控制一些逻辑 

inspect模块 

此处要用到python中非常重要的一个库inspect模块，用于收集python对象的信息，可以获取类或函数的参数的信 息，源码，解析堆栈，对对象进行类型检查等等。 

提取函数签名python3 inspect.signature() 带参数的装饰器 

```python
from inspect import signature

import inspect

def func(a, b=0, *c, d, e=1, **f):
	pass

aa = inspect.signature(func)
print("inspect.signature（fn)是:%s" % aa)
print("inspect.signature（fn)的类型：%s" % (type(aa)))
print("\n")
```

 输出的结果是：  

```python
inspect.signature（fn)是:(a, b=0, *c, d, e=1, **f)
inspect.signature（fn)的类型：<class 'inspect.Signature'>
```

 此处对函数签名，能把函数的定义类型都给获取到  

 **案例分析** 

 如下是一个采用带参数装饰器实现一个对函数参数进行类型检查 

```python
from inspect import signature

def check_type(*ty_args, **ty_kwargs):
	def out_wrapper(func):
        # 通过signature方法，获取函数形参：name, age, height
        sig = signature(func)
        # 获得装饰器传来的参数， 函数签名与之绑定，字典类型
        bind_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        print(bind_types)
        def wrapper(*args, **kwargs):
            # 给执行函数中具体的实参进行和形参进行绑定，形成字典的形式
            func_type = sig.bind(*args, **kwargs).arguments.items()
            print(func_type)
            # 循环形参和实参字典的items()形式
            for name, obj in func_type:
            	if name in bind_types:
            		if not isinstance(obj, bind_types[name]):
            			raise TypeError('%s must be %s' % (name, bind_types[name]))
            func(*args, **kwargs)
         return wrapper
	return out_wrapper
# 通过装饰器实现对函数参数进行类型检查
@check_type(str, int, float)
def func(name, age, height):
	print(name, age, height)
    
    
if __name__ == '__main__':
	func('china', 100, 2.75)
```

 **案例分析：**  

（1）实现统计函数时间装饰器 

（2）带参数装饰器实现权限控制 

（3）采用带参数装饰器实现超时重试机制函数

（4）通过分析 小明和baby的爱情故事 的故事扩展部分功能，掌握装饰器用法 



## 文件操作 

> 文件的处理包括读文件和写文件，读写文件就是请求操作系统打开一个文件对象，然后，通过操作系统提供的 接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）  



### 1 文件读取 

 文件读取可分为以下步骤：  

-  打开文件
- 读取文件内容
- 关闭文件  

 打开文件要使用open内建函数： 

 open(file [, mode='r', encoding=None, errors=None])  

 参数说明： 

file：文件路径，可以是相对路径和绝对路径

mode：文件打开模式

encodeing: 文件编码方式，不用于二进制文件，一般是utf-8,gbk

errors：指定如何处理编码和解码错误 ，适用于文本文件

返回值：一个可迭代的文件对象  

| mode | 解释                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 只读                                                         |
| w    | 写之前会清空文件的内容                                       |
| a    | 追加的方式，在原本内容中继续写                               |
| r+   | 可读可写                                                     |
| w+   | 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模 式。如果该文件不存在，创建新文件用于读写。 |
| b    | rb、wb、ab、rb+、wb+、ab+意义和上面一样，用于二进制文件操作  |

注意：二进制文件一般用于视频、音频、图片

读取文件常用函数： 

| 函数             | 解释                                             |
| ---------------- | ------------------------------------------------ |
| read([size])     | 读取文件(读取size字节，默认读取全部              |
| readline([size]) | 读取一行,如果指定size，将读入指定的字符数        |
| readlines()      | 把文件内容按行全部读入，返回一个包含所有行的列表 |

```python
#打开文件
fp = open('qfile.txt','r',encoding='utf-8')
#读取文件全部内容
#content = fp.read()
#print(content)
#读取指定字符数,包括行尾的换行符\n
# print(fp.read(20))
#读取一行
# print(fp.readline(5)) #读取指定字符数
# print(fp.readline()) #读取一整行，直到碰到一个\n
#读取所有行，返回列表
# print(fp.readlines())
#关闭文件
fp.close()

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
# fp = open('qfile.txt','r',encoding='utf-8')
# print(fp.readlines())
# finally:
# fp.close()
#可以简写为：
#with语句会自动调用close方法关闭文件
with open('qfile.txt','r',encoding='utf-8') as fp:
	print(fp.readline())

#fread()和freadlines()会一次读入文件全部内容，如果文件太大，会直接耗尽内存的，因为文件对象可迭代，所以可以用for循环遍历文件读取
with open('qfile.txt','r',encoding='utf-8') as fp:
	for line in fp:
		print(line.strip()) #注意无论是read、readline、readlines都会读入行末的\n，所以需要手动剔除\n
```

### 读取大文件 

 比如给你一个10G大文件，如何读取？ 

 python文件对象提供了三个“读”方法： .read() 、 .readline() 和 .readlines() 。 

 .read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。然而 .read() 生成文件内容最直接的 字符串表示，但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理。  

 处理大文件是很容易想到的就是将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。这里用了 iter 和 yield （关于yield和iter是属于生成器的，后续章节会讲到） 

```python
def read_in_chunks(filePath, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
	file_object = open(filePath)
	while True:
		chunk_data = file_object.read(chunk_size)
		if not chunk_data:
			break
		yield chunk_data

def process(chunk):
    '''
    do some data with chunk.
    :param chunk:
    :return:
    '''
	pass

if __name__ == "__main__":
	filePath = './path/filename'
	for chunk in read_in_chunks(filePath):
		process(chunk)

```

 关于读取大文件，经常在面试过程中被问到，其实采用map-reduce原理来解决此类问题是最佳方案。 

 将大块文件数据分块读取，然后分发到不同的线程或者进程中处理，也就是map思想，采用分而治之的思想处理每块 数据，然后进行reduce结果合并最终结果数据。  

###  2 写文件 

```python
path = "file11.txt"

#IO流
#1.打开文件
f = open(path,"w",encoding="utf-8")
#2.写入内容，将内容写入到缓冲区
#不会自动换行，需要换行的话，需要在字符串末尾添加换行符
f.write("Whatever is worth doing is worth doing well该行很骄傲很关键\n")
#3.刷新缓冲区【加速数据的流动，保证缓冲区的流畅】
f.flush()
#4.关闭文件 关闭文件也会刷新缓冲区
f.close()

#简写方式：可以不用手动调用close
with open(path,"w",encoding="utf-8") as f1:
	f.write("Whatever is worth doing is worth doing well该行很骄傲很关键")

```

### 3 移动文件指针  

 文件是顺序向后读写的，如果想要移动文件指针，可以使用seek方法： 

 file_obj.seek(offset,whence=0)  

 功能：移动文件指针 

 参数：offset 是偏移量，正数表示从文件开头向文件末尾移动，负数相反。 

 whence ： 文件指针的位置，可选参数，值可以是 

 SEEK_SET or 0 表示文件开头位置，是默认值  

 SEEK_CUR or 1 表示当前位置 

 SEEK_END or 2 文件末尾位置 

 返回值：新的位置 

```python
#1.txt内容：hello world
with open('1.txt','r',encoding='utf-8') as fp:
	fp.seek(5) #移动到hello后的空格位置
	print(fp.read(3)) #wo
	fp.seek(0) #移动到开头
	print(fp.read(5)) #hello
	print(fp.tell()) #tell()显示当前指针位置
```

### 4 编码和解码  

字符串类型和字节类型转换过程

字符串类型转换为字节类型：编码，encode

字节类型转换为字符串类型：解码，decode  

```python
str = "今天是个好日子 today is a good day"
path = "file22.txt"

with open(path,"wb") as f:
	result = str.encode("utf-8")
	print(result)
	f.write(result)
    
with open(path,"rb") as f1:
	data = f1.read()
	print(data)
	print(type(data))
    
	newData = data.decode("utf-8")
	print(newData)
	print(type(newData))

```

### 5 os模块 

 需要引入os模块  

| 函数名                             | 函数值                                                    |
| ---------------------------------- | --------------------------------------------------------- |
| os.name                            | 获取当前的操作系统的类型nt->windows posix->unix 后者Linux |
| os.environ[ɪn'vaɪərən]             | 获取操作系统中的环境变量                                  |
| os.environ.get("path")[ɪn'vaɪərən] | 获取path的环境变量                                        |
| os.curdir                          | 获取当前的目录                                            |
| os.getcwd()                        | 获取当前的工作目录                                        |
| os.listdir()                       | 以列表的形式 返回当前目录的文件                           |
| os.mkdir()                         | 创建目录                                                  |
| os.rmdir()                         | 删除目录                                                  |
| os.rename(old,new)                 | 修改文件后者文件夹的名字                                  |
| os.remove()                        | 删除文件                                                  |
| os.system(command)                 | 执行系统命令                                              |
| os.path.join(path1,path2)          | 将path1和path2拼接成一个正常的路径                        |
| os.path.splitext()                 | 获取文件扩展名                                            |
| os.path.isdir()                    | 判断是否是目录                                            |
| os.path.isfile()                   | 判断是否是文件                                            |
| os.path.exists()                   | 判断文件或者目录是否存在                                  |
| os.path.getsize()                  | 获取文件的大小(字节)                                      |
| os.path.dirname()                  | 获取路径的目录名                                          |
| os.path.basename()                 | 获取路径的文件名                                          |
| os.path.abspath()                  | 返回文件的绝对路径                                        |
| os.path.split()                    | 拆分路径                                                  |



##  面向对象编程 

### 1 面向对象的思想 

面向过程：面向处理，更多的是从计算机角度思考，注重计算每一个步骤，程序更像是一本cpu操作手册。 面向对象：以日常生活的角度思考问题的解决，更接近人的思维方式，让人可以从更高的层面考虑系统的构建 以你请朋友吃饭  

| 面向过程     | 面向对象         |
| ------------ | ---------------- |
| 自己买菜     | 和朋友一块到饭店 |
| 自己摘菜     | 叫服务员点菜     |
| 自己洗菜     | 和朋友一块吃     |
| 自己做菜     |                  |
| 和朋友一块吃 |                  |

面向对象的优点： 

-  面向对象更加适合做应用的开发 --- 面向实体性编程为主，造飞机，造轮船 
-  面向对象可以使你的代码更加优雅和紧凑 
-  面向对象开发效率更高 ---- 将功能和数据进行隔离 
-  面向对象代码复用度更高、可维护性更好 

面向对象是一种思维方式，它认为万事万物皆对象，程序是由多个对象协作共同完成功能的，所以以后我们要从面向 过程转向面向对象。以面向对象的方式考虑程序的构建。面向对象的核心是：**类和对象** 



### 2 类和对象 

#### 2.1 类和对象的概念 

> 类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在。一个类可以找到多个对 象。  
>
>  对象是类的行为属性和数据属性进行具体化后的实例。 

生活角度 

-  类：具有相同特征和行为的对象的集合，是一个概念  
-  对象：客观存在的一切事物，是类的实例 

 类： 汽车 超级英雄 电脑 杯子 

 对象： 红色的宝马 美国队长 桌上的mac pro 老王的黑色杯子 

 **类就相当于制造飞机时的图纸，用它来进行创建的飞机就相当于对象**  

 程序角度 

-  类：用户自定义的数据类型，是模板，**不占用内存** 
-  对象：由类定义的变量，占用内存 

类： 成员属性（成员变量） 描述对象的静态特征，诸如，名字、身高体重 成员方法 描述对象的动态特征，例 如：吃饭、睡觉、打豆豆  

**类和对象之间的关系** 

![](\img\企业微信截图_16702184415837.png)

 总之，类就是创建对象的模板 

#### 2.2 类的构成 

类(Class) 由3个部分构成  

-  类的名称:类名 
-  类的属性:一组数据 
-  类的方法:允许对进行操作的方法 (行为) 

**举例：** 

1）人类设计,只关心3样东西:  

-  事物名称(类名):人(Person) 
-  属性:身高(height)、年龄(age) 
-  属性:身高(height)、年龄(age) 

2）狗类的设计 

-  类名:狗(Dog) 
-  属性:品种 、毛色、性别、名字、 腿儿的数量  
-  方法(行为/功能):叫 、跑、咬人、吃、摇尾巴  

![](\img\企业微信截图_16702186187319.png)

#### 2.3 类的定义 

```python
#语法：
class 类名:
类体
```

 注意： 

- 类定义必须以关键字class
- 类名要符合标识符的规范
- 类名一般用大驼峰风格： 每个单词首字母大写，其它小写 ，例如MyBook YouMoney
- 类体必须缩进 在python3中类默认继承object，所以可以这样写 class Dog:，它等价于class Dog(object):
- 一个文件里只放一个类  

(1) 定义一个Car类  

```python
# 定义类
class Car: #经典定义类，如果是Car(object)则为新式类
# 方法
def getCarInfo(self):
print(f'车轮子个数:{self.wheelNum}, 颜色:{self.color}')
def move(self):
print("车正在移动...")
```

 **说明：** 

- 定义类时有2种：新式类和经典类，上面的Car为经典类，如果是Car(object)则为新式类
- 类名 的命名规则按照"大驼峰 

 (2) 成员方法 

成员方法其实就是函数，作用域在类内，成员方法的第一个参数必须是self，self代表当前对象，也就是调用这个方 法的对象，这个参数有系统传递。 

```python
class Dog(object):
	def bark(self): #成员方法，第一个参数必须是self，代表当前调用对象
		print('我是小可爱--丁丁')
        
dingding = Dog() #实例化一个对象

#调用方法,不需要传参数，self是系统传递的
#调用形式： 对象.方法（[实参]）
dingding.bark() #等价调用形式：bark(dingding)
```

 注意：  

-  self参数在调用的时候不必传值，由系统传值 
-  self只能在实例方法中使用 
-  方法和函数的区别： 
  -  方法作用域属于类，所以即便和普通函数重名，也不会被覆盖 
  -  方法的第一个参数必须是self，但函数不要求 
  -  方法必须通过对象调用，而函数不需要 

- 方法的第一个参数self其实可以使任何合法标识符，不过一般约定俗成都是self 

####  2.4 创建对象 

 上节2.3中定义了一个Car类；就好比有车一个张图纸，那么接下来就应该把图纸交给生成工人们去生成了。 python中，可以根据已经定义的类去创建出一个个对象。 

创建对象的格式为: 

```
对象名 = 类名()
```

创建对象: 

```python
# 定义类
class Car:
    # 移动
    def move(self):
		print('车在奔跑...')
    # 鸣笛
    def toot(self):
    	print("车在鸣笛...嘟嘟..")
        
# 创建一个对象，并用变量BMW来保存它的引用
BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = 4 #轮子数量
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
```

 说明： 

-  BMW = Car()，这样就产生了一个Car的实例对象，此时也可以通过实例对象BMW来访问属性或者方法 
-  第一次使用BMW.color = '黑色'表示给BMW这个对象添加属性，如果后面再次出现BMW.color = xxx表示对属性 进行修改  
-  BMW是一个对象，它拥有属性（数据）和方法（函数） 

![](\img\企业微信截图_16702193935658.png)

 另外说明：  

```python
#语法： 对象 = 类名（[实参]）
dingding = Dog() #实例化一个对象
print(dingding) #<__main__.Dog object at 0x00000000023F40B8>
print(type(dingding)) #<class '__main__.Dog'>

#查看对象的类名
print(dingding.__class__)
```



#### 2.5 成员属性  

成员属性描述的是对象的静态特征，比如说狗名字、品种等，其实就是一个变量，作用域属于类，不会和类外的全局 变量冲突。python中成员属性可以动态添加，也可以在构造函数中添加。成员属性属于对象，每个对象的成员属性 都不同  

-  给对象动态添加的属性只属于这个对象，其它对象没有该属性
- 使用__ slots__限制属性的动态绑定： 
- 在构造函数中添加的属性属于所有对象（重点） 

 **理解self** 

-  所谓的self，可以理解为自己
- 可以把self当做C++中类里面的this指针一样理解，就是对象自身的意思
- 某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面 的参数即可 

**python中 slots 作用？** 

当一个类需要创建大量实例时，可以通过 __slots__ 声明实例所需要的属性，如果超过了此属性范围进行对象属性 赋值，就会限制，起到保护数据作用。  

例如，

```python
class Foo(object): 
	__slots__ = ['foo'] 
```

 这样做带来以下优点：

	 1. 更快的属性访问速度 
  	 2. 通过取消 __dict__ 的使用减少内存消耗 
        	 3. 保护数据安全性 

Python内置的字典本质是一个哈希表，它是一种用空间换时间的数据结构。**为了解决冲突的问题，当字典使用量超 过2/3时，Python会根据情况进行2-4倍的扩容。由此可预见，取消 dict 的使用可以大幅减少实例的空间消 耗。**

```python
#添加属性语法：
对象.成员属性 = 值
#引用方式：对象.成员属性
class Dog(object):
	__slots__ = ('gender','name','age','kind') #这个类的对象这能有这些属性，同时也限制了采用		__dict__属性可以用来查看实例属性
    
	def __init__(self,name,kind,age):
		self.name = name
		self.kind = kind
		self.age = age
        
	def bark(tmp):
		print('我是小可爱--丁丁')
        
dingding = Dog('丁丁','泰迪',3)
print('我是可爱的%s犬，%s,我今年%d岁了' % (dingding.kind, dingding.name, dingding.age))
dingding.gender = '公' #动态添加的属性
#dingding.weight = 8 #不能添加这个属性，语法错误

#查看实例属性
print(dingding.__dict__) #__dict__属性可以用来查看实例属性
print(dir(dingding)) #查看Dog的属性，包括实例属性
```

 说明： 

 python中类如何来保护成员属性和成员方法呢？ 

 采用self.__xxx方式来定义类的成员。（两个下划线, 见 保护对象的属性） 



#### 2.6 构造和析构 

#####  （1） 构造方法 

-  目的：构造方法用于初始化对象，可以在构造方法中添加成员属性 
-  时机：实例化对象的时候自动调用  
-  参数：第一个参数必须是self，其它参数根据需要自己定义 
-  返回值：不返回值，或者说返回None，不应该返回任何其他值 

```python
语法：
	def __init__(self,arg1,arg2....):
		函数体
#参数：arg1,agr2...根据需要自己定义
#如果自己不定义构造方法，系统自动生成一个构造函数
def __init__(self):
	pass
```

 注意： 

-  如果没有定义构造方法，系统会生成一个无参构造方法，如果自己定义了构造方法，则系统不会自动生成 

```python
class 类名:
	def __init__(self):
		pass
```

-  一个类只能有一个构造方法，如果定义多个，后面的会覆盖前面的 
-  构造函数由系统在实例化对象时自动调用，不要自己调用 

```python
class Dog(object):
	def __init__(self,name,kind,age):
        self.name = name #定义对象属性，这个类所有的对象都具有该属性
        self.kind = kind #成员属性必须通过self.引用，否则是普通变量
        self.age = age
        
	def bark(tmp):
		print('我是小可爱--丁丁')
        
dingding = Dog('丁丁','泰迪',3)
print('我是可爱的%s犬，%s,我今年%d岁了' % (dingding.kind, dingding.name, dingding.age))
```



##### （2） 析构方法 

-  目的：对象销毁时，释放资源  
-  时机：对象销毁时由系统自动调用 
-  参数：除了self外，没有其他参数  
-  返回值：不返回值，或者说返回None。 
-  语法： 

```python
def __del__(self):
	#to do
```

 案例 

```python
class Dog(object):
    #构造
    def __init__(self,name,kind,age):
        self.name = name
        self.kind = kind
        self.age = age
        
    #析构
    def __del__(self):
		print('拜拜了，二十年后又是一条好汉')
        
    def bark(tmp):
    	print('我是小可爱--丁丁')
        
dingding = Dog('丁丁','泰迪',3)
print('我是可爱的%s犬，%s,我今年%d岁了' % (dingding.kind, dingding.name, dingding.age))
del dingding #销毁对象,自动调用析构方法
```

 当删除一个对象时，python解释器也会默认调用一个方法，这个方法为 __del__() 方法 



### 3 保护对象的属性 

 如果有一个对象，当需要对其进行修改属性时，有2种方法 

-  对象名.属性名 = 数据 ---->直接修改 
-  对象名.方法名() ---->间接修改  

 为了更好的保存属性安全，即不能随意修改，一般的处理方式为 

-  将属性定义为私有属性 
-  添加一个可以调用的方法，供调用 

```python
class People(object):
    def __init__(self, name):
    	self.__name = name
        
    def getName(self):
    	return self.__name
    
    def setName(self, newName):
        if len(newName) >= 5:
        	self.__name = newName
        else:
        	print("error:名字长度需要大于或者等于5")
            
xiaoming = People("dongGe")
print(xiaoming.__name)
```

 此时就会出现错误。 

```python
class People(object):
    name = 'Tom' #公有的类属性
    __age = 12 #私有的类属性
    
p = People()

print(p.name) #正确
print(People.name) #正确
print(p.__age) #错误，不能在类外通过实例对象访问私有的类属性
print(People.__age) #错误，不能在类外通过类对象访问私有的类属性

```



### 4 @property装饰器 

> Python中有一个被称为属性函数(property)的小概念，它可以做一些有用的事情。 
>
> -  将类方法转换为只读属性  
> -  重新实现一个类的属性的setter和getter方法 

 Python内置的@property装饰器就是负责把一个方法变成属性调用的，特别在对属性数据进行校验的时候。  

```python

class Student(object):
    @property
    def score(self):
    	return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
        	raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
        	raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    @score.deleter
    def score(self):
        if not hasattr(self, '_score'):
        	raise AttributeError('Student object has no attribute "_score"')            
		del self._score
        
s = Student()
s.score =99
print(s.score)

del s.score
```

 @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样程序运行 时就减少了出错的可能性。 



### 5 魔法方法 

####  （1）id() 方法 

 获取对象在内存中的地址 

 创建对象，并打印对象地址  

```python
dingding2 = Dog('丁丁', '泰迪', 3)
print(id(dingding2))
```

####  （2） \__str__() 方法 

 自定义打印对象内容，以字符串形式打印出来  

 案例： 

```python
class Car:
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
        
    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + int(self.wheelNum) + "个轮胎..."
        return msg
    
    def move(self):
    	print('车在跑，目标:夏威夷')
        
BMW = Car(4, "白色")
print(BMW)
```



###  6 静态方法和类方法 

####  6.1 类方法 

是类对象所拥有的方法，需要用修饰器 @classmethod 来标识其为类方法，对于类方法，第一个参数必须是类对象， 一般以 cls 作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个 参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。 

```python
class People(object):
    country = 'china'
    
    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
    	return cls.country
    
p = People()
print p.getCountry() #可以用过实例对象引用
print People.getCountry() #可以通过类对象引用
```

####  6.2 静态方法  

 需要通过修饰器 @staticmethod 来进行修饰，静态方法不需要多定义参数  

```python
class People(object):
    country = 'china'
    
    @staticmethod
    #静态方法
    def getCountry():
    	return People.country
    
print People.getCountry()
```

 综上:  

 从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的 必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可 能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。静 态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用  



### 7 类的继承 

> 在现实生活中，继承一般指的是子女继承父辈的财产 
>
>  在程序中，继承描述的是事物之间的所属关系，例如猫和狗都属于动物，程序中便可以描述为猫和狗继承自动 物 

```python
# 定义一个父类，如下:
class Cat(object):
    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color
    
    def run(self):
    	print("%s--在跑"%self.name)
        
# 定义一个子类，继承Cat类如下:
class Bosi(Cat):
    def setNewName(self, newName):
    	self.name = newName
    def eat(self):
    	print("%s--在吃"%self.name)
        
bs = Bosi("印度猫")    
print('bs的名字为:%s'%bs.name)
print('bs的颜色为:%s'%bs.color)
bs.eat()
bs.setNewName('波斯')
bs.run()
```

 说明： 

- 私有的属性，不能通过对象直接访问，但是可以通过方法访问
- 私有的方法，不能通过对象直接访问
- 私有的属性、方法，不会被子类继承，也不能被访问
- 一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用 

 **多重继承** 

```python
class base(object):
    def test(self):
    	print('----base test----')
        
class A(base):
    def test(self):
    	print('----A test----')
        
# 定义一个父类
class B(base):
    def test(self):
   		print('----B test----')
        
# 定义一个子类，继承自A、B
class C(A,B):
	pass


obj_C = C()
obj_C.test()
print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
```



**重写父类方法  **

 所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法  

```python
class Cat(object):
    def sayHello(self):
    	print("halou-----1")
        
class Bosi(Cat):
    def sayHello(self):
    	print("halou-----2")
        
bosi = Bosi()

bosi.sayHello()
```

 **调用父类的方法** 

```python
class Cat(object):
    def __init__(self,name):
        self.__id = id #私有的，不被继承到子类
        self.name = name
        self.color = 'yellow'
        
class Bosi(Cat):
	def __init__(self,name):
        # 调用父类的__init__方法1(python2)
        #Cat.__init__(self,name)
        # 调用父类的__init__方法2
        #super(Bosi,self).__init__(name)
        # 调用父类的__init__方法3
        super().__init__(name)
        
    def getName(self):
    	return self.name
    
    
bosi = Bosi('xiaohua')
print(bosi.name)
print(bosi.color)

```



### 8 多态  

 多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”。 

 所谓多态：定义时的类型和运行时的类型不一样，此时就成为多态 

 Python “鸭子类型”  

```python
class F1(object):
    def show(self):
    	print 'F1.show'
        
class S1(F1):
    def show(self):
    	print 'S1.show'
        
class S2(F1):
    def show(self):
    	print 'S2.show'
        
def Func(obj):
	print obj.show()
    
s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)
```



 **说明** 

 python3的面向对象编程其实还有一些高级应用，大部分工作中不会用到 



##  Python异常处理 

###  异常处理 

 当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。 

 python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误 

1. 异常处理 
2. 断言(Assertions) 

####  1 什么是异常？ 

> 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。  
>
>  一般情况下，在Python无法正常处理程序时就会发生一个异常。 
>
>  异常是Python对象，表示一个错误。 

####  2 捕捉异常 

> 捕捉异常可以使用try/except语句。 
>
>  try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。 
>
>  如果你不想在异常发生时结束你的程序，只需在try里捕获它。 

 语法： 

 以下为简单的try....except...else的语法：  

```python
try:
<语句> #运行别的代码
except <名字>：
<语句> #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句> #如果引发了'name'异常，获得附加的数据
else:
<语句> #如果没有异常发生
```

 有时候我们写程序的时候，会出现一些错误或异常，导致程序终止。例如，做除法时，除数为0，会引起一个 ZeroDivisionError 

```python
a=10
b=0
c=a/b
print("done"）
```

 运行结果： 

 Traceback (most recent call last): File "C:/Users/lirong/PycharmProjects/untitled/openfile.py", line 3, in c=a/b ZeroDivisionError: integer division or modulo by zero 



 为了处理异常，我们使用try...except,更改代码： 

```python
a=10
b=0
try:
	c=a/b
	print(c)
except ZeroDivisionError as e:
	print(e)
    
print("done")
```

 此时就会打印出异常 



 **try ...catch...finally** 

 无论异常是否发生，在程序结束前，finally中的语句都会被执行。 

```python
a=10
b=0
try:
	print(a/b)
except ZeroDivisionError as e:
	print(e)
finally:
	print("always excute")
    
print("done")

运行结果：
error
always excute
done

```



###  python所有标准异常类 

| 异常名称          | 描述                       |
| ----------------- | -------------------------- |
| BaseException |所有异常的基类|
| SystemExit |解释器请求退出|
| KeyboardInterrupt |用户中断执行(通常是输入^C)|
| Exception |常规错误的基类|
| StopIteration |迭代器没有更多的值|
| GeneratorExit |生成器(generator)发生异常来通知退出|
| SystemExit |Python 解释器请求退出|
| StandardError |所有的内建标准异常的基类|
| ArithmeticError |所有数值计算错误的基类|
| FloatingPointError |浮点计算错误|
| OverflowError |数值运算超出最大限制|
| ZeroDivisionError |除(或取模)零 (所有数据类型)|
| AssertionError |断言语句失败|
| AttributeError |对象没有这个属性|
| EOFError |没有内建输入,到达EOF 标记|
| EnvironmentError |操作系统错误的基类|
| IOError |输入/输出操作失败|
| OSError |操作系统错误|
| WindowsError |系统调用失败|
| ImportError |导入模块/对象失败|
| KeyboardInterrupt |用户中断执行(通常是输入^C)|
| LookupError |无效数据查询的基类|
| IndexError |序列中没有没有此索引(index)|
| KeyError |映射中没有这个键|
| MemoryError |内存溢出错误(对于Python 解释器不是致命的)|
| NameError |未声明/初始化对象 (没有属性)|
| UnboundLocalError |访问未初始化的本地变量|
| ReferenceError |弱引用(Weak reference)试图访问已经垃圾回收了的对象|
| RuntimeError |一般的运行时错误|
| NotImplementedError |尚未实现的方法|
| SyntaxError |Python 语法错误|
| IndentationError |缩进错误|
| TabError Tab |和空格混用|
| SystemError |一般的解释器系统错误|
| TypeError |对类型无效的操作|
| ValueError |传入无效的参数|
| UnicodeError |Unicode 相关的错误|
| UnicodeDecodeError |Unicode 解码时的错误|
| UnicodeEncodeError |Unicode 编码时错误|
| UnicodeTranslateError |Unicode 转换时错误|
| Warning |警告的基类|
| DeprecationWarning |关于被弃用的特征的警告|
| FutureWarning |关于构造将来语义会有改变的警告|
| OverflowWarning |旧的关于自动提升为长整型(long)的警告|
| PendingDeprecationWarning |关于特性将会被废弃的警告|
| RuntimeWarning |可疑的运行时行为(runtime behavior)的警告|
| SyntaxWarning |可疑的语法的警告|
| UserWarning |用户代码生成的警告|



 **案例：多个except进行多重捕捉**  

```python
try:
	print("try.....")
	r = 10 / int("a")
	print("result:", r)
except ValueError as e:
	print("ValueError:", e)
except ZeroDivisionError as e:
	print("ZeroDivisionError:", e)
finally:
	print("finally...")
print("END...")
```



### 断言(Assertions)  

> 当程序出现错误时，系统会自动引发异常。除此之外，Python也允许程序自行引发异常，自行引发异常使用 raise 语句来完成。  

 如果需要在程序中自行引发异常，则应使用 raise 语句。raise 语句有如下三种常用的用法： 

1.  raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。 
2.  raise 异常类：raise 后带一个异常类。该语句引发指定异常类的默认实例。 
3.  raise 异常对象：引发指定的异常对象。 

 如下可以自定义抛出异常的方式： 

```python
import random
def process():
	i = random.randint(1, 10)
	print(i)
    if i > 8:
    	raise Exception("i is too large")
    elif i > 6:
    	print("i is perfect.")
    else:
    	raise Exception("i is too small")
        
try:
	process()
except Exception as e:
	print(e)

```



## 列表推导式 

### 引言： 

你一定听过这样一个说法，尽量使用列表推导式，而不是用list.append方法来初始化一个列表，那么究竟为何列表 推导式会更快呢？ 

这是因为，列表推导式被编译后的字节码执行速度更快。python当然不是一门编译型语言，但是它还是要被解析成 二进制的字节码才能被执行，执行它的正是python解释器。 python底层还是用C语言写的 

### 什么是列表推导式？ 

> 列表推导能非常简洁的构造一个新列表:只用一条简洁的表达式即可对得到的元素进行转换变形。  



### 格式 

 [表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件] 

```python
result = []
for value in collection:
    if condition:
    	result.append(expression)
```

### 案例分析 

 例子1： 

```python
mlist = []
for x in range(1,5):
    if x > 2:
        for y in range(1,4):
            if y < 3:
            	mlist.append(x*y)
```

修改为列表推导式，如下： 

```python
[x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
```



例子2： 

循环获取1~10之间的每个元素的平方列表 

```python
#for循环
list = []
for x in range(10):
	list.append(x**2)
```

修改为列表推导式如下： 

```python
[x**2 for x in range(10)]
```



 例子3：  

 偶数的平方列表 

```python
list1=[]
for x in range(10):
    if x%2 == 0:
    	list1.append(x**2)
```

 修改为列表推导式 

```python
[x**2 for x in range(10) if x%2 == 0]
```



 例子4：  

 求出30以内所有的能被3整除的数的平方列表 

```python
def squared(x):
	return x * x

multiples = [squared(i) for i in range(30) if i % 3 is 0]
print(multiples)
```



### 列表推导式改造成生成器  

 **使用()生成generator** 

 将推导式的[]改成()即可得到生成器。 

 将上述列表推导式的 [] 改成 () 就成了生成器 

```python
multiples = (i for i in range(30) if i % 3 is 0)
print(type(multiples))
# Output: <type 'generator'>
```

 关于生成器见 下一节 《2_迭代器，生成器》 



### 字典推导式  

> 字典推导和列表推导的使用方法是类似的，只不过将中括号该改成大括号。  

 案例1： 

 快速更换key和value 

```python
mcase = {'a': 20, 'b': 54}
mcase_frequency = {v: k for k, v in mcase.items()}
print mcase_frequency
# Output: {20: 'a', 54: 'b'}
```



 案例2：（此例子在面试过程中笔试命中率达到70%） 

 通过zip对象+两个字符型列表组成字典  

```python
x = ['A', 'B', 'C', 'D']
y = ['a', 'b', 'b', 'd']
mdict = {i: j for i, j in zip(x, y)}
print(mdict)
```



 案例3：  

 将如下二维列表 [(‘name’,’tongpan’),(‘age’,28),(‘height’, 178)] 转换成字典  

```python
myinfo = [('name', 'tongpan'), ('age', 28), ('height', 178)]
dic_myinfo = {key: value for (key, value) in myinfo}
print(dic_myinfo)
```



### 集合推导式  

它们跟列表推导式也是类似的。 唯一的区别在于它使用大括号{} 

 { expr for value in collection if condition } 

```python
squared = {x ** 2 for x in [1, 1, 2]}
print(squared)
# Output: set([1, 4])
```

 用集合推导建字符串长度的集合 

```python
strings = ['a','is','with','if','file','exception']
res = {len(s) for s in strings}
print(res)
```



## 迭代器(iterator)  

### 为何要引入迭代器？ 

通过列表生成式，我们可以直接创建一个列表，但是，受到内存限制，列表容量肯定是有限的，而且创建一个包含 100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的 空间都白白浪费了。 

我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间，在 Python中，这种一边循环一边计算的机制，称为生成器：generator  

### 1.1 什么迭代器呢？ 

> 在Python中如果一个对象有iter( )方法和next( )方法，则称这个对象是迭代器（Iterator）；其中iter( )方法是 让对象可以用for ... in循环遍历，next( )方法是让对象可以通过next(实例名)访问下一个元素。  
>
>  注意：这两个方法必须同时具备，才能称之为迭代器。 

迭代器是在python2.2中被加入的，**它为类序列对象提供了一个类序列的接口**。有了迭代器可以迭代一个不是序列的 对象，因为他表现出了序列的行为。 

迭代器的实质是实现了next()方法的对象，**常见的元组、列表、字典都是迭代器**。 

**迭代器中重点关注两种方法：**  

iter方法：返回迭代器自身。可以通过python内建函数iter()调用。 

next方法：当next方法被调用的时候，迭代器会返回它的下一个值，如果next方法被调用，但迭代器没有只可以返 回，就会引发一个StopIteration异常。该方法可以通过 python 内建函数next()调用。 

举例 

内建函数iter()可以从可迭代对象中获得迭代器。  

```python
>>> it = iter([1,2,3])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>>
```

迭代器是一个带状态的对象，他能在你调用 next() 方法的时候返回容器中的下一个值，任何实现了 \__iter__ 和 \__next__() （python2中实现 next() ）方法的对象都是迭代器。 

\__iter__ 返回迭代器自身， \__next__ 返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration 异常，至于它们到底是如何实现的这并不重要。  

 迭代器就是实现了工厂模式的对象，它在你每次你询问要下一个值的时候给你返回。 

### 1.2 如何创建一个迭代器 

 要创建一个迭代器有2种方法，其中前两种分别是： 

1.  为容器对象添加 \__iter__() 和 \_\_next\_\_() 方法（Python 2.7 中是 next() ）； \_\_iter\_\_() 返回迭代器 对象本身 self ， \_\_next\_\_() 则返回每次调用 next() 或迭代时的元素； 
2.  内置函数 iter() 将可迭代对象转化为迭代器 

 案例：创建迭代器容器 

```python
# Create iterator Object
class Container:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        
    def __iter__(self):
        print("I made this iterator!")
        return self
    
    def __next__(self):
        print("Calling __next__ method!")
        if self.start < self.end:
        	i = self.start
        	self.start += 1
        	return i
        else:
        	raise StopIteration()


c = Container(0, 5)
for i in c:
	print(i)
```

对于迭代器对象，使用for循环遍历整个数组其实是个语法糖，他的内部实现还是通过调用对象的 \__next__() 方 法。  

创建迭代器对象的好处是当序列长度很大时，可以减少内存消耗，因为每次只需要记录一个值即刻（经常看到人们介 绍 Python 2.7 的 range 函数时，建议当长度太大时用 xrange 更快，在 Python 3.5 中已经去除了 xrange 只有一 个类似迭代器一样的 range ）。 

### 1.3 斐波那契数列应用举例 

 我们如果采用正常的斐波那契数列求值过程如下： 

```python
def fibs(n):
    if n == 0 or n == 1:
    	return 1
    else:
    	return fibs(n-1) + fibs(n-2)

print([fibs(i) for i in range(10)])
```



 自定义一个迭代器, 实现斐波那契数列 

```python
class Fib2(object):
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
        self.count = 0
        
    def __iter__(self):
    	return self
    
    def next(self):
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        if self.count > self.n:
        	raise StopIteration
        self.count += 1
        return res


print(list(Fib2(10)))

```



 其他迭代器案例 

 (1) 有很多关于迭代器的例子，比如 itertools 函数返回的都是迭代器对象。 

```python
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

```

 (2) 从一个有限序列中生成无限序列 

```python
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
    print(next(colors))

```

总结： 

对于list、string、tuple、dict等这些容器对象,使用for循环遍历是很方便的。在后台for语句对容器对象调用iter()函 数。iter()是python内置函数。 iter()函数会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内的 元素。next()也是python内置函数。在没有后续元素时，next()会抛出一个StopIteration异常，通知for语句循环结束。 

迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的时候，迭代器会向我们返回它 所记录位置的下一个位置的数据。实际上，在使用next()函数的时候，调用的就是迭代器对象的next方法（Python3 中是对象的next方法，Python2中是对象的next()方法）。所以，我们要想构造一个迭代器，就要实现它的next方 法。但这还不够，python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现iter方法，而iter方法要返回一 个迭代器，迭代器自身正是一个迭代器，所以迭代器的iter方法返回自身self即可。 



## 生成器  

> 生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回 值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。  

### 生成器作用

 延迟操作。也就是在需要的时候才产生结果，不是立即产生结果。 

### 什么是生成器？ 

生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，不同于一般的函数会一次性返 回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很 快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器。 

生成器是包含yield关键字的函数。本质上来说，关键字yield是一个语法糖，内部实现支持了迭代器协议，同时yield 内部是一个状态机，维护着挂起和继续的状态。 

### python中的生成器 

要创建一个generator，有很多种方法，第一种方法很简单，只有把一个列表生成式的[]中括号改为（）小括号，就 创建一个generator 

 举例如下： 

```python
# 列表生成式
lis = [x * x for x in range(10)]
print(lis)
# 生成器
generator_ex = (x * x for x in range(10))
print(generator_ex)

结果：
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
< generator
object < genexpr > at
0x000002A4CBF9EBA0 >

#生成器
generator_ex = (x*x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))

#生成器， 可以直接循环得出结果
generator_ex = (x*x for x in range(10))
for i in generator_ex:
	print(i)
    
结果：
0
1
4
9

```

### 生成器调用顺序 

那么，生成器是怎么调用执行的呢？只需要了解下面几条规则即可：  

 a. 当生成器被调用的时候，函数体的代码不会被执行，而是会返回一个迭代器，其实，生成器函数返回生成器的迭代 器。 “生成器的迭代器”这个术语通常被称作”生成器”。要注意的是生成器就是一类特殊的迭代器。作为一个迭代器， 生成器必须要定义一些方法，其中一个就是next()。如同迭代器一样，我们可以使用next()函数来获取下一个值。需 要明白的是，这一切都是在yield内部实现的。 

 b. 当next()方法第一次被调用的时候，生成器函数才开始执行，执行到yield语句处停止 next()方法的返回值就是yield 语句处的参数（yielded value） 当继续调用next()方法的时候，函数将接着上一次停止的yield语句处继续执行，并 到下一个yield处停止；如果后面没有yield就抛出StopIteration异常。 

 c.每调用一次生成器的next()方法，就会执行生成器中的代码，知道遇到一个yield或者return语句。yield语句意味着 应该生成一个值（在上面已经解释清楚）。return意味着生成器要停止执行，不在产生任何东西。  

 d. 生成器的编写方法和函数定义类似，只是在return的地方改为yield。生成器中可以有多个yield。当生成器遇到一 个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直 到下一个yield。生成器自身又构成一个循环器，每次循环使用一个yield返回的值。 

 **注意：**  

 （1）生成器是只能遍历一次的。

 （2）生成器是一类特殊的迭代器。  

 **分类：**  

####  第一类：生成器函数：  

 生成器函数：也是用def定义的，利用关键字yield一次性返回一个结果，阻塞，重新开始 

 还是使用 def 定义函数，但是，使用yield而不是return语句返回结果。yield语句一次返回一个结果，在每个结果中 间，挂起函数的状态，以便下次从它离开的地方继续执行。 

 如下案例加以说明： 

```python
def Fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return '亲！没有数据了...'

print("@@@@@@@@@@@@@222")
    
# 调用方法，生成出10个数来
f=Fib(10)
# 使用一个循环捕获最后return 返回的值，保存在异常StopIteration的value中
while True:
    try:
        x=next(f)
        print("f:",x)
    except StopIteration as e:
    	print("生成器最后的返回值是：",e.value)
   		break
```

####  第二类：生成器表达式： 

 类似于列表推导，只不过是把一对大括号[]变换为一对小括号()。但是，生成器表达式是按需产生一个生成器结果对 象，要想拿到每一个元素，就需要循环遍历。 

 如下案例加以说明： 

```python
# 一个列表
xiaoke=[2,3,4,5]
# 生成器generator，类似于list，但是是把[]改为()
gen=(a for a in xiaoke)
for i in gen:
	print(i)
#结果是：
2
3
4
5

```

 为什么要使用生成器？因为效率。使用生成器表达式取代列表推导式可以同时节省 cpu 和 内存(RAM)。如果你构造 一个列表(list)的目的仅仅是传递给别的函数, 比如 传递给tuple()或者set(), 那就用生成器表达式替代吧!  

### iter 

 如果一个类想被用于 for ... in 循环，类似list或tuple那样，就必须实现一个 __iter__() 方法，该方法返回一个 迭代对象，然后，Python的for循环就会不断调用该迭代对象的 next() 方法拿到循环的下一个值，直到遇到 StopIteration错误时退出循环。 

 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环： 

```python
class Fib(object):
    def __init__(self):
    	self.a, self.b = 0, 1 # 初始化两个计数器a，b
        
    def __iter__(self):
    	return self # 实例本身就是迭代对象，故返回自己
    
    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
        	raise StopIteration();
        return self.a # 返回下一个值
```

 现在，试试把Fib实例作用于for循环： 

```python
>>> for n in Fib():
... print n
...
1
1
2
3
5
...
46368
75025
```



###  getitem 

 要表现得像list那样按照下标取出元素，需要实现 \__getitem__() 方法： 

```python
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
        	a, b = b, a + b
        return a

```

 现在，就可以按下标访问数列的任意一项了：  

```python
>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
573147844013817084101
```

 但是list有个神奇的切片方法： 

```python
>>> range(100)[5:10]
[5, 6, 7, 8, 9]
```

 对于Fib却报错。原因是 \__getitem__() 传入的参数可能是一个int，也可能是一个切片对象 slice ，所以要做判 断：  

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
            	a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
            	if x >= start:
            	L.append(a)
            	a, b = b, a + b
            return L
```

 现在试试Fib的切片： 

```python
>>> f = Fib()
>>> f[0:5]
[1, 1, 2, 3, 5]
>>> f[:10]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

```

 但是没有对step参数作处理： 

```python
>>> f[:10:2]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

 也没有对负数作处理，所以，要正确实现一个 \__getitem__() 还是有很多工作要做的。 

###  文件是可迭代对象，也是迭代器 

```python
f = open('housing.csv')
from collections import Iterator
from collections import Iterable

print(isinstance(f, Iterator)) #判断是不是迭代器
print(isinstance(f, Iterable)) #判断是不是可迭代对象

True
True

```

###  小结： 

-  凡是可作用于 for 循环的对象都是 Iterable 类型；
- 凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；
- 集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。 

 Python3的 for 循环本质上就是通过不断调用 next() 函数实现的，例如：  

```python
for x in [1, 2, 3, 4, 5]:
	pass
```

 实际上完全等价于  

```python
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

```

###  yield的总结  

 （1）通常的for..in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文 件。他可以是a = [1,2,3]，也可以是a = [x*x for x in range(3)]。 它的缺点也很明显，就是所有数据都在内存里面，如果有海量的数据，将会非常耗内存。 

 （2）生成器是可以迭代的，但是只可以读取它一次。因为用的时候才生成，比如a = (x*x for x in range(3))。!!!! 注意这里是小括号而不是方括号。 

（3）生成器（generator）能够迭代的关键是他有next()方法，工作原理就是通过重复调用next()方法，直到捕 获一个异常。 

（4）带有yield的函数不再是一个普通的函数，而是一个生成器generator，可用于迭代 

（5）yield是一个类似return 的关键字，迭代一次遇到yield的时候就返回yield后面或者右面的值。而且下一次 迭代的时候，从上一次迭代遇到的yield后面的代码开始执行 

（6）yield就是return返回的一个值，并且记住这个返回的位置。下一次迭代就从这个位置开始。 

（7）带有yield的函数不仅仅是只用于for循环，而且可用于某个函数的参数，只要这个函数的参数也允许迭代参 数。 

（8）send()和next()的区别就在于send可传递参数给yield表达式，这时候传递的参数就会作为yield表达式的 值，而yield的参数是返回给调用者的值，也就是说send可以强行修改上一个yield表达式值。 

（9）send()和next()都有返回值，他们的返回值是当前迭代遇到的yield的时候，yield后面表达式的值，其实就 是当前迭代yield后面的参数。 

（10）第一次调用时候必须先next（）或send（）,否则会报错，send后之所以为None是因为这时候没有上一 个yield，所以也可以认为next（）等同于send(None)



## 豆瓣源安装库：

pip install sqlalchemy -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 pip install pymysql  -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

pip install requests  -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 pip install lxml    -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 pip install bs4   -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

pip install pandas  -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com



##  MySQL SQL语句大全 

###  SQL 语句分类 

 DDL（Data Definition Languages）语句：数据定义语言，这些语句定义了不同的数据段、数据库、表、列、索 引等数据库对象的定义。常用的语句关键字主要包括 create、drop、alter等。 

 DML（Data Manipulation Language）语句：数据操纵语句，用于添加、删除、更新和查询数据库记录，并检查 数据完整性，常用的语句关键字主要包括 insert、delete、udpate 和select 等。(增添改查）  

 DCL（Data Control Language）语句：数据控制语句，用于控制不同数据段直接的许可和访问级别的语句。这些 语句定义了数据库、表、字段、用户的访问权限和安全级别。主要的语句关键字包括 grant、revoke 等。 

**DDL 语句： **

 DDL 是数据定义语言的缩写，简单来说，就是对数据库内部的对象进行创建、删除、修改的操作语言。它和 DML 语 言的最大区别是 DML 只是对表内部数据的操作，而不涉及到表的定义、结构的修改，更不会涉及到其他对象。DDL 语句更多的被数据库管理员（DBA）所使用，一般的开发人员很少使用。 

1.  说明：创建数据库 

    CREATE DATABASE database default charset utf8; 

2.  说明：删除数据库 

    drop database dbname 

3. 说明：备份sql server

    --- 创建 备份数据的 device

   还原一个数据库: mysql -h localhost -u root -p123456 先登录

   source ./xxx.sql 执行sql文件进行还原

   备份一个数据库:mysqldump -h localhost -u root -p123456 www > d:\www2008-2-26.sql  

    其中WWW为数据库名 

    eg:  

    mysqldump -hlocalhost -uzhougy -p123456 sh_1801_lesson > ./database.sql 

    选择你所创建的数据库  

    mysql> USE database; (按回车键出现Database changed 时说明操作成功！) 

4.  查看现在的数据库中存在什么表  

    mysql> SHOW TABLES; 

5.  创建一个数据库表  

    mysql> CREATE TABLE MYTABLE (name VARCHAR(20), sex CHAR(1)); 

6.  显示表的结构： 

    mysql> DESCRIBE MYTABLE; （or desc mytable;）  

7.  往表中加入记录 

    mysql> insert into MYTABLE values (”hyq”,”M”); 

8.  用文本方式将数据装入数据库表中（例如D:/mysql.txt） 

    mysql> LOAD DATA LOCAL INFILE “D:/mysql.txt” INTO TABLE MYTABLE; 

    类似于hive操作 

9.  导入.sql文件命令（例如D:/mysql.sql）  

    mysql>use database; 

    mysql>source d:/mysql.sql; 

10.  删除表  

     mysql>drop TABLE MYTABLE 

11.  清空表  

     mysql>delete from MYTABLE; （or truncate table MYTABLE; ） 

     delete 清空表的记录  

     truncate table： 清空表的结构和记录 

12.  更新表中数据 

     mysql>update MYTABLE set sex=”f” where name='hyq'; 

13.  增加一个列  

     Alter table tabname add column col type;  

     在student表中添加一个列，在name字段后 

     alter table student add column sex varchar(100) after name; 

     alter table student drop sex ; 

     alter table student add column sex int default 0 after name; 

14.  添加主键 

     主键：当前数据库表中某一个字段，在表内唯一性。查询方便，方便数据迁移 

     外键：其他表主键在本表中的字段 

     Alter table tabname add primary key(ID)(设置某字段为主键，ID可自由设置，主键数据不可重复）  

15.  删除主键 

     Alter table tabname drop primary key(ID)（删除某字段主键）

     show create table student \G;  

     \G: 方便文本查看，不加就是表格查看。 

16.  索引 

     搜索引擎采用倒排索引。 

     数据库中索引主要是为了方便查询；但是索引多了表维护成本大 

     主键也是一种特殊的索引 

     创建索引： 

     CREATE INDEX indexName ON mytable(username(length)); 

     修改表结构，添加索引 

     ALTER table tableName ADD INDEX indexName(columnName)  

     DROP INDEX [indexName] ON mytable; 

     使用 SHOW INDEX 命令来列出表中的相关的索引信息。可以通过添加 \G 来格式化输出信息  

     mysql> SHOW INDEX FROM table_name \G;  

     create index stu_index on student(address);  

17.  去除重复的值 

     格式: select distinct 字段名 from 表名 where 条件; 例: select distinct gender from student; 

18.  聚合函数 count(*) 求当前结果总共有多少条数据 

    ``` mysql
    sum(列名) 求列名对应列的和
    avg(列名) 求当前列的平均值
    max(列名) 求当前列的最大值
    min(列名) 求当前列的最小值
    例: 求当前表总共有多少条数据?
    select count(*) from student;
    求年龄最小的?
    select min(age) from student;
    ```

    

19.  分组 group by 格式: select 字段名... from 表名 where 条件 group by 字段名 查看有多少种性别 例: select gender from student group by gender; 需求:统计 男生 和 女生 各有多少个 select gender,count() from student group by gender; 需求: 统计所有女生的个数? 例: select gender,count() from student group by gender having gender = 1;  

    ```mysql
    where 查询条件, 是对select数据结果加的查询条件
    having 查询条件 是对group by分组后结果加的查询条件
    ```

    

20.  排序 

     格式: select 字段名... from 表名 where 条件 order by 字段名1,字段名2... 例: 年龄小到大 

    ```mysql
    select * from student order by age;
    ```

     默认是从小到大排列 asc 从小到大 desc 从大到小 select * from student order by age asc; 

21.  分页 

     格式: select 字段名... from 表名 where 条件 limit 起始值,多少条数据 起始值可以从 0 开始 例: select * from student limit 0,3; 

    ```mysql
    如果每页数据量为30，页码从1开始
    page = 1： limit 0,30;
    page = 2： limit 30,30;
    page = 3： limit 60,30;
    ...
    page = n： limit (n-1)*30,30;
    ```

     存在一个问题： 

     数据更新比较快，过度依赖数据库进行计算，比较耗费资源 

    

    案例分析

       如何采用python语言操作mysql数据库？

    采用pymysql ---- python3推荐一种mysql数据库连接库

    安装过程： pip install pymysql 

    

##  Python-ORM实战 

###  什么是ORM? 

 ORM（object relational mapping）, 就是对象关系映射，简单来说我们类似python这种面向对象的程序来说一切皆 对象，但是我们使用的数据库却都是关系型的，为了保证一致的使用习惯，通过orm将编程语言的对象模型和数据库 的关系模型建立映射关系，这样我们在使用编程语言对数据库进行操作的时候可以直接使用编程语言的对象模型进行 操作就可以了，而不用直接使用sql语言。

ORM作用: 对象模型（类） 《====》 关系模型 进行关联 

 用户只需要操作类就可以实现操作数据库 

 ORM 相当于把数据库也实例化，在代码操作mysql中级又加了orm这一层。 

###  ORM 的优点： 

1.  隐藏了数据访问细节，“封闭”的通用数据库交互，ORM的核心。他使得我们的通用数据库交互变得简单易行， 并且完全不用考虑该死的SQL语句。快速开发，由此而来。  

2.  ORM使我们构造固化数据结构变得简单易行。  

   ![](\img\企业微信截图_16705842478765.png)

###  sqlalchemy 

 在Python中，最有名的ORM框架是SQLAlchemy。用户包括openstack＼Dropbox等知名公司或应用. 

 安装依赖库(豆瓣源)： 

 pip install sqlalchemy -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 pip install pymysql  -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操 作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。SQLAlchemy本身无法操作数据 库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库 API，从而实现对数据库的操作： 

 相关连接语句如下：  

```python
MySQL - Python (python2.7推荐)
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
        
pymysql (python3.5以上版本推荐使用)
mysql+pymysql://<username>:<password>@<host>:<port>/<dbname>[?<options>]
            
MySQL - Connector
mysql + mysqlconnector: // < user >: < password >
        
cx_Oracle (oracle数据连接)
	oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
```

### ORM 案例分析 

```python
'''
采用sqlalchemy定义实体类，进行ORM操作
依赖库：
pip install sqlalchemy
pip install pymysql
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
'''
数据库连接拼接串语法：
mysql_conn_str = "mysql+pymysql://username:password@IP:PORT/database"
'''
mysql_conn_str = "mysql+pymysql://django:123456@172.16.245.202:3306/toscrape"
engine = create_engine(mysql_conn_str)
Base = declarative_base()

class Book(Base):
    __tablename__ = "toscrape_book"
    id = Column(Integer, primary_key=True) #create id column, set it auto_increment.
    book_title = Column(String(200))
    image_url = Column(String(300))
    book_url = Column(String(300))
    book_rate = Column(String(50))
    book_price = Column(String(15))
    
'''
初始化DB，进行模型 --> 数据库 同步
'''
def _create_db_table():
	Base.metadata.create_all(engine)
    
def create_session():
    _create_db_table()
    Session = sessionmaker(bind=engine)
    session = Session()
    #session = sessinmaker(bind=engine)()
    return session

'''
add record to session.
objs --> (1) [obj1, obj2] (2) obj
'''
def add_records(session, objs):
    if isinstance(objs, list):
    	session.add_all(objs)
    else:
        session.add(objs)
        session.commit()
        
'''
查询数据模型中的db数据
'''
def query_records(session, Cls):
	return session.query(Cls).all()

if __name__ == "__main__":
    session = create_session()
    '''
    records = query_records(session, Book)
    for rec in records:
    	print("title: " + rec.book_title + ", image_url:" + rec.image_url)
    '''
    
    book = Book(book_title='xxx', image_url='xxx', book_url='xxx', book_rate='2.0',
    	book_price='xxx')
    add_records(session, book)
```

 相关参考文档： https://blog.csdn.net/fgf00/article/details/52949973 



##  Redis 介绍 

 **实现缓存的方式，有多种，本地内存缓存，数据库缓存，文件系统缓存。这里介绍使用Redis 数据库进行缓存。  **

###  Redis是什么？ 

 REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。 

 Redis是一个开源的使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数 据库，并提供多种语言的API。 

 它通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Map), 列表(list), 集合(sets) 和 有序集合 (sorted sets)等类型。 

###  Redis 简介 

 Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。  

 Redis 与其他 key - value 缓存产品有以下三个特点： 

-  Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。 
-  Redis不仅仅支持简单的key-value类型的数据(memcache)，同时还提供list，set，zset，hash等数据结构的存 储。  
-  Redis支持数据的备份，即master-slave模式的数据备份。 

###  Redis 优势 

-  性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。 
-  丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。 
-  原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多 个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。  
-  丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。  

###  安装Redis  

 wget http://download.redis.io/releases/redis-3.2.6.tar.gz 

 解压： 

 tar -zxvf redis-3.2.6.tar.gz 

 cd redis-3.2.6 



 编译： 

 cd redis-3.2.6 #进入目录 make #编译  



 设置redis 

 mkdir /usr/local/redis #创建redis操作目录 cp src/redis-server src/redis-cli /usr/local/redis/bin/ #复制redis服务 和命令 cp redis.conf /usr/local/redis/conf #复制redis配置文件 cd /usr/local/redis ./bin/redis-server conf/redis.conf & #后台启动redis 



 创建快捷键 

 vim ~/.bashrc alias redis='/usr/local/redis/bin/redis-cli' #添加快捷键 source ~/.bashrc #使生效 



 redis远程连接 

 redis-cli -h 172.16.245.xxx -p 6379

redis 172.16.245.179:6379> 



 安装验证成功！ 



###  配置文件 

 redis.conf 配置项说明如下： 

1.   Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程 

   daemonize no 

2.  当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定 

   pidfile /var/run/redis.pid  

3.  指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为 6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字  

    port 6379  

4.  绑定的主机地址 

    bind 127.0.0.1 

5.  当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能 

    timeout 300 

6.  指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose 

    loglevel verbose 

7.  日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输 出，则日志将会发送给/dev/null 

    logfile stdout  

8.   设置数据库的数量，默认数据库为0，可以使用SELECT 命令在连接上指定数据库id 

    databases 16 

9.  指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合 

    save  

    Redis默认配置文件中提供了三个条件： 

    save 900 1 

    ** save 300 10** 

   ** save 60 10000** 

    分别表示900秒（15分钟）内有1个更改，300秒（5分钟）内有10个更改以及60秒内有10000个更改。  

10.  指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该 选项，但会导致数据库文件变的巨大  

     rdbcompression yes  

11.  指定本地数据库文件名，默认值为dump.rdb  

     dbfilename dump.rdb 

12.  指定本地数据库存放目录  

     dir ./ 

13.  设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步 

     slaveof  

14.  当master服务设置了密码保护时，slav服务连接master的密码  

     masterauth 

15.  设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH 命令提供密码，默认关闭

     requirepass foobared   

16.  设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大 文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客 户端返回max number of clients reached错误信息  

     maxclients 128 

17.  指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期 或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。 Redis新的vm机制，会把Key存放内存，Value会存放在swap区 

     maxmemory 

18.  指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会 在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在 一段时间内只存在于内存中。默认为no 

     appendonly no 

19.  指定更新日志文件名，默认为appendonly.aof 

     appendfilename appendonly.aof  

20.  指定更新日志条件，共有3个可选值： no：表示等操作系统进行数据缓存同步到磁盘（快） always：表示每 次更新操作后手动调用fsync()将数据写到磁盘（慢，安全） everysec：表示每秒同步一次（折衷，默认值） 

     appendfsync everysec  

21.  指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少 的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机 制） 

     vm-enabled no 

22.  虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享  

     vm-swap-file /tmp/redis.swap 

23.  将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储 的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认 值为0  

     vm-max-memory 0 

24.  Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享， vm-page-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者 64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值  

     vm-page-size 32 

25.  设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上 每8个pages将消耗1byte的内存。  

     vm-pages 134217728  

26.  设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的， 可能会造成比较长时间的延迟。默认值为4  

     vm-max-threads 4 

27.  设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启 

     glueoutputbuf yes 

28.  指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法 

     hash-max-zipmap-entries 64  

     ** hash-max-zipmap-value 512** 

29.   指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍） 

     activerehashing yes 

30.  指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有 自己的特定配置文件 

     include /path/to/local.conf 

     查看配置信息 

     redis 127.0.0.1:6379> CONFIG GET * 



###  Redis数据类型 

####  String（字符串） 

 string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。

 string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

 string类型是Redis最基本的数据类型，一个键最大能存储512MB。 

 实例  

```redis
redis 127.0.0.1:6379> SET name "1000phone"
OK
redis 127.0.0.1:6379> GET name
"1000phone"
```



####  Hash（哈希） 

 Redis hash 是一个键值(key=>value)对集合。

 Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。 

 实例 

```
redis> HMSET myhash field1 "Hello" field2 "World"
"OK"
redis> HGET myhash field1
"Hello"
redis> HGET myhash field2
"World"
```

 redis 172.16.245.179:6379> hgetall myhash 1) "fd1" 2) "value1" 3) "fd2" 4) "value2" 5) "fd3" 6) "value2"  

 fd1 fd2 fd3 

value1 value2 value3  



####  List（列表） 

 Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右 边）。  

 实例 

```
redis 127.0.0.1:6379> lpush name redis
(integer) 1
redis 127.0.0.1:6379> lpush name mongodb
(integer) 2
redis 127.0.0.1:6379> lpush name rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange name 0 10
1) "rabitmq"
2) "mongodb"
3) "redis"
redis 127.0.0.1:6379> rpop name

```



####  Set（集合） 

 Redis的Set是string类型的无序集合。 

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。  

**sadd 命令**

 添加一个 string 元素到 key 对应的 set 集合中，成功返回1，如果元素已经在集合中返回 0，如果 key 对应的 set 不 存在则返回错误。 

 sadd key member  

 实例 

```
redis 127.0.0.1:6379> sadd name redis
(integer) 1
redis 127.0.0.1:6379> sadd name mongodb
(integer) 1
redis 127.0.0.1:6379> sadd name rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd name rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers name
1) "redis"
2) "rabitmq"
3) "mongodb"
```



####  zset(sorted set：有序集合)  

 Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。 

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

 zset的成员是唯一的,但分数(score)却可以重复。 

**zadd 命令 **

 添加元素到集合，元素在集合中存在则更新对应score 

 zadd key score member 

 实例 

```
redis 127.0.0.1:6379> zadd runoob 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> > ZRANGEBYSCORE runoob 0 1000
1) "mongodb"
2) "rabitmq"
3) "redis"
```



####  Redis 发布订阅  

 Redis 发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。 

Redis 客户端可以订阅任意数量的频道。 

下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：  



 当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：  



 实例  

 以下实例演示了发布订阅是如何工作的。在我们实例中我们创建了订阅频道名为 redisChat: 



```
redis 127.0.0.1:6379> SUBSCRIBE redisChat
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1
```

 现在，我们先重新开启个 redis 客户端，然后在同一个频道 redisChat 发布两次消息，订阅者就能接收到消息。  

```
redis 127.0.0.1:6379> PUBLISH redisChat "Redis is a great caching technique"
(integer) 1
redis 127.0.0.1:6379> PUBLISH redisChat "Learn redis by runoob.com"
(integer) 1
# 订阅者的客户端会显示如下消息
1) "message"
2) "redisChat"
3) "Redis is a great caching technique"
1) "message"
2) "redisChat"
3) "Learn redis by runoob.com"

```



###  Python操作Redis 

 安装redis-py  

 pip install redis  -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

 redis-py 的API的使用可以分类为： 

-  连接方式 

- 连接池 

- 操作  

  -  String 操作 
  - Hash 操作 
  - List 操作 
  - Set 操作 
  - Sort Set 操作 

- 管道  

   redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用 官方的语法和命令，Redis是StrictRedis的子类 

```python
import redis

r = redis.Redis(host='192.168.49.130', port=6379)
r.set('foo', 'Bar')
print r.get('foo')
```

**创建连接池:**

 redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认， 每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个 Redis实例共享一个连接池。 

```python
import redis

pool = redis.ConnectionPool(host='192.168.49.130', port=6379)

r = redis.Redis(connection_pool=pool)
#r = redis.StrictRedis(connection_pool=pool) #StrictRedis也是支持的
r.set('foo', 'Bar')
print r.get('foo')

```

 MySQL数据有两种存储引擎： 

MyISAM — 表锁 

INONDB — 表行锁 ———这种存储方式推荐使用， 支持事务 

###  应用场景案例 

####  1 页面点击数  

 假定我们对一系列页面需要记录点击次数。例如论坛的每个帖子都要记录点击次数，而点击次数比回帖的次数的多得 多。如果使用关系数据库来存储点击，可能存在大量的行级锁争用。所以，点击数的增加使用redis的INCR命令最好 不过了。 

 当redis服务器启动时，可以从关系数据库读入点击数的初始值（1237这个页面被访问了34634次） 

```
>>> r.set("visit:1237:totals",34634)
True
```

 每当有一个页面点击，则使用INCR增加点击数即可。 

```
>>> r.incr("visit:1237:totals")
34635
>>> r.incr("visit:1237:totals")
34636
页面载入的时候则可直接获取这个值
>>> r.get ("visit:1237:totals")
'34636'
```

#### 2 使用hash类型保存多样化对象，类似二维表结构 

 当有大量类型文档的对象，文档的内容都不一样时，（即“表”没有固定的列），可以使用hash来表达。  

```
>>> r.hset('users:jdoe', 'name', "John Doe")
1L
>>> r.hset('users:jdoe', 'email', 'John@test.com')
1L
>>> r.hset('users:jdoe', 'phone', '1555313940')
1L
>>> r.hincrby('users:jdoe', 'visits', 1)
1L
>>> r.hgetall('users:jdoe')
{'phone': '1555313940', 'name': 'John Doe', 'visits': '1', 'email': 'John@test.com'}
>>> r.hkeys('users:jdoe')
['name', 'email', 'phone', 'visits']
```

#### 4  社交圈子数据 

 在社交网站中，每一个圈子(circle)都有自己的用户群。通过圈子可以找到有共同特征（比如某一体育活动、游戏、电 影等爱好者）的人。当一个用户加入一个或几个圈子后，系统可以向这个用户推荐圈子中的人。 我们定义这样两个 圈子,并加入一些圈子成员。 

```
>>> r.sadd('circle:game:lol','user:debugo')
1
>>> r.sadd('circle:game:lol','user:leo')
1
>>> r.sadd('circle:game:lol','user:Guo')
1
>>> r.sadd('circle:soccer:InterMilan','user:Guo')
1
>>> r.sadd('circle:soccer:InterMilan','user:Levis')
1
>>> r.sadd('circle:soccer:InterMilan','user:leo')
1
```

 获取一个圈子的成员 

```
>>> r.smembers('circle:game:lol')
set(['user:Guo', 'user:debugo', 'user:leo'])
```

 可以使用集合运算来得到几个圈子的共同成员：  

```
>>> r.sinter('circle:game:lol', 'circle:soccer:InterMilan')
set(['user:Guo', 'user:leo'])
>>> r.sunion('circle:game:lol', 'circle:soccer:InterMilan')
set(['user:Levis', 'user:Guo', 'user:debugo', 'user:leo'])
```



##  Python多进程原理与实现 

###  1 进程的基本概念  

 什么是进程？  

 进程就是一个程序在一个数据集上的一次动态执行过程。进程一般由程序、数据集、进程控制块三部分组成。我们编 写的程序用来描述进程要完成哪些功能以及如何完成；数据集则是程序在执行过程中所需要使用的资源；进程控制块 用来记录进程的外部特征，描述进程的执行变化过程，系统可以利用它来控制和管理进程，它是系统感知进程存在的 唯一标志。  

###  2 父进程和子进程 

 Linux 操作系统提供了一个 fork() 函数用来创建子进程，这个函数很特殊，调用一次，返回两次，因为操作系统是将 当前的进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回。子进程永远返回0，而父进程返 回子进程的 PID。我们可以通过判断返回值是不是 0 来判断当前是在父进程还是子进程中执行。

 Python 中同样提供了 fork() 函数，此函数位于 os 模块下。  

```python
import os
import time

print("在创建子进程前: pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

pid = os.fork() #一次调用，两次返回
if pid == 0:
	print("子进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
	time.sleep(5)
else:
	print("父进程信息: pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    # pid表示回收的子进程的pid
    #pid, result = os.wait() # 回收子进程资源 阻塞
    time.sleep(5)
    #print("父进程：回收的子进程pid=%d" % pid)
    #print("父进程：子进程退出时 result=%d" % result)
    
# 下面的内容会被打印两次，一次是在父进程中，一次是在子进程中。
# 父进程中拿到的返回值是创建的子进程的pid，大于0
print("fork创建完后: pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
```

####  2.1 父子进程如何区分?  

 子进程是父进程通过fork()产生出来的，pid = os.fork() 

通过返回值pid是否为0，判断是否为子进程，如果是0，则表示是子进程 

由于 fork() 是 Linux 上的概念，所以如果要跨平台，最好还是使用 subprocess 模块来创建子进程。 

####  2.2 子进程如何回收？ 

 python中采用os.wait()方法用来回收子进程占用的资源 

pid, result = os.wait() # 回收子进程资源 阻塞，等待子进程执行完成回收 

如果有子进程没有被回收的，但是父进程已经死掉了，这个子进程就是僵尸进程。 



###  3 Python进程模块 

 python的进程multiprocessing模块有多种创建进程的方式，每种创建方式和进程资源的回收都不太相同，下面分别 针对Process,Pool及系统自带的fork三种进程分析。  

####  3.1 fork(  )  

```python
import os
pid = os.fork() # 创建一个子进程
os.wait() # 等待子进程结束释放资源
pid为0的代表子进程。
```

 缺点： 1.兼容性差，只能在类linux系统下使用，windows系统不可使用； 2.扩展性差，当需要多条进程的时候，进 程管理变得很复杂； 3.会产生“孤儿”进程和“僵尸”进程，需要手动回收资源。 优点： 是系统自带的接近低层的创建 方式，运行效率高。 

####  3.2 Process进程 

 multiprocessing模块提供Process类实现新建进程  

```python
import os
from multiprocessing import Process
import time

def fun(name):
    print("2 子进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    print("hello " + name)

def test():
	print('ssss')
    
if __name__ == "__main__":
    print("1 主进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps = Process(target=fun, args=('jingsanpang', ))
    print("111 ##### ps pid: " + str(ps.pid) + ", ident:" + str(ps.ident))
    print("3 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    print(ps.is_alive())
    ps.start()
    print(ps.is_alive())
    print("222 #### ps pid: " + str(ps.pid) + ", ident:" + str(ps.ident))
    print("4 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps.join()
    print(ps.is_alive())
    print("5 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps.terminate()
    print("6 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

```

**特点：** 

1.注意：Process对象可以创建进程，但Process对象不是进程，其删除与否与系统资源是否被回收没有直接 的关系。 

2.主进程执行完毕后会默认等待子进程结束后回收资源，不需要手动回收资源；join()函数用来控制子进程  结束的顺序,其内部也有一个清除僵尸进程的函数，可以回收资源； 

3.Process进程创建时，子进程会将主进程的 Process对象完全复制一份，这样在主进程和子进程各有一个 Process对象，但是p.start()启动的是子进程，主进程中 的Process对象作为一个静态对象存在，不执行。 

4.当子进程执行完毕后，会产生一个僵尸进程，其会被join函数回收，或者再有一条进程开启，start函数也会回收僵 尸进程，所以不一定需要写join函数。 

5.windows系统在子进程结束后会立即自动清除子进程的Process对象，而 linux系统子进程的Process对象如果没有join函数和start函数的话会在主进程结束后统一清除。 

另外还可以通过继承Process对象来重写run方法创建进程 

####  3.3 进程池POOL (多个进程 ）

 进程池：为了避免我们多进程创建，销毁带来的开销，引入的进程池 

```python
import multiprocessing
import time

def work(msg):
	mult_proces_name = multiprocessing.current_process().name
	print('process: ' + mult_proces_name + '-' + msg)
    
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=5) # 创建4个进程
    for i in range(20):
		msg = "process %d" %(i)
    pool.apply_async(work, (msg, ))
    pool.close() # 关闭进程池，表示不能在往进程池中添加进程
    pool.join() # 等待进程池中的所有进程执行完毕，必须在close()之后调用
    print("Sub-process all done.")
```

 上述代码中的 pool.apply_async() 是 apply() 函数的变体， apply_async() 是 apply() 的并行版本， apply() 是 apply_async() 的阻塞版本，使用 apply() 主进程会被阻塞直到函数执行结束，所以说是阻塞版本。 apply() 既 是 Pool 的方法，也是Python内置的函数，两者等价。可以看到输出结果并不是按照代码for循环中的顺序输出的。  

 多个子进程并返回值  

 apply_async() 本身就可以返回被进程调用的函数的返回值。上一个创建多个子进程的代码中，如果在函数 func 中 返回一个值，那么 pool.apply_async(func, (msg, )) 的结果就是返回pool中所有进程的值的对象（注意是对 象，不是值本身）。 

```python
import multiprocessing
import time

def func(msg):
	return multiprocessing.current_process().name + '-' + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4) # 创建4个进程
    results = []
    for i in range(20):
    	msg = "process %d" %(i)
    	results.append(pool.apply_async(func, (msg, )))
    pool.close() # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    pool.join() # 等待进程池中的所有进程执行完毕
    print ("Sub-process(es) done.")
    
    for res in results:
    	print (res.get())

```

 与之前的输出不同，这次的输出是有序的。 

 如果电脑是八核，建立8个进程，在Ubuntu下输入top命令再按下大键盘的1，可以看到每个CPU的使用率是比较平 均的 

###  4 进程间通信方式 

1.  管道pipe：管道是一种半双工的通信方式，数据只能单向流动，而且只能在具有亲缘关系的进程间使用。进程 的亲缘关系通常是指父子进程关系。  
2.  命名管道FIFO：有名管道也是半双工的通信方式，但是它允许无亲缘关系进程间的通信。 
3.   消息队列MessageQueue：消息队列是由消息的链表，存放在内核中并由消息队列标识符标识。消息队列克服 了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点。  
4.   共享存储SharedMemory：共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创 建，但多个进程都可以访问。共享内存是最快的 IPC 方式，它是针对其他进程间通信方式运行效率低而专门设  计的。它往往与其他通信机制，如信号两，配合使用，来实现进程间的同步和通信。 

 以上几种进程间通信方式中，消息队列是使用的比较频繁的方式。 



 （1）管道pipe 

```python
import multiprocessing

def foo(sk):
	sk.send('hello father')
	print(sk.recv())
    
if __name__ == '__main__':
    conn1,conn2=multiprocessing.Pipe() #开辟两个口，都是能进能出，括号中如果False即单向通信
    p=multiprocessing.Process(target=foo,args=(conn1,)) #子进程使用sock口，调用foo函数
    p.start()
    print(conn2.recv()) #主进程使用conn口接收
    conn2.send('hi son') #主进程使用conn口发送
```

 （2）消息队列Queue 

 Queue是多进程的安全队列，可以使用Queue实现多进程之间的数据传递。  

 Queue的一些常用方法： 

-  Queue.qsize()：返回当前队列包含的消息数量； 
- Queue.empty()：如果队列为空，返回True，反之False ； 
- Queue.full()：如果队列满了，返回True,反之False； 
- Queue.get():获取队列中的一条消息，然后将其从列队中移除，可传参超时时长。 
- Queue.get_nowait()：相当Queue.get(False),取不到值时触发异常：Empty； 
- Queue.put():将一个值添加进数列，可传参超时时长。 
- Queue.put_nowait():相当于Queue.get(False),当队列满了时报错：Full。 

 案例：  

```python
from multiprocessing import Process, Queue
import time

def write(q):
    for i in ['A', 'B', 'C', 'D', 'E']:
    	print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)
        
def read(q):
    while True:
        v = q.get(True)
        print('get %s from queue' % v)
        
if __name__ == '__main__':
	q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    print('write process = ', pw)
    print('read process = ', pr)
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    pr.terminate()
    pw.terminate()
```

 Queue和pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。 

注：进程间通信应该尽量避免使用共享数据的方式 



###  5 多进程实现生产者消费者 

 以下通过多进程实现生产者，消费者模式 

```python
import multiprocessing
from multiprocessing import Process
from time import sleep
import time

class MultiProcessProducer(multiprocessing.Process):
    def __init__(self, num, queue):
        """Constructor"""
        multiprocessing.Process.__init__(self)
            self.num = num
            self.queue = queue
        
    def run(self):
        t1 = time.time()
        print('producer start ' + str(self.num))
        for i in range(1000):
        	self.queue.put((i, self.num))
        # print 'producer put', i, self.num
        t2 = time.time()
        print('producer exit ' + str(self.num))
        use_time = str(t2 - t1)
        print('producer ' + str(self.num) + ',
        use_time: '+ use_time)
              
class MultiProcessConsumer(multiprocessing.Process):
	def __init__(self, num, queue):
        """Constructor"""
        multiprocessing.Process.__init__(self)
            self.num = num
            self.queue = queue
              
    def run(self):
        t1 = time.time()
        print('consumer start ' + str(self.num))
        while True:
            d = self.queue.get()
            if d != None:
                # print 'consumer get', d, self.num
                continue
            else:
            	break
        t2 = time.time()
        print('consumer exit ' + str(self.num))
        print('consumer ' + str(self.num) + ', use time:' + str(t2 - t1))
              
def main():
    # create queue
    queue = multiprocessing.Queue()
    # create processes
    producer = []
    for i in range(5):
    	producer.append(MultiProcessProducer(i, queue))
              
    consumer = []
    for i in range(5):
    consumer.append(MultiProcessConsumer(i, queue))
              
    # start processes
    for i in range(len(producer)):
    	producer[i].start()
              
    for i in range(len(consumer)):
    	consumer[i].start()
              
    # wait for processs to exit
    for i in range(len(producer)):
    	producer[i].join()
              
    for i in range(len(consumer)):
    	queue.put(None)
              
    for i in range(len(consumer)):
    	consumer[i].join()
              
    print('all done finish')
              
if __name__ == "__main__":
	main()

```



###  6 总结 

 python中的多进程创建有以下两种方式： 

（1）fork子进程 

（2）采用 multiprocessing 这个库创建子进程 

需要注意的是队列中Queue.Queue是线程安全的，但并不是进程安全，所以多进程一般使用线程、进程安全的 multiprocessing.Queue() 

另外, 进程池使用 multiprocessing.Pool实现，pool = multiprocessing.Pool(processes = 3)，产生一个进程池， pool.apply_async实现非租塞模式，pool.apply实现阻塞模式。 

apply_async和 apply函数，前者是非阻塞的，后者是阻塞。可以看出运行时间相差的倍数正是进程池数量。 

同时可以通过result.append(pool.apply_async(func, (msg, )))获取非租塞式调用结果信息的 



##  Python多线程原理与实现 

 Python多线程原理与实战 

目的： 

（1）了解python线程执行原理 

（2）掌握多线程编程与线程同步 

（3）了解线程池的使用 

###  1 线程基本概念 

####  1.1 线程是什么？  

 线程是指进程内的一个执行单元,也是进程内的可调度实体.  

 与进程的区别: (1) 地址空间:进程内的一个执行单元;进程至少有一个线程;它们共享进程的地址空间;而进程有自己独立 的地址空间; (2) 资源拥有:进程是资源分配和拥有的单位,同一个进程内的线程共享进程的资源 (3) 线程是CPU处理器调 度的基本单位,但进程不是. (4) 二者均可并发执行. 

 简而言之,一个程序至少有一个进程,一个进程至少有一个线程. 

 线程的划分尺度小于进程，使得多线程程序的并发性高。 另外，进程在执行过程中拥有独立的内存单元，而多个线 程共享内存，从而极大地提高了程序的运行效率。 

 #### 1.2 线程和进程关系？  

 进程就是一个应用程序在处理机上的一次执行过程，它是一个动态的概念，而线程是进程中的一部分，进程包含多个 线程在运行。 

 多线程可以共享全局变量，多进程不能。多线程中，所有子线程的进程号相同；多进程中，不同的子进程进程号不 同。  

 进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单 位. 线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上 不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其 他的线程共享进程所拥有的全部资源. 一个线程可以创建和撤销另一个线程;同一个进程中的多个线程之间可以并发执 行. 



###  2 Python线程模块  

 python主要是通过thread和threading这两个模块来实现多线程支持。python的thread模块是比较底层的模块， python的threading模块是对thread做了一些封装，可以更加方便的被使用。但是python（cpython）由于GIL的存 在无法使用threading充分利用CPU资源，如果想充分发挥多核CPU的计算能力需要使用multiprocessing模块 (Windows下使用会有诸多问题)。 

####  2.1 如何创建线程 

 python3.x中已经摒弃了Python2.x中采用函数式thread模块中的start_new_thread()函数来产生新线程方式。 

 python3.x中通过threading模块创建新的线程有两种方法：一种是通过threading.Thread(Target=executable Method)-即传递给Thread对象一个可执行方法（或对象）;第二种是继承threading.Thread定义子类并重写run()方 法。第二种方法中，唯一必须重写的方法是run(). 

 （1）通过threading.Thread进行创建多线程  

```python
import threading
import time

def target():
    print("the current threading %s is runing"
    	%(threading.current_thread().name))
	time.sleep(1)
	print("the current threading %s is ended"%(threading.current_thread().name))
    
print("the current threading %s is runing"%(threading.current_thread().name))
## 属于线程t的部分
t = threading.Thread(target=target)
t.start()
## 属于线程t的部分
t.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
print("the current threading %s is ended"%(threading.current_thread().name))

```

 （2）通过继承threading.Thread定义子类创建多线程 

 使用Threading模块创建线程，直接从threading.Thread继承，然后重写init方法和run方法： 

```python
import threading
import time

class myThread(threading.Thread): # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self): # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)
        
    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s process at: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
            
thread1 = myThread(1, "Thread-1", 1) # 创建新线程
thread2 = myThread(2, "Thread-2", 2)

thread1.start() # 开启线程
thread2.start()

thread1.join() # 等待线程结束
thread2.join()
print("Exiting Main Thread")


```

 通过以上案例可以知道，thread1和thread2执行顺序是乱序的。要使之有序，需要进行线程同步 



###  3 线程间同步 

 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同 步。 

 使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需 要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。  

 需要注意的是，Python有一个GIL（Global Interpreter Lock）机制，任何线程在运行之前必须获取这个全局锁才能 执行，每当执行完100条字节码，全局锁才会释放，切换到其他线程执行。 

####  3.1 线程同步问题 

 多线程实现同步有四种方式：   锁机制，信号量，条件判断和同步队列。 

 下面我主要关注两种同步机制：锁机制和同步队列。  

 （1）锁机制  

 threading的Lock类，用该类的acquire函数进行加锁，用realease函数进行解锁 

```python
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
    	print("Starting " + self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁
        threadLock.release()
        
    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
            
threadLock = threading.Lock()
threads = []
thread1 = myThread(1, "Thread-1", 1) # 创建新线程
thread2 = myThread(2, "Thread-2", 2)
thread1.start() # 开启新线程
thread2.start()
threads.append(thread1) # 添加线程到线程列表
threads.append(thread2)
for t in threads: # 等待所有线程完成
	t.join()
print("Exiting Main Thread")

```

 (2) 线程同步队列queue 

 python2.x中提供的Queue， Python3.x中提供的是queue 

 见import queue. 

 Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队 列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列 来实现线程间的同步。 

 queue模块中的常用方法: 

-  queue.qsize() 返回队列的大小 
- queue.empty() 如果队列为空，返回True,反之False 
- queue.full() 如果队列满了，返回True,反之False 
- queue.full 与 maxsize 大小对应 
- queue.get([block[, timeout]])获取队列，timeout等待时间 
- queue.get_nowait() 相当Queue.get(False)
-  queue.put(item) 写入队列，timeout等待时间 
- queue.put_nowait(item) 相当Queue.put(item, False) queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号 
- queue.join() 实际上意味着等到队列为空，再执行别的操作 

 案例1： 

```python
import queue
import threading
import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)
    
    def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print("%s processing %s" % (threadName, data))
            else:
                queueLock.release()
            time.sleep(1)
    
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
thread = myThread(threadID, tName, workQueue)
thread.start()
threads.append(thread)
threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
	pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

```

 案例2： 

```python
import time
import threading
import queue

class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start() #执行run()
    
    def run(self):
        #循环，保证接着跑下一个任务
        while True:
            # 队列为空则退出线程
            if self.queue.empty():
            	break
            # 获取一个队列数据
            foo = self.queue.get()
            # 延时1S模拟你要做的事情
            time.sleep(1)
            # 打印
            print(self.getName() + " process " + str(foo))
            # 任务完成
            self.queue.task_done()
    
# 队列
queue = queue.Queue()
# 加入100个任务队列
for i in range(100):
	queue.put(i)
# 开10个线程
for i in range(10):
    threadName = 'Thread' + str(i)
    Worker(threadName, queue)
# 所有线程执行完毕后关闭
queue.join()

```

### 4. 多线程的生产者消费者模式 

```python
from queue import Queue
import random, threading, time

# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    
    def run(self):
        for i in range(5):
            print("%s is producing %d to the queue!" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())
    
# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    
    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s is consuming. %d in the queue is consumed!" % (self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())
    
def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('All threads finished!')
    
if __name__ == '__main__':
	main()

```



###  5 线程池  

 传统多线程问题？  

 传统多线程方案会使用“即时创建， 即时销毁”的策略。尽管与创建进程相比，创建线程的时间已经大大的缩短，但是 如果提交给线程的任务是执行时间较短，而且执行次数极其频繁，那么服务器将处于不停的创建线程，销毁线程的状 态。  

 一个线程的运行时间可以分为3部分：线程的启动时间、线程体的运行时间和线程的销毁时间。在多线程处理的情景 中，如果线程不能被重用，就意味着每次创建都需要经过启动、销毁和运行3个过程。这必然会增加系统相应的时 间，降低了效率。 

 有没有一种高效的解决方案呢？ —— 线程池 

 线程池基本原理：  

 我们把任务放进队列中去，然后开N个线程，每个线程都去队列中取一个任务，执行完了之后告诉系统说我执行完 了，然后接着去队列中取下一个任务，直至队列中所有任务取空，退出线程。 

 使用线程池： 由于线程预先被创建并放入线程池中，同时处理完当前任务之后并不销毁而是被安排处理下一个任 务，因此能够避免多次创建线程，从而节省线程创建和销毁的开销，能带来更好的性能和系统稳定性。  

![](\img\企业微信截图_16709137128034.png)

####  线程池要设置为多少？ 

 服务器CPU核数有限，能够同时并发的线程数有限，并不是开得越多越好，以及线程切换是有开销的，如果线程切换 过于频繁，反而会使性能降低 

 线程执行过程中，计算时间分为两部分： 

-  CPU计算，占用CPU 
-  不需要CPU计算，不占用CPU，等待IO返回，比如recv(), accept(), sleep()等操作，具体操作就是比如 访问 cache、RPC调用下游service、访问DB，等需要网络调用的操作  

 那么如果计算时间占50%， 等待时间50%，那么为了利用率达到最高，可以开2个线程： 假如工作时间是2秒， CPU 计算完1秒后，线程等待IO的时候需要1秒，此时CPU空闲了，这时就可以切换到另外一个线程，让CPU工作1秒后， 线程等待IO需要1秒，此时CPU又可以切回去，第一个线程这时刚好完成了1秒的IO等待，可以让CPU继续工作，就 这样循环的在两个线程之前切换操作。 

 那么如果计算时间占20%， 等待时间80%，那么为了利用率达到最高，可以开5个线程： 可以想象成完成任务需要5 秒，CPU占用1秒，等待时间4秒，CPU在线程等待时，可以同时再激活4个线程，这样就把CPU和IO等待时间，最大 化的重叠起来 

 抽象一下，计算线程数设置的公式就是： N核服务器，通过执行业务的单线程分析出本地计算时间为x，等待时间为 y，则工作线程数（线程池线程数）设置为 N*(x+y)/x，能让CPU的利用率最大化。 由于有GIL的影响，python只能 使用到1个核，所以这里设置N=1  

```python
import queue
import threading
import time

class WorkManager(object):
    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = queue.Queue()
        self.threads = []
        self.__init_work_queue(work_num)
        self.__init_thread_pool(thread_num)
    """
    初始化线程
    """
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))
    
    """
    初始化工作队列
    """
    def __init_work_queue(self, jobs_num):
        for i in range(jobs_num):
            self.add_job(do_job, i)
            
    """
    添加一项工作入队
    """
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args))) # 任务入队，Queue内部实现了同步机制
        
    """
    等待所有线程运行完毕
    """
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive(): item.join()
                
    class Work(threading.Thread):
        def __init__(self, work_queue):
            threading.Thread.__init__(self)
            self.work_queue = work_queue
            self.start()
        def run(self):
            # 死循环，从而让创建的线程在一定条件下关闭退出
            while True:
                try:
                    do, args = self.work_queue.get(block=False) # 任务异步出队，Queue内部实现了同步机制
                    do(args)
                    self.work_queue.task_done() # 通知系统任务完成
                except:
                    break
                    # 具体要做的任务
                    
    def do_job(args):
        time.sleep(0.1) # 模拟处理时间
        print(threading.current_thread())
        print(list(args))
    
if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager(100, 10) # 或者work_manager = WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print("cost all time: %s" % (end - start))

```



###  6. python 进行并发编程 

 在Python 2的时代，高性能的网络编程主要是使用Twisted、Tornado和Gevent这三个库，但是它们的异步代码相互 之间既不兼容也不能移植。 asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。 

 asyncio 的编程模型就是一个消息循环。我们从 asyncio 模块中直接获取一个 EventLoop 的引用，然后把需要执行 的协程扔到 EventLoop 中执行，就实现了异步IO。  

 Python的在3.4中引入了协程的概念，可是这个还是以生成器对象为基础。 Python 3.5添加了async和await这两个关键字，分别用来替换 asyncio.coroutine 和 yield from 。  

 python3.5则确定了协程的语法。下面将简单介绍asyncio的使用。实现协程的不仅仅是asyncio，tornado和gevent 都实现了类似的功能。 

 （1）协程定义 

 用 asyncio 实现 Hello world 代码如下：  

```python
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")
    
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
```

 @asyncio.coroutine 把一个generator标记为coroutine类型，然后，我们就把这个 coroutine 扔到 EventLoop 中执行。 hello() 会首先打印出 Hello world! ，然后， yield from 语法可以让我们方便地调用另一个 generator 。由于 asyncio.sleep() 也是一个 coroutine ，所以线程不会等待 asyncio.sleep() ，而是直接中断并执行下一个消息 循环。当 asyncio.sleep() 返回时，线程就可以从 yield from 拿到返回值（此处是 None ），然后接着执行下一行 语句。 

 把 asyncio.sleep(1) 看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行 EventLoop 中其他可 以执行的 coroutine 了，因此可以实现并发执行。 

 我们用Task封装两个 coroutine 试试： 

```python
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
    
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

```

 观察执行过程： 

```python
Hello world! (<_MainThread(MainThread, started 140735195337472)>)
Hello world! (<_MainThread(MainThread, started 140735195337472)>)
(暂停约1秒)
Hello again! (<_MainThread(MainThread, started 140735195337472)>)
Hello again! (<_MainThread(MainThread, started 140735195337472)>)

```

 由打印的当前线程名称可以看出，两个 coroutine 是由同一个线程并发执行的。 

 如果把 asyncio.sleep() 换成真正的IO操作，则多个 coroutine 就可以由一个线程并发执行。 

 asyncio案例实战 

 我们用 asyncio 的异步网络连接来获取sina、sohu和163的网站首页： 

 async_wget.py 

```python
import asyncio

    @asyncio.coroutine
    def wget(host):
        print('wget %s...' % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = yield from connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        yield from writer.drain()
        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
            	break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
         # Ignore the body, close the socket
         writer.close()
        
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

 结果信息如下： 

```
wget www.sohu.com...
wget www.sina.com.cn...
wget www.163.com...
(等待一段时间)
(打印出sohu的header)
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html
...
(打印出sina的header)
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Date: Wed, 20 May 2015 04:56:33 GMT
...
(打印出163的header)
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
...
```

 可见3个连接由一个线程通过 coroutine 并发完成。 

 #### 小结  

asyncio 提供了完善的异步IO支持； 

异步操作需要在 coroutine 中通过 yield from 完成； 

多个 coroutine 可以封装成一组Task然后并发执行。 

## subprocess 

 **运行一个进程**

> 运行python的时候，我们都是在创建并运行一个进程。像Linux进程那样，一个进程可以fork一个子进程，并 让这个子进程exec另外一个程序。在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运 行一个外部的程序。 

  subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来 从中选取一个使用。 

####  1. subprocess.call()  

 函数格式如下： 

```python
call(*popenargs, timeout=None, **kwargs):
    """Run command with arguments. Wait for command to complete or
    timeout, then return the returncode attribute.
    
    The arguments are the same as for the Popen constructor. Example:
    
    retcode = call(["ls", "-l"])
```

 父进程等待子进程完成 返回退出信息(returncode，相当于Linux exit code)  

```
>>> import subprocess
>>> retcode = subprocess.call(["ls", "-l"])
#和shell中命令ls -a显示结果一样
>>> print retcode
0

```

 或者是  

```
>>> a = subprocess.call(['df','-hT'],shell=False)
Filesystem Type Size Used Avail Use% Mounted on
/dev/sda2 ext4 94G 64G 26G 72% /
tmpfs tmpfs 2.8G 0 2.8G 0% /dev/shm
/dev/sda1 ext4 976M 56M 853M 7% /boot

```

 subprocess.check_call()：用法与subprocess.call()类似，区别是，当返回值不为0时，直接抛出异常 

```
>>> a = subprocess.check_call('df -hT',shell=True)
Filesystem Type Size Used Avail Use% Mounted on
/dev/sda2 ext4 94G 64G 26G 72% /
tmpfs tmpfs 2.8G 0 2.8G 0% /dev/shm
/dev/sda1 ext4 976M 56M 853M 7% /boot
>>> print a
0
>>> a = subprocess.check_call('dfdsf',shell=True)
/bin/sh: dfdsf: command not found
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/lib64/python2.6/subprocess.py", line 502, in check_call
raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'dfdsf' returned non-zero exit status 127
```

####  2. subprocess.Popen() 

> 在一些复杂场景中，我们需要将一个进程的执行输出作为另一个进程的输入。在另一些场景中，我们需要先进 入到某个输入环境，然后再执行一系列的指令等。这个时候我们就需要使用到suprocess的Popen()方法。 

 函数形式如下： 

```python
class Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None,
preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None,
universal_newlines=False, startupinfo=None, creationflags=0)
```

 Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞 block) 

```python
import subprocess

if __name__ == "__main__":
    child = subprocess.Popen('ping -c www.baidu.com', shell=True)
    child.wait()
    print('parent process')

```

 父进程在开启子进程之后并等待child的完成后，再运行print。 此外，你还可以在父进程中对子进程进行其它操作， 比如我们上面例子中的child对象:代码如下: 

 child.poll() # 检查子进程状态 child.kill() # 终止子进程 child.send_signal() # 向子进程发送信号 child.terminate() # 终止子进程  

 子进程的标准输入、标准输出和标准错误， 如下属性分别表示: child.stdin child.stdout child.stderr 

 示例，将一个子进程的输出，作为另一个子进程的输入： 

```python
import subprocess

child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["grep","0:0"],stdin=child1.stdout, stdout=subprocess.PIPE)
out = child2.communicate()
```

 案例分析：  

 在工作中经常会遇到这样的需求： 

 需要采用python来运行一个shell脚本，如何优雅的操作呢？ 

 解决方案： 

 用python的subprocess去执行传递过来的脚本，通常情况下subprocess都能运行的很好，完成脚本的执行并返回。 

 可以采用如下代码实现： 

```python
import subprocess
from threading import Timer
import os
import time
import signal

class TestSubProcess(object):
    def __init__(self):
        self.stdout = []
        self.stderr = []
        self.timeout = 6
        self.is_timeout = False
    
    def timeout_callback(self, p):
    	print('exe time out call back')
        try:
            p.kill()
            # os.killpg(p.pid, signal.SIGKILL)
        except Exception as error:
        	print(error)
            
    def run(self):
        stdout = open('/tmp/subprocess_stdout', 'wb')
        stderr = open('/tmp/subprocess_stderr', 'wb')
        cmd = ['bash', '/home/xxx/while_test.sh']
        ps = subprocess.Popen(cmd, stdout=stdout.fileno(), stderr=stderr.fileno())
        my_timer = Timer(self.timeout, self.timeout_callback, [ps])
        my_timer.start()
        print(ps.pid)
        try:
            print("start to count timeout; timeout set to be %d \n" % (self.timeout,))
            ps.wait()
        finally:
            my_timer.cancel()
            stdout.flush()
            stderr.flush()
            stdout.close()
            stderr.close()
        
if __name__ == "__main__":
    tsp = TestSubProcess()
    tsp.run()

```

 总结： 

 关于p = subprocess.Popen，最好用p.communicate.而不是直接用p.wait()， 因为p.wait()有可能因为子进程往PIPE 写的时候写满了，但是子进程还没有结束，导致子进程阻塞，而父进程一直在wait()，导致父进程阻塞。而且p.wait() 和p.communicate不能一起用，因为p.communicate里面也会去调用wait()。 



## 扩展-同步与异步

 在实际项目开发过程中，经常会存在同步和异步，阻塞和非阻塞的概念 

 同步： 

一个服务的完成需要依赖其他服务时，只有等待被依赖的服务完成后，才算完成，这是一种可靠的服务序列。要么成 功都成功，失败都失败，服务的状态可以保持一致 

 异步： 

一个服务的完成需要依赖其他服务时，只通知其他依赖服务开始执行，而不需要等待被依赖的服务完成，此时该服务 就算完成了。被依赖的服务是否最终完成无法确定，是一个不可靠的服务序列。  

 场景比喻： 

 小明去买奶茶，可能会有两种方式 

- 3.1、小明点单交钱，然后等着取奶茶； 
- 3.2、小明点单交钱，然后奶茶妹给了小明一个小票，等小明的奶茶做好了，再告诉小明来取； 
- 第一种方式就是同步，就等着奶茶妹做好奶茶，奶茶做好之后，小明拿到奶茶才算完成整个任务 
- 第二种方式就是异步，奶茶妹给了小明一个小票，小明就算完成了。至于最后奶茶做好没有，反正奶茶妹会告 诉小明的，那是后面的事情了。 

 所以： 同步与异步着重点在消息通知的方式，也就是调用结果通知的方式。 

 阻塞： 

阻塞调用是指调用结果返回之前，当前线程会被挂起，一直处于等待消息通知，不能够执行其他业务,函数只有在得 到结果之后才会返回。 

 进程的5种状态： 

一个线程/进程经历的5个状态，创建，就绪，运行，阻塞，终止。各个状态的转换条件如上图，其中有个阻塞状态， 就是说当线程中调用某个函数，需要IO请求，或者暂时得不到竞争资源的，操作系统会把该线程阻塞起来，避免浪费 CPU资源，等到得到了资源，再变成就绪状态，等待CPU调度运行。  

![](\img\企业微信截图_16709149346701.png)

 创建状态：进程在创建时需要申请一个空白PCB，向其中填写控制和管理进程的信息，完成资源分配。如 果创建工作 无法完成，比如资源无法满足，就无法被调度运行，把此时进程所处状态称为创建状态 

 就绪状态：进程已经准备好，已分配到所需资源，只要分配到CPU就能够立即运行 

 执行状态：进程处于就绪状态被调度后，进程进入执行状态 

 阻塞状态：正在执行的进程由于某些事件（I/O请求，申请缓存区失败）而暂时无法运行，进程受到阻塞。在满足请 求时进入就绪状态等待系统调用 

 终止状态：进程结束，或出现错误，或被系统终止，进入终止状态。无法再执行 

 非阻塞：  

 非阻塞和阻塞的概念相对应，指在不能立刻得到结果之前，该函数不会阻塞当前线程，而会立刻返回。 

 阻塞和非阻塞  

   阻塞和非阻塞这两个概念与程序（线程）等待消息通知(无所谓同步或者异步)时的状态有关。也就是说阻塞与非阻塞 主要是程序（线程）等待消息通知时的状态角度来说的。 

 同步/异步关注的是消息通知的机制，而阻塞/非阻塞关注的是程序（线程）等待消息通知时的状态 

 网络IO处理阻塞非租塞，同步和异步关系 

 在处理 IO 的时候，阻塞和非阻塞都是同步 IO。只有使用了特殊的 API 才是异步 IO。  

![](\img\企业微信截图_16709150403749.png)

 并发与并行 

 并发和并行一直是容易混淆的概念。并发通常指有多个任务需要同时进行，并行则是同一时刻有多个任务执行。用上 课来举例就是，并发情况下是一个老师在同一时间段辅助不同的人功课。并行则是好几个老师分别同时辅助多个学生 功课。简而言之就是一个人同时吃三个馒头还是三个人同时分别吃一个的情况，吃一个馒头算一个任务。  

  生活中的近似例子： 

边玩游戏边吃饭 #并发，交替执行 

同时操作2个英雄 #并发，交替操作两个英雄 

并行：绝对的同时进行  



##  网络编程基础 

###  一. 网络模型 

> 网络编程最主要的工作就是在发送端把信息通过规定好的协议进行组装包，在接收端按照规定好的协议把包进 行解析，从而提取出对应的信息，达到通信的目的。 

 作为一个 开发程序员，知道网络到底是怎么进行通信的，怎么进行工作的，为什么服务器能够接收到请求，做出响 应。这些原理应该是每个程序员应该了解的。 

####  1.历史及起源 

 网络模型不是一开始就有的，在网络刚发展时，网络协议是由各互联网公司自己定义的，比如那时的巨头网络公司 IBM、微软、苹果、思科等等，他们每家公司都有自己的网络协议，各家的协议也是不能互通的，那时候大家觉得这 是可以的，但对消费者来说这实际上是技术垄断，因为你买了苹果的设备就不能用微软的设备，因为他们的协议不是 一样的，没有统一的标准来规范网络协议，都是这些公司的私有协议。 

####  2. 网络模型与协议 

#####  2.1 TCP/IP协议 

 TCP/IP(Transmission Control Protocal/Internet Protocal，传输控制协议/网间网协议)是目前世界上应用最为广泛的 网络通信协议，它的流行与Internet的迅猛发展密切相关。TCP/IP最初是为互联网的原型ARPANET所设计的，目的是 提供一整套方便实用、能应用于多种网络上的协议，事实证明TCP/IP做到了这一点，它使网络互联变得容易起来，并 且使越来越多的网络加入其中，成为Internet的事实标准。日常生活中的大部分网络应用（如浏览网页、收发电子邮 件、QQ聊天）都是基于该系列协议。 

 为了减少协议设计的复杂性，大多数网络模型都是按层的方式来组织的。在分层网络模型中，每一层都为上一层提供 一定的服务，而把如何实现本层服务的细节对上一层加以屏蔽。上层只需要知道下层提供了什么功能以及对应于这些 功能的接口，而不必关心下一层如何实现这些功能。  

#####  2.2 OSI 模型和TCP/IP模型的对比  

 开放系统互连参考模型为实现开放系统互连所建立的通信功能分层模型，简称OSI模型。 

 其目的是为异种计算机互连提供一个共同的基础和标准框架，并为保持相关标准的一致性和兼容性提供共同的参考。 

 但是由于种种原因，OSI模型始终没有得到广泛应用，当前普遍使用的是TCP/IP模型。  

 几乎所有的互联网设备都支持TCP/IP协议。TCP/IP协议已经成为事实上的国际标准和工业标准。 

![](\img\企业微信截图_1671175397730.png)

#####  2.3 TCP/IP各层功能 

######  （1）应用层：  

 应用层是所有用户所面向的应用程序的统称。ICP/IP协议族在这一层面有着很多协议来支持不同的应用，许多大家所 熟悉的基于Internet的应用的实现就离不开这些协议。如我们进行万维网（WWW）访问用到了HTTP协议（超文本传 输协议）、文件传输用FTP协议、电子邮件发送用SMTP（简单邮件传输协议）、域名的解析用DNS协议、远程登录 用Telnet协议等等，还有近几年来十分流行的点对点共享文件协议，即BitTorrent协议，该协议基于HTTP协议。使用 该协议构建的BT下载工具有比特精灵、BitTorrent等，都是属于TCP/IP应用层的；就用户而言，看到的是由一个个软 件所构筑的大多为图形化的操作界面，而实际后台运行的便是上述协议。 

######  （2）传输层：  

 传输层通过位于该层的TCP协议（传输控制协议）或UDP协议（用户数据报协议）在两台主机间传输数据。其中TCP 协议提供可靠的面向连接的服务，它保证数据能完整地按顺序地传送到目标计算机。它在传输数据前首先需要和目的 计算机建立连接，并且在数据传输过程中维持此链接，因此在速度上会有些损失。UDP提供简单的无连接服务，它不 保证数据能按顺序、正确地传送到目的地（但可由他的上层来保证），它不用建立连接，通常速度上要比TCP快些。 TCP协议和IP协议都需要网络层提供通往目的地的路由。传输层提供端到端，即应用程序之间的通信。该层的主要功 能有差错控制、传输确认和丢失重传等。 

######  （3）网络层： 

 网络层是TCP/IP协议族中非常关键的一层，主要定义了IP地址格式，从而能够使得不同应用类型的数据在Internet上 通畅地传输，IP协议就是一个网络层协议。  

 网络层负责在发送端和接收端之间建立一条虚拟路径。IP协议并不保证数据能完整正确的到达目的地，这个任务由他 上面的传输层来完成。这一层的ARP协议（地址解析协议）和RARP协议（反向地址解析协议）用于IP地址和物理地 址（通常就是网卡地址）的相互转换。如果数据在传输过程中出现问题，该层的ICMP协议将生产错误报文。  

######  （4）网络接口层： 

 这是TCP/IP软件的最低层，它包括多种逻辑链路控制盒媒体访问协议。负责将网络层发送来的数据分成帧，并通过物 理链路进行传送，或从网络上接收物理帧，抽取数据并转交给其上的网络层 

![](\img\企业微信截图_16711755342618.png)

#####  2.4. ISO模型各层的功能 

######  （1）应用层： 

 指网络操作系统和具体的应用程序，对应WWW服务器、FTP服务器等应用软件。术语“应用层”并不是指运行在网络上 的某个特别应用程序，而是提供了一组方便程序开发者在自己的应用程序中使用网络功能的服务。应用层提供的服务 包括文件传输（FTP）、文件管理以及电子邮件的信息处理（SMTP）等。  

######  （2）表示层： 

 内码转换、压缩与解压缩、加密与解密,充当应用程序和网络之间的“翻译官”角色。在表示层，数据将按照网络能理解 的方案进行格式化；这种格式化也因所使用网络的类型不同而不同。例如，IBM主机使用EBCDIC编码，而大部分PC 机使用的是ASCII码。在这种情况下，便需要会话层来完成这种转换。表示层协议还对图片和文件格式信息进行解码 和编码。表示层管理数据的解密与加密，如系统口令的处理。如果在Internet 上查询你银行账户，使用的即是一种安 全连接。  

######  （3）会话层 

 负责在网络中的两节点之间建立和维持通信。功能包括：建立通信链接，保持会话过程通信链接的畅通，同步两个节 点之间的对话，决定通信是否被中断以及通信中断时决定从何处重新发送 例：使用全双工模式或半双工模式，如何 发起传输，如何结束传输，如何设定传输参数。会话层通过决定节点通信的优先级和通信时间的长短来设置通信期 限。  

######  （4）传输层：  

 编定序号、控制数据流量、查错与错误处理，确保数据可靠、顺序、无错地从A点到传输到B 点。因为如果没有传输 层，数据将不能被接受方验证或解释，所以，传输层常被认为是O S I 模型中最重要的一层。传输协议同时进行流量 控制或是基于接收方可接收数据的快慢程度规定适当的发送速率。传输层按照网络能处理的最大尺寸将较长的数据包 进行强制分割并编号。例如：以太网无法接收大于1 5 0 0 字节的数据包。发送方节点的传输层将数据分割成较小的 数据片，同时对每一数据片安排一序列号，以便数据到达接收方节点的传输层时，能以正确的顺序重组。该过程即被 称为排序。在网络中，传输层发送一个A C K （应答）信号以通知发送方数据已被正确接收。如果数据有错或者数据 在一给定时间段未被应答，传输层将请求发送方重新发送数据。  

######  （5）网络层： 

 定址、选择传送路径。网络层通过综合考虑发送优先权、网络拥塞程度、服务质量以及可选路由的花费来决定从一个 网络中节点A 到另一个网络中节点B 的最佳路径。在网络中，“路由”是基于编址方案、使用模式以及可达性来指引数 据的发送。网络层协议还能补偿数据发送、传输以及接收的设备能力的不平衡性。为完成这一任务，网络层对数据包 进行分段和重组。分段和重组 是指当数据从一个能处理较大数据单元的网络段传送到仅能处理较小数据单元的网络 段时，网络层减小数据单元的大小的过程。重组是重构被分段的数据单元。 

######  （6）数据链路层： 

 同步、查错、制定MAC方法。它的主要功能是将从网络层接收到的数据分割成特定的可被物理层传输的帧。帧 (Frame)是用来移动数据的结构包，它不仅包括原始（未加工）数据，或称“有效荷载”，还包括发送方和接收方的网 络地址以及纠错和控制信息。其中的地址确定了帧将发送到何处，而纠错和控制信息则确保帧无差错到达。通常，发 送方的数据链路层将等待来自接收方对数据已正确接收的应答信号。数据链路层控制信息流量，以允许网络接口卡正 确处理数据。数据链路层的功能独立于网络和它的节点所采用的物理层类型。 

######  （7）物理层： 

 传输信息的介质规格、将数据以实体呈现并传输的规格、接头规格。该层包括物理连网媒介，如电缆连线、连接器、 网卡等。物理层的协议产生并检测电压以便发送和接收携带数据的信号。尽管物理层不提供纠错服务，但它能够设定 数据传输速率并监测数 例：在你的桌面P C 上插入网络接口卡，你就建立了计算机连网的基础。换言之，你提供了 一个物理层。 



###  二. 网络套接字  

> 套接字是通信的基石，是支持TCP/IP协议的网络通信的基本操作单元。可以将套接字看作 不同主机间的进程进 行双向通信的端点，它构成了单个主机内及整个网络间的编程界面。套接 字存在于通信域中，通信域是为了处 理一般的线程通过套接字通信而引进的一种抽象概念。  
>
>  套 接字通常和同一个域中的套接字交换数据（数据交换也可能穿越域的界限，但这时一定要执行 某种解释程 序）。各种进程使用这个相同的域互相之间用Internet协议簇来进行通信。  

 四元组：（源IP，源端口，目的IP，目的端口） 

####  1. 套接字工作原理 

1.  要通过互联网进行通信，你至少需要一对套接字，其中一个运行于客户机端，我们称之为 ClientSocket，另一 个运行于服务器端，我们称之为ServerSocket。 
2.  根据连接启动的方式以及本地套接字要连接的目标，套接字之间的连接过程可以分为三个 步骤：服务器监听， 客户端请求，连接确认。  
3.  所谓服务器监听，是服务器端套接字并不定位具体的客户端套接字，而是处于等待连接的 状态，实时监控网络 状态。  
4.  所谓客户端请求，是指由客户端的套接字提出连接请求，要连接的目标是服务器端的套接 字。为此，客户端的 套接字必须首先描述它要连接的服务器的套接字，指出服务器端套接字的 地址和端口号，然后就向服务器端套 接字提出连接请求。 
5.  所谓连接确认，是指当服务器端套接字监听到或者说接收到客户端套接字的连接请求，它 就响应客户端套接字 的请求，建立一个新的线程，把服务器端套接字的描述发给客户端，一旦 客户端确认了此描述，连接就建立好 了。而服务器端套接字继续处于监听状态，继续接收其他 客户端套接字的连接请求。 

#### 2. TCP和UDP网络通信过程 

1.  TCP通信过程  

   ![](\img\企业微信截图_16711757862548.png)

   

2.  UDP通信过程 

   ![](\img\企业微信截图_16711758209462.png)

###  三. UDP 和 TCP 的区别 

|            | TCP            | UDP        |
| ---------- | -------------- | ---------- |
| 连接性     | 面向连接       | 面向无连接 |
| 传输可靠性 | 可靠           | 不可靠     |
| 传输模式   | 流             | 数据报     |
| 应用场景   | 传输大量的数据 | 少量数据   |
| 速度       | 慢             | 快         |



####  TCP： 

 TCP 的可靠体现在传输数据之前，会有三次握手来建立连接。在数据传完后，还会断开连接用来节约系统资源。在数 据传递时，有确认机制、重传机制、拥塞控制机制以保证传输的可靠性，但这些机制都会消耗大量的时间和系统资 源，每个连接都会占用系统的 CPU、内存等硬件资源，所以也导致 TCP 容易被人利用，比如 DDOS、CC 等攻击。  

 一般用于文件传输、收发邮件或远程登录等对数据准确性要求高的场景。 

####  UDP：  

 UDP 没有 TCP 那些可靠的机制，所以在数据传递时，如果网络质量不好，就会很容易丢包。但 UDP 也是无法避免 攻击的，比如：UDP Flood 攻击。  

 一般用于即时通讯、在线视频、网络电话等对传输效率要求高，但对准确性要求相对低的场景。 



###  四. TCP 的三次握手和四次挥手 

####  TCP三次握手  

 所谓三次握手(Three-way Handshake)，是指建立一个TCP连接时，需要客户端和服务器总共发送3个包。 

 三次握手的目的是连接服务器指定端口，建立TCP连接,并同步连接双方的序列号和确认号并交换 TCP 窗口大小信息. 在socket编程中，客户端执行connect()时。将触发三次握手。 

![](\img\企业微信截图_16711762051977.png)

####  TCP 四次挥手

 TCP 四次挥手 TCP的连接的拆除需要发送四个包，因此称为四次挥手(four-way handshake)。客户端或服务器均可 主动发起挥手动作，在socket编程中，任何一方执行close()操作即可产生挥手操作。  

![](\img\企业微信截图_16711763668025.png)

 扩展：  

 TIME_WAIT状态所带来的影响： 

 当某个连接的一端处于TIME_WAIT状态时，该连接将不能再被使用。事实上，对于我们比较有现实意义的是，这个端 口将不能再被使用。某个端口处于TIME_WAIT状态(其实应该是这个连接)时，这意味着这个TCP连接并没有断开(完全 断开)，那么，如果你bind这个端口，就会失败。对于服务器而言，如果服务器突然crash掉了，那么它将无法再 2MSL内重新启动，因为bind会失败。解决这个问题的一个方法就是设置socket的SO_REUSEADDR选项。这个选项意 味着你可以重用一个地址。 



##  Python 进行网络编程 

###  1. Python TCP通信实现 

#### socket()函数

 Python 中，我们用 socket（）函数来创建套接字，语法格式如下：  

```
socket.socket([family[, type[, proto]]])
```

**参数**

-  family: 套接字家族可以使AF_UNIX或者AF_INET 
- type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM 
- protocol: 一般不填默认为0. 

**注：**

 socket只能发送字节类型的数据 所以在发送时要将发送的数据通过str.encode() 转为字节类型，接收时在通过 str.decode()转为字符串。 

#### Socket 对象(内建)方法 

| 函数                                 | 描述                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| 服务器端套接字                       |                                                              |
| s.bind()                             | 绑定地址（host,port）到套接字， 在AF_INET下,以元组 （host,port）的形式表示地址。 |
| s.listen()                           | 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的 最大连接数量。该值至少为1，大部分应用程序设为5就可以了。 |
| s.accept()                           | 被动接受TCP客户端连接,(阻塞式)等待连接的到来                 |
| 客户端套接字                         |                                                              |
| s.connect()                          | 主动初始化TCP服务器连接，一般address的格式为元组 （hostname,port），如果连接出错，返回socket.error错误。 |
| s.connect_ex()                       | connect()函数的扩展版本,出错时返回出错码,而不是抛出异常      |
| 公共用途的套接字函数                 |                                                              |
| s.recv()                             | 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大 数据量。flag提供有关消息的其他信息，通常可以忽略。 |
| s.send()                             | 发送TCP数据，将string中的数据发送到连接的套接字。返回值是要 发送的字节数量，该数量可能小于string的字节大小。 |
| s.sendall()                          | 完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连 接的套接字，但在返回之前会尝试发送所有数据。成功返回None， 失败则抛出异常。 |
| s.recvfrom()                         | 接收UDP数据，与recv()类似，但返回值是（data,address）。其中 data是包含接收数据的字符串，address是发送数据的套接字地址。 |
| s.sendto()                           | 发送UDP数据，将数据发送到套接字，address是形式为（ipaddr， port）的元组，指定远程地址。返回值是发送的字节数。 |
| s.close()                            | 关闭套接字                                                   |
| s.getpeername()                      | 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。  |
| s.getsockname()                      | 返回套接字自己的地址。通常是一个元组(ipaddr,port)            |
| s.setsockopt(level,optname,value)    | 设置给定套接字选项的值。                                     |
| s.getsockopt(level,optname[.buflen]) | 返回套接字选项的值。                                         |
| s.settimeout(timeout)                | 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为 None表示没有超时期。一般，超时期应该在刚创建套接字时设置， 因为它们可能用于连接的操作（如connect()） |
| s.gettimeout()                       | 返回当前超时期的值，单位是秒，如果没有设置超时期，则返回 None。 |
| s.fileno()                           | 返回套接字的文件描述符。                                     |
| s.setblocking(flag)                  | 如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞 模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数 据，或send()调用无法立即发送数据，那么将引起socket.error异 常。 |
| s.makefile()                         | 创建一个与该套接字相关连的文件                               |

#### socket异常 

| Exception       | 解释                                                   |
| --------------- | ------------------------------------------------------ |
| socket.error    | 由Socket相关错误引发                                   |
| socket.herror   | 由地址相关错误引发                                     |
| socket.gaierror | 由地址相关错误，如getaddrinfo()或getnameinfo()引发     |
| socket.timeout  | 当socket出现超时时引发。超时时间由settimeout()提前设定 |

####  交互过程 

##### TCP服务端： 

###### 1 创建套接字，绑定套接字到本地IP与端口 

> s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)，s.bind()  

###### 2 开始监听连接  

> s.listen() 

###### 3 进入循环，不断接受客户端的连接请求 

> s.accept() 

###### 4 然后接收传来的数据，并发送给对方数据 

> s.recv() , s.send() 

###### 5 传输完毕后，关闭套接 

> s.close()  



##### TCP客户端: 

######  1 创建套接字，连接远端地址 

> socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect() 

######  2 连接后发送数据和接收数据  

> s.send(), s.recv() 

######  3 传输完毕后，关闭套接字 

> s.close() 



###  2. TCP协议的Python实现 

 服务器端：  

```python
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM) ##创建服务器TCP套接字
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept() ##等待客户端连接
    print('...connected from:', addr)    
    while True:
        data = tcpCliSock.recv(BUFSIZ) ##监听客户端是否发送消息
        print(data)
        if not data:
            break
        
tcpCliSock.send(data)
tcpCliSock.close()
tcpSerSock.close()
```

 客户端代码： 

```python
from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) ##创建客户端TCP套接字
tcpCliSock.connect(ADDR) ##连接服务器
while True:
    data = input('> ')
    if not data:
    	break
    tcpCliSock.send(data.encode(encoding='utf8'))
    data = tcpCliSock.recv(BUFSIZ) ##监听客户端发送消息
    if not data:
    	break
    print(data)
tcpCliSock.close()
```

###  3. Python UDP通信实现 

> UDP则是面向无连接的协议。 
>
> 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能 到达就不知道了。 
>
> 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP 协议。 

 服务器端代码： 

```python
import socket
'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道
了。
虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口
绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
'''
# ipv4 SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定 客户端口和地址:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据 自动阻塞 等待客户端请求:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto('Hello, %s!' % data, addr)
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。

```

 客户端代码 

```python
import socket
'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数
据：
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in ['python', 'java', 'c']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024))
s.close()
```



##  Select， Poll，Epoll 

###  1. Select 

 select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回 后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操 作。  

 select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多 的优点之一。 

 select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过 修改宏定义甚至重新编译内核的方式提升这一限制。 

 另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。 同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫 描，所以这也浪费了一定的开销。  

 Select是一种线性扫描方式处理 

 在python中，select函数是一个对底层操作系统的直接访问的接口。它用来监控sockets、files和pipes，等待IO完成 （Waiting for I/O completion）。当有可读、可写或是异常事件产生时，select可以很容易的监控到。  

 在python中，select函数是一个对底层操作系统的直接访问的接口。它用来监控sockets、files和pipes，等待IO完成 （Waiting for I/O completion）。当有可读、可写或是异常事件产生时，select可以很容易的监控到。  

###  2. Poll 

 poll在1986年诞生于System V Release 3，它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的 限制。 

 poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不 论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。 

 另外，select()和poll()将就绪的文件描述符告诉进程后，如果进程没有对其进行IO操作，那么下次调用select()和 poll()的时候将再次报告这些文件描述符，所以它们一般不会丢失就绪的消息，这种方式称为水平触发（Level Triggered）。  

###   3. Epoll  

 直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为 Linux2.6下性能最好的多路I/O就绪通知方法。 

 直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为 Linux2.6下性能最好的多路I/O就绪通知方法。 

 直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为 Linux2.6下性能最好的多路I/O就绪通知方法。 

 另一个本质的改进在于epoll采用基于事件的就绪通知方式。在select/poll中，进程只有在调用一定的方法后，内核才 对所有监视的文件描述符进行扫描，而epoll事先通过epoll_ctl()来注册一个文件描述符，一旦基于某个文件描述符就 绪时，内核会采用类似callback的回调机制，迅速激活这个文件描述符，当进程调用epoll_wait()时便得到通知。 

###  使用 select 

 在python中，select函数是一个对底层操作系统的直接访问的接口。它用来监控sockets、files和pipes，等待IO完成 （Waiting for I/O completion）。当有可读、可写或是异常事件产生时，select可以很容易的监控到。 select.select（rlist, wlist, xlist[, timeout]） 传递三个参数，一个为输入而观察的文件对象列表，一个为输出而观察 的文件对象列表和一个观察错误异常的文件列表。第四个是一个可选参数，表示超时秒数。其返回3个tuple，每个 tuple都是一个准备好的对象列表，它和前边的参数是一样的顺序。 

**当我们调用select()时： **

1、上下文切换转换为内核态 

2、将fd从用户空间复制到内核空间 

3、内核遍历所有fd，查看其对应事件是否发生 

4、如果没发生，将进程阻塞，当设备驱动产生中断或者timeout时间后，将进程唤醒，再次进行遍历 

5、返回遍历后的fd 

6、将fd从内核空间复制到用户空间  

```
通过socket建立网络连接的步骤:
至少需要2个套接字, server和client
需要建立socket之间的连接, 通过连接来进行收发data
client 和 server连接的过程:
1. 建立server的套接字,绑定主机和端口,并监听client的连接请求
2. client套接字根据server的地址发出连接请求, 连接到server的socket上; client socket需要提供自己的
socket fd,以便server socket回应
3. 当server监听到client连接请求时, 响应请求, 建立一个新的线程, 把server fd 发送给client
而后, server继续监听其他client请求, 而client和server通过socket连接互发data通信
```

**select方法 **

 fd_r_list, fd_w_list, fd_e_list ``= select.select(rlist, wlist, xlist, [timeout]) 

 参数： 可接受四个参数（前三个必须） 

- rlist: wait until ready for reading 
- wlist: wait until ready for writing 
- xlist: wait for an “exceptional condition” 
- timeout: 超时时间 

 返回值：三个列表  

 fd_r_list： 读列表， fd_w_list：写列表， fd_e_list ：异常列表  

###  4. 案例分析  

 服务器端代码： 

```python
import socket, select, threading
host = socket.gethostname()
port = 5963
addr = (host, port)

inputs = []
fd_name = {}
def who_in_room(w):
    name_list = []
    for k in w:
    	name_list.append(w[k])
    return name_list

def conn():
    print('wait connecting...')
    ss = socket.socket()
    ss.bind(addr)
    ss.listen(5)
    return ss

def new_coming(ss):
    client, add = ss.accept()
    print('欢迎 %s %s' % (client, add))
    wel = '''聊天室，请输入您的名称:'''
    try:
        client.send(wel.encode(encoding='utf8'))
        name = client.recv(1024).decode(encoding='utf8')
        inputs.append(client)
        fd_name[client] = name
        nameList = "当前聊天室内，有如下成员： %s" % (who_in_room(fd_name))
        client.send(nameList.encode(encoding='utf8'))
    except Exception as e:
    	print(e)

def server_run():
    ss = conn()
    inputs.append(ss)
    
    while True:
        rList, wList, eList = select.select(inputs, [], [])
        for temp in rList:
            if temp is ss:
            	new_coming(ss)
            else:
                disconnect = False
                try:
                    data = temp.recv(1024) #bytes
                    data = data.decode(encoding='utf8') #str
                    user_name = fd_name[temp] #bytes
                    data = user_name + ' say : ' + data
                    #data = data.decode('utf8')
                except socket.error:
                    data = fd_name[temp] + ' leave the room'
                    disconnect = True
                if disconnect:
                    inputs.remove(temp)
                    print(f"disconnect message:{data}")
                    for other in inputs:
                        if other != ss and other != temp:
                        try:
                            other.send(data.encode(encoding='utf8'))
                        except Exception as e:
                            print(e)
                    del fd_name[temp]
                else:
                    print(f"connect message: {data}")
                    for other in inputs:
                        if other != ss and other != temp:
                            try:
                            	other.send(data.encode(encoding='utf8'))
                            except Exception as e:
                            	print(e)

if __name__ == '__main__':
server_run()
```



 客户端代码：  

```python
import socket, select, threading, sys;

host = socket.gethostname()

addr = (host, 5963)

def conn():
    s = socket.socket()
    s.connect(addr)
    return s

def lis(s):
    my = [s]
    while True:
        r, w, e = select.select(my, [], [])
        if s in r:
            try:
            	print(s.recv(1024).decode(encoding='utf8'))
            except socket.error:
            	print('socket is error')
            	exit()

def talk(s):
    while True:
        try:
            info = input('')
            s.send(info.encode(encoding='utf8'))
        except Exception as e:
            print(e)
            exit()

def main():
    ss = conn()
    t = threading.Thread(target=lis, args=(ss,))
    t.start()
    t1 = threading.Thread(target=talk, args=(ss,))
    t1.start()

if __name__ == '__main__':
	main()
```

 启动一个服务器端代码，启动两个客户端代码；两个客户端进行通信，中间经过服务器进行中转。 

  扩展：考虑采用python配色方案来处理上述网络场景。 



##  采用tcp协议和UDP协议实现简单的聊天功能 

