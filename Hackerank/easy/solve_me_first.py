def solveMeFirst(a,b):
    if 1 <= a <= 1000 and 1 <= b <= 1000:
        return a+b
    else:
        return "Give a valid number"
	


num1 = int(input("Enter a first number: "))
num2 = int(input("Enter second number: "))
res = solveMeFirst(num1,num2)
print(res)