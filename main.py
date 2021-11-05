import time

import pep8
"""" Insert grams in  the type of food and calculate the total amount of calories consumed for the moment the information is  provided"""

#create list for categories
Foods = ('fats', 'alcohol', 'carbohydrates', 'proteins')

#greet user


def welcome():
    print(
        'Welcome to the calorie counting app, please provide the information requested below: '
    )
    #create list so that values are collected later and available
    print()


grams = []


def request_info():

    for food in Foods:

        weight = float(
            input(f"please provide the weight of {food} in grams: "))

        all_grams = grams.append(weight)
        print()


def calculate():
    fats, alcohol, carbs, proteins = grams
    calorie_fats = float(fats) * 9  #
    calorie_alcohol = float(alcohol) * 7  #14
    calorie_carbs = float(carbs) * 4  #12
    calorie_proteins = float(proteins) * 4  #16
    total_calories = calorie_fats + calorie_alcohol + calorie_carbs + calorie_proteins
    print(f"The Total calories  ingested for these foods are: {total_calories}"
          )  #49


welcome()
request_info()
calculate()
