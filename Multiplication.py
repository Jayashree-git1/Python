# Python program to find multiply two numbers  Reading two numbers
number1 = input('Enter first number: ')
number2 = input('Enter second number: ')
# Converting to float ---input() function return string
number1 = float(number1)
number2 = float(number2)
result = number1 * number2
# Displaying result
print('%0.2f * %0.2f = %0.2f' % (number1, number2, result))