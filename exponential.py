print("Exponential X^Y")
x=int(input("Insert X: "))
y=int(input("Insert Y: "))

for index in range(1, y+1):
    result = x ** index

print(result)
