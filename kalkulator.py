num1 = float(input("angka pertama: "))
op = (input("operator: "))
num2 = float(input("angka kedua: "))

if op == '+':
	print(num1 + num2)
elif op == '-':
	print(num1 - num2)
elif op == '/':
	print(num1 / num2)
elif op == '*':
	print(num1 * num2)
else:
	print("operator tidak falid")
