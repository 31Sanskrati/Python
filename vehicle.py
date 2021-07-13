import math
import random
from random import randint

#generate a random number of n size
def unique_num(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#prints a unique registration id
def registration_ID():
    num = unique_num(12)
    print("Registration Id: ", num)

#generate licence plate number
def num_plate():
    #different states code for denoting the states in which the car is registered
    states = ["JK", "LA", "HP", "PB", "CH", "UK", "HR", "DL", "UP", "RJ",
              "BR", "GJ", "MP", "JH", "WB", "MH", "TS", "CG",
              "OR", "AP", "GA", "KA", "TN", "KL", "SK", "AR", "AS",
              "NL", "ML", "TR", "MN", "MZ"]
    random_state = random.randint(0, 32)
    
    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    random_aplhabet = random.randint(0, 25)

    # format of number plate : MP24AB5555
    plate_number = ""
    plate_number += states[random_state]
    plate_number += str(unique_num(1)) #denotes the district 
    plate_number += str(unique_num(1)) #denotes the district 
    plate_number += alphabets[random_aplhabet]
    plate_number += alphabets[random_aplhabet]
    plate_number += str(unique_num(4))
    print("Licence plate number :", plate_number)


def tax(price, type):
    #for electrical vehicle 5% tax
    if car_type == 'E':
        payable = (5*price)/100
        return payable
    #for regular vehicle 8% tax
    else:
        payable = (8*price)/100
        return payable


brand_name = input("Enter car brand name: ")
car_type = input(
    "Enter 'E' if your vehicle is electrical and any other alphabet if its not : ")
price = {'maruti': 400000, 'hyundai': 500000, 'honda': 700000, 'tata': 500000,
         'toyota': 930000, 'ford': 600000, 'audi': 3500000, 'mahindra': 600000,
         'renault': 300000, 'nissan': 250000, 'skoda': 800000}

registration_ID()
num_plate()
print("Brand Name:",brand_name.upper())
print("Catalog price of the car:", price[brand_name])

if brand_name in price:
    print("You have to pay", tax(price[brand_name], car_type), "tax on the vehicle")
else:
    print("Enter another brand")
