def run():
    # squares=[]
    
    # for i in range(1,101):
    #     squares.append(i**2)

    # for i in range(1,101):
    #     if i%3!=0:
    #         squares.append(i**2)
    squares=[i**2 for i in range(1,101) if i%3!=0]

    m36=[i for i in range(1,100000) if i%36 ==0]

    print (squares)
    print(m36)
if __name__=='__main__':
    run()