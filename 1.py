# # # #
# # # # age = int(input("请输出你家猫猫的年龄"))
# # # # print("")
# # # # if age <0:
# # # #     print("不足一岁")
# # # # elif age ==1:
# # # #     print("相当于10岁的人")
# # # # elif age ==2:
# # # #     print("相当于20岁的人")
# # # # elif age >2:
# # # #     human = 20 + (age -2)*5
# # # #     print("对应人类年龄：",human)
# # # # input("点击退出")
# # # #
# # # # print(6==6)
# # # # x=5
# # # # y=8
# # # # print(x==y)
# # # number=7
# # # guess=-1
# # # print("猜数字")
# # # while guess != number:
# # #     guess = int(input("请输入"))
# # #     if guess == number:
# # #         print("猜对")
# # #     elif guess < number:
# # #         print("猜小了")
# # #     elif guess > number:
# # #         print("猜大了")
# #
# #
# # n=int(input("请输入N的值"))
# #
# # sum=0
# # counter=1
# # while counter <=n:
# #     sum=sum+counter
# #     counter+=1
# # print("1到%d 之和为：%d" %(n,sum))
# #
# count=0
# while count<5:
#     print(count,"<5")
#     count = count +1
# else:
#     print(count,">=5")
#
# flag=1
# while 1<2:
#     print('小茹欢迎你！！')
# print("再见！！")

# xiaoru=["朝","之","雾","万","岁"]
# for x in xiaoru:
# print(x)
#
# zzw=["zhao","zhi","wu","xiaoru","benzhu"]
#
# for xiaoru in zzw:
#     if xiaoru == "xiaoru":
#         print("#笨猪#雪糕")
#         break
#     print("就很帅" + xiaoru)
# else:
#     print("不够帅")
# print("帅到完事了")
#
# for i in  range(10):
#     print(i+1)
# for i in  range(50,60):
#     print(i)
# for i in range(-1,-10,-2):
#     print(i)
# a=['xiaoru','qq','wechat','alipay','python']
# for i in range(len(a)):
#     print(i,a[i])
# for letter in 'xiaoru':
# #     if letter == 'o':
# #         continue
# #     print('当前字母为：',letter)
# # var = 10
# # while var >0:
# #     print('当前变量为：',var)
# #     var = var -1
# #     if var == 5:
# #         continue
# # print("good bye!")
# for letter in 'xiaoru':
#     if letter == 'o':
#         break
#     print('当前字母为：',letter)
# var = 10
# while var >0:
#     print('当前变量为：',var)
#     var = var -1
#     if var == 5:
#         break
# print("good bye!")
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n,'等于',x,'*',n//x)
#             break
#     else:
#         print(n,'是质数')
# while True:
# #     pass
# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
#
# print("Good bye!")
# def func(**kwargs):
#     for name,value in kwargs.items():
#         print(0 = 1),format(name,value)
# func(name='jack',age=30)
# a=map(lambda x:x*2,[1,2,3])
# list(a)
# class mynumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=mynumbers()
# myiter=iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# 类对象
# 比如x.i就是
# 先定义
# myclass
# 然后
# myclass里面有 i 是123456
# myclass里面有 f 是会返回hello world
# 再定义x是在myclass类里面的
# x=myclass
# 在通过x.i 和 x.f
# 来打印不同的结果
#
# class myclass:
#     i = 123456
#     j = 654321
#     def f(self):
#         return 'hello world'
#     def v(self):
#         return 'xiao ru'
# x = myclass()
#
# print("myclass类的属性i 为 ：",x.i)
# print("myclass类的属性j 为 ：",x.j)
# print("myclass类的方法f输出为：",x.f())
# print("myclass类的方法v输出为：",x.v())

# def __init__(self):
#     self.data = []

#
# class complex:
# #定义一个complex的类
#     def __init__(self,realpart,imagpart):
#         #定义
#         self.r=realpart
#         self.i=imagpart
# x = complex(3.0,-4.5)
# print(x.r,x.i)

# class test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# t =test()
# t.prt()

# class Test:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
#
#
# t = Test()
# t.prt()

# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, x, y, z):
#         self.name = x
#         self.age = y
#         self.__weight = z
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
# # 实例化类
# p = people('xiaoru', 22, 60)
# p.speak()

# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
# class student(people):
#     grade=''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在 %s "%(self.name,self.age,self.grade))
# s = student('xiaoru',22,60,'work')
# s.speak()

# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
#
#
# # 多重继承
# class sample(speaker, student):
#     a = ''
#
#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         #调用student类里面的self,n,a,w,g参数
#         speaker.__init__(self, n, t)
#         #调用speaker类里面的self,n,t参数
#
# # 对sample调用的speaker提供变量
# test = sample("XiaoRu", 25, 80, 4, "Python")
# y=test.speak()
# print(y)

# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


#
# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('小茹自学', 'www.xiaoru.vip')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# #x.__foo()  # 报错

# def hello():
#     print("hello world")
#
# hello()

# def area(width,height):
#     return width * height
# def print_welcome(name):
#     print("welcome",name)
# print_welcome("xiaoru")
# w=7
# h=8
# print("width=",w,"height=",h,"area=",area(w,h))

# def printme(str):
#     print(str)
#     return
#
# printme("我要开始了")
# printme("不愧是你呀")

# a=[1,2,3]
# a="xiaoru"

# def changeint(a):
#     a=10
# b=2
# changeint(b)
# print(b)

# def changeme(mylist):
#     mylist.append([1,2,3,4])
#     print("函数内取值:",mylist)
#     return
#
# mylist=[10,20,30]
# changeme(mylist)
# print("函数外取值",mylist)

# def printme(str):
#     print(str)
#     return
#
# printme("不愧是小茹")

# def printinfo(name,age):
#     print("名字",name)
#     print("年龄",age)
#     return
#
# printinfo(age=22,name="xiaoru")

# def printinfo(name,age=22):
#     print("名字",name)
#     print("年龄",age)
#     return
#
# printinfo(name="xiaoru")
# print("------------------")
# printinfo(name="xiaoru",age=23)

# def functionname([formal_args,] * var_args_tuple):
#     function_suite
#     return [expression]

# def printinfo(arg1,*vartuple):
#     print("输出")
#     print(arg1)
#     print(vartuple)
#
# printinfo(70,60,50,40,30,20,10)

# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
# printinfo(10)
# printinfo(20,30,40,50)

# def printinfo(arg1,**vartuple):
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#     return
#
# printinfo(10,a=7,b=8)

# sum = lambda arg1, arg2:agr1 + arg2
#
# print("相加后的值为：", sum( 10 , 20 ))
# print("相加后的值为：", sum( 20 , 20 ))

# def sum(arg1,arg2):
#     total=arg1+arg2
#     print("函数内：",total)
#     return total
#
# total = sum(10,20)
# print("函数外：",total)

# if True:
#     msg='i am from zhaozhiwu'
#
# print(msg)

# total = 0 #全局变量
#
# def sum(arg1,arg2):
#     total=arg1+arg2
#     print("函数内是局部变量：",total)
#     return total
# sum(10,20) #sum函数变量
#
# print("函数外是全局变量：",total)

# num = 1
# def fun1():
#     global num
#     print(num)
#     num = 123
#     print(num)
#
# fun1()
# print(num)

# a = 10
# def test(a):
#     a = a + 1
#     print(a)
# test(a)


# 实现用户登录（三次输错机会），且每次错误时候显示剩余错误次数
# username = 'xiaoru'
# password = '123456'
# i=3
#
# while i>0:
#
#     i -= 1
#
#     name = input("请输入用户名:")
#
#     if name == username :
#         passwd=input("请输入密码:")
#         if passwd == password :
#             print("密码正确，请稍后")
#             print("""
#
#           用户名：%s
#           密码：%s
#           登陆成功！
#
#             """%(username,password))
#             break
#         else:
#             print("密码错误，请重新尝试")
#             print("剩余尝试次数:",i)
#     else:
#         print("用户名错误，请重新尝试")
#         print("剩余尝试次数:",i)

# 计算 1 - 2 + 3 - 4 ..... +99 中除了88以外所有数的总和
# i = 1
# sum = 0
# while i < 100:
#     if i != 88:
#         if i % 2 == 0:
#             sum = sum - i
#             print(sum)
#         else:
#             sum = sum + i
#             print(sum)
#     i += 1
#
# print(sum)

# 计算 1 - 2 + 3 - 4 ..... -99 中除了88以外所有数的总和
#
# i = 1
# j = 1
# sum = 0
#
# while > 100

# s = 'asdgsdfgxcvzxcfsadf'
# n = 0
# while 1:
#     print(s[n])
#     n += 1
#     if n == len(s):break

# content = input('>>>').strip()
# con1 = content.split('+')
#
# num = 0
#
# for i in con1:
#     num += int(i)
# print(num)

# a = [66.25, 22, 233, 1, 33, 233, 123.5]
# print(a.count(233),a.count(22),a.count('x'))
#
# a.insert(2,-1)
# a.append(233)
# print(a)
# print(a.count(233),a.count(22),a.count('x'))
#
# a.index(233)
# print(a.index(233))
# a.remove(233)
# print(a)
#
# a.reverse()
# print(a)
#
# a.sort()
# print(a)


# stack=[3,4,5]
# stack.append(6)
# stack.append(7)
#
# print(stack)

# from collections import deque
# import sys
#
# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)
#
# print('\n\npython 路径为 ：',sys.path,'\n')

# import fibo
#
# fibo.fib(1000)
#
# import hello
#
# hello.print_h1(h2='xiaoru')

# import hello,sys,fibo
# print(dir(hello))
#
# print(dir(fibo))
#
# print(dir(sys))

