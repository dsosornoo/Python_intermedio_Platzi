def compareTriplets(a, b):
    a=[17, 28, 30]
    b=[99, 16, 8]
    # Write your code here
    bob=0
    ali=0
    for i in range(0,4):
        if a[i]<b[i]:
            bob+=i
        elif a[i]>b[i]:
            ali+=i    
    return (ali,bob)

if __name__ == '__main__':
    compareTriplets()