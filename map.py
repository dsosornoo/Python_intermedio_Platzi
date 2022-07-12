

my=[1,2,3,4,5]


## convertir esta lista pero realizandole un proceso o un funcion
# squares=[i**2 for i in my ]
squares = list(map(lambda x : x**2, my))

print(squares)