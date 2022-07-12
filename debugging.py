# def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    
    # return divisors
divisors=lambda num:[i for i in range(1,num+1) if num&i==0]


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num<=0:
            raise ValueError('negative number is not valid')
            print(divisors(num))
            print('Finish!...')
        
    except ValueError:
        print("Solo numeros positivos")
    


if __name__ == '__main__':
    run()