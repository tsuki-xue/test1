#字符串
# 输出
print("hello world!")
print('I love Python')#单双引号都可，三引号也可以
c=3+5
print(c)
c1="hello"
c2="world"
print(c1+" "+c2)
#\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print ("It's a dog!")
print ('It\'s a dog!')#不可以是print ('It's a dog!')，因为单引号里的'不被转义
print ('\\\t\\')
print (r'\\\t\\')#在引号前加r表示原始字符串，即\和t都不被转义
#子字符串运算
s="hello world"
print(s[0:5])#从第0个字符开始，取到第5个字符
print(s[5:])#从第6个字符开始，取到最后
print(s[:5])#从开头取到第5个字符
print(s[-5:])#从倒数第5个字符开始，取到最后
print(s[::2])#每隔2个字符取一个
print(s[::-1])#反转字符串
print('hello'in s)#判断字符串中是否包含子字符串'hello'
print(s.upper())#转换为大写
print(s.lower())#转换为小写
print(s.replace('l','*'))#替换字符串中的'l'为'*'
print(s.split())#以空格为分隔符，分割字符串为列表
#四则运算
# + - * / 
# //整除 %求余 **乘方
#布尔值
# True--True False--False True and False--False
# True or False--True not True--False True+True--2 True-False--1
#18 >= 6 * 3 or 'py' in 'Python'--True

