num1 = int(input('Enter a number: '))
num2 = int(input('Enter the second number: '))

if(num1 == num2):
    print('Number %d is equal to number %d ' %(num1, num2))
elif(num1 != num2):
    print('Number %d is different from number %d ' %(num1, num2))
elif(num1 < num2):
    print('Number %d is less than number %d ' % (num1, num2))
elif(num1 > num2):
    print('Number %d is greater than number %d ' % (num1, num2))
else:
    print('ERROR')