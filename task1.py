## task 1 :  compare numbers several times.

num1 = int(input('enter first number: '))

num2 = int(input('enter second number: '))

comparison = True

while comparison:
    if num1 == num2:
        print ('numbers are equal')
    else:
        print('Numbers are not equal')
    if num1 < num2: 
        print('Second number is greater than first number') 
    if num1 <= num2:
        print('Second number is greater than or equal to first number')

    if num1>200 and num2>200:
        print('Both numbers are big!')
    elif num1>200 or num2>200:
        print('one of the number is big!')
    else:
        print('Both numbers are not big!')
    comparison = False

#print('big_numbers is set to  True')
#print('big_numbers is set to  False')


#big_numbers = True
