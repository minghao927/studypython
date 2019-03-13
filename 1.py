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
