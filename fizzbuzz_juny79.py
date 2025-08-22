for j in range(1,30+1):
    if j % 15 == 0:
        print('fizzbuzz')
    elif j % 3 == 0:
        print('fizz')
    elif j % 5 == 0:
        print('buzz')
    else:
        print(j)
