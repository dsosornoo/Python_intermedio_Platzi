from urllib.parse import ParseResultBytes


def run():
    list1=[1,"hello",False,4.5]
    dict1={"primer":"Daniel","segundo":"Steven"}
    #lista de diccionarios
    supper_list=[
        {"primer":"Daniel","segundo":"Steven"},
        {"primer":"Daniel","segundo":"Steven"},
        {"primer":"Daniel","segundo":"Steven"},
        {"primer":"Daniel","segundo":"Steven"}

    ]

    supper_dict={
        "naturales":[1,2,3,4,5,6],
        "integer":[-1,-2,0,4,5,6]

    }

    for key,value in supper_dict.items():
        print(key,"-", value)
        
    

if __name__ == '__main__':
    run()