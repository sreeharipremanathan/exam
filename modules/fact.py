def fact():
    num=int(input('enter a number: '))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print('factorial of',num,'is',fact)


fact()