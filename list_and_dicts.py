def run():
    my_list = [1,"duck",True,4.5]
    my_dict={"firstname":"daniel","lastname":"bear"}

    #list of dicts
    super_list=[
        {"firstname":"daniel","lastname":"mex"},
        {"firstname":"juan","lastname":"wall"},
        {"firstname":"pedro","lastname":"rock"},
        {"firstname":"lee","lastname":"qin"},
    ]
    #dict of lists
    super_dict={
        "natural":[1,2,3,4,5,6,7,8,9,0],
        "integer":[-1,-2,0,1,2],
        "float":[1.1,-0.2,0.3,0.4]

    }
    print('superdict'+'\n')
    for key, value in super_dict.items():
        print(key,'-', value)
    print('\n')
    print('super_list','\n')

    # for i in super_list:
    #     print(i["firstname"],'-',i['lastname'])

    for item in super_list:
        print(item['firstname'],'-',item['lastname'])

if __name__ == '__main__':
    run()