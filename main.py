hei=float(input("Insert height in m: "))
wei=int(input("Insert weight in kg: "))
BMI= wei/(hei*hei)

if (BMI <= 16.00):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: starvation")
elif(16.00 <= BMI <= 16.99):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: emaciation")
elif(17.00 <= BMI <= 18.49):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: underweight")
elif(18.50 <= BMI <= 24.99):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: correct weight")
elif(25.00 <= BMI <= 29.99):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: overweight")
elif(30.00 <= BMI <= 34.99):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: first degree obesity")
elif(35.00 <= BMI <= 39.99):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: second degree obesity")
elif(BMI >= 40.00):
    print("BMI: ")
    print(BMI)
    print("Diagnosis: third degree obesity")

wei_inf=18.50*hei*hei
wei_sup=24.99*hei*hei
print("The correct intervall of weight is between: ")
print(wei_inf)
print(wei_sup)
