from add import add
from divide import divide
from multiply import multiply
from subtract import subtract
print("Welcome to Simple Calculator")
print("1. Addition")
print("2. Subtraction ")
print("3. Multliply")
print("4. Divide")
ch = input("Enter Operation: ")
if ch == '1':
	add()
elif ch == '2':
	subtract()
elif ch == '3':
	multiply()
elif ch == '4':
	divide()
else:
	print("Error")