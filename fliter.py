my=[1,4,5,6,9,13,19,21,8,10]

# odd=[i for i in my if i %2!=0]

odd= list(filter(lambda x: x%2!=0,my))

print(odd)