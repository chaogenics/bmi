#simple bmi calculator.
weight = float(input("Weight in lbs: "))
heightft = float(input("Height feet: "))
heightin = float(input("Height inches: "))
weightkg = weight/2.2046
heightm = ((heightft*12)+heightin)*0.0254
bmi = weightkg/((heightm)**2)

print(f"Your bmi based on your weight being {int(weight)}lbs and height as {int(heightft)}'{int(heightin)} is {round(bmi,2)}.")