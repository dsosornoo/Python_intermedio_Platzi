from functools import  reduce
my=[2,2,2,2,2]
# l=1
# for i in my:
#     l=l*i

l= reduce(lambda a,b: a+b, my)

print(l)