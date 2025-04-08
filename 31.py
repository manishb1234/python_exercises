def foo(a=1, b=2):
    return a + b


x = foo() - 1

#type error - foo() should be called as foo is function
# name, its type error not syntax

print(x)