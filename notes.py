# function with argument list
# def kitten(*args):

#     if len(args):
#         for s in args:
#             print(s)
#     else: print("Meow")
    
# kitten("dog", "cat")

# tup = ('dog', 'cat', 3)
# kitten(*tup)

# # Argument as a dictionary
# def kitten2(**args):
#     if(len(args)):
#         for key in args:
#             print(f'args[{key}]: ', args[key])

# dic ={'dog': 'Boy', 'rabbit': 'Tim'}
# kitten2(**dic)

# def fun():
#     print('hello')
#     return None

# print(fun())


# # Decorator

# def f1(f):
#     print('This is f1')
#     def f2():
#         print('This is before')
#         f()
#         print('This is after')
    
#     print('This is something')
#     return f2
#     print('this is other things')

# @f1
# def f3():
#     print('this is f3')

# f3()

# def Func(a, b):
#     print(id(a))
#     print(id(b))
#     a = 1; b[0] = 1
#     print(id(a))
#     print(id(b))

# x = 0; y=[0]

# print(id(x))
# print(id(y))
# Func(x, y)
# print(x, y)


# game = ['rock', 'paper', 'scissors', 'paper']
# string = "this is canada"
# print(sorted(set(game), reverse= True))
# import sys
# def main():
#     try:

#         x = int("foo")
#         # y = 5/0
#     # except ValueError:
#     #     print("Value Error")
#     except:
#         print(f"Unknown Error: {sys.exc_info()[1]}")
# if __name__ == '__main__': main()

3000000.32

x = 3000000.325656464564646546

print(f'Money: {x:,.2f}')

s = 'Kayden-is studying-for-test.'
l = s.split('-')
s2 = ' '.join(l)
print(s2)

s1 = 'Test'
s2 = 'tEST'

print(s2.title())

a=1
print('{0:03}'.format(a))
