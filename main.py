from diabetes import diabetes
from Heart import heart
from hypertension import hypertension
from obesity import obesity
from food import obesity_food
from food import heartfood
from food import diafood
from food import hyperfood
from indian import indobesity_food
from indian import indheartfood
from indian import inddiafood
from indian import indhyperfood

print("Welcome!!!")
print("Risk Calculator and Food recommendation system")
while True:
    n = int(input("Select condition: 1. Diabetes 2. Heart disease 3. Hypertension 4. Obesity (press 0 to exit the risk calculator)"))
    if n == 1:
        diabetes()
        print("Want to know recommended foods for this condition?? if yes press y, if no then press n")
        i = input()
        if i == 'y':
            x = int(input("press 1 for Indian food else press 0 American food"))
            if x == 1:
                inddiafood()
            else:
                diafood()
    elif n == 2:
        heart()
        print("Want to know recommended foods for this condition?? if yes press y, if no then press n")
        i = input()
        if i == 'y':
            x = int(input("press 1 for Indian food else press 0 American food"))
            if x == 1:
                indheartfood()
            else:
                heartfood()
    elif n == 3:
        hypertension()
        print("Want to know recommended foods for this condition?? if yes press y, if no then press n")
        i = input()
        if i == 'y':
            x = int(input("press 1 for Indian food else press 0 American food"))
            if x == 1:
                indhyperfood()
            else:
                hyperfood()
    elif n == 4:
        obesity()
        print("Want to know recommended foods for this condition?? if yes press y, if no then press n")
        i = input()
        if i == 'y':
            x = int(input("press 1 for Indian food else press 0 American food"))
            if x == 1:
                indobesity_food()
            else:
                obesity_food()
    else:
        break
