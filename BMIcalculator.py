name_1 = "Anni"
weight_1 = 40
height_1 = 1.5

name_2 = "Ani"
weight_2 = 90
height_2 = 1.67

def BMIcalculation(name, weight_KG, height_m):
        bmi = weight_KG/(height_m ** 2)
        print("bmi :")
        print(bmi)
        if bmi < 25:
            return name + " not overweight"
        else :
            return name + " is overweight"


result1 = BMIcalculation(name_1, weight_1, height_1)
print(result1)
print("")
result2 = BMIcalculation(name_2, weight_2, height_2)
print(result2)
