def run():
    # my_dict={}

    # for i in range(1,101):
    #     my_dict[i]=i**3
    # print(my_dict)
    my={i:i**3 for i in range(1,101) if i%3!=0}
    print(my)



if __name__ == '__main__':
    run()