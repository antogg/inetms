str='Hello world'
print('This is a', str) # Literal string and string variable

def func1():
    print('In func1')

print('Outside func1')

def func2():
    return 'In func2'

func1()
str2=func2()
print(str2)