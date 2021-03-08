# This is a simple application to convert your weight from lbs to kg or
# from kg to lbs

import unitConverter


class PrintResults():
    def print_results(name, weight, unit_result):
        print(f"Hello {name}, your weight is {weight} in {unit_result}.")

'''
name = input("What is your name: ")
try:
    weight = int(input("What is your weight: "))
except ValueError:
    print("Invalid value")

unit = (input("(K)g or (l)bs: ")).upper()
'''

name = "Chris"
weight = int(143)
unit = "l"
unit_result = ""

if unit.upper() == "K":
    unit_result = "lbs"
    weight = unitConverter.kg_to_lbs(weight)
    # print(f"Hello {name}, your weight is {weight} in {unit_result}")
    PrintResults.print_results(name, weight, unit_result)
elif unit.upper() == "L":
    unit_result = "kg"
    weight = unitConverter.lbs_to_kg(weight)
    # print(f"Hello {name}, your weight is {weight} in {unit_result}")
    PrintResults.print_results(name, weight, unit_result)
else:
    print("Unit must be 'k' for kg or 'l' for lbs, please try again")