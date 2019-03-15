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