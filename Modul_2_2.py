First = input('Enter the first number:')
Second = input('Enter the second number:')
Third = input('Enter the third number:')
if First == Second and First == Third:
print(3)
elif First == Second or First == Third or Second == Third:
print(2)
else:
print(0)
