def run():
    d={i:i**3 for i in range (1,101) if i%3!=0}
    quiz={i:round(i**0.5,2) for i in range(1,1001)}
    print(d)
    print(quiz)

if __name__=='__main__':
    run()