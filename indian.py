import pandas as pd

df = pd.read_csv('Indian237_Ingested.csv')
df.head()
del df['Unnamed: 0']
df['Standard_Food_Category'] = df['Standard_Food_Category'].replace({'Sabzis, Dals & Curries':'1', 'Rice based Dishes':'2', 'Rotis & Parathas':'3', 'Sweets':'4', 'Idlis & Dosa':'5', 'Fast Foods':'6', 'Fish & Egg Products':'7', 'Meat & Poultry':'8'})


def indobesity_food():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1. Sabzis, Dals & Curries, 2. Rotis & Parathas, 3. Sweets, 4. Idlis & Dosa, 5. Fast Foods")
        n = int(input())
        x = df[(df['Protein'] <= '10(kcal/24H)') & (df['Saturated'] <= '10.0(gm)')]
        if n == 1:
            x = x[x['Standard_Food_Category'] == '1']
            print(x['FoodItem'])
        elif n == 2:
            x = x[x['Standard_Food_Category'] == '3']
            print(x['FoodItem'])
        elif n == 3:
            x = x[x['Standard_Food_Category'] == '4']
            print(x['FoodItem'])
        elif n == 4:
            x = x[x['Standard_Food_Category'] == '5']
            print(x['FoodItem'])
        elif n == 5:
            x = x[x['Standard_Food_Category'] == '6']
            print(x['FoodItem'])
        else:
            break


def inddiafood():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1. Sabzis, Dals & Curries, 2. Rice based Dishes, 3. Rotis & Parathas, 4. Sweets, 5. Idlis & Dosa, 6. Fast Foods, 7. Fish & Egg Products, 8. Meat & Poultry")
        n = int(input())
        x = df[(df['Cholesterol'] <= '50mg') & (df['Saturated'] <= '7.0(gm)')]
        if n == 1:
            x = x[x['Standard_Food_Category'] == '1']
            print(x['FoodItem'])
        elif n == 2:
            x = x[x['Standard_Food_Category'] == '2']
            print(x['FoodItem'])
        elif n == 3:
            x = x[x['Standard_Food_Category'] == '3']
            print(x['FoodItem'])
        elif n == 4:
            x = x[x['Standard_Food_Category'] == '4']
            print(x['FoodItem'])
        elif n == 5:
            x = x[x['Standard_Food_Category'] == '5']
            print(x['FoodItem'])
        elif n == 6:
            x = x[x['Standard_Food_Category'] == '6']
            print(x['FoodItem'])
        elif n == 7:
            x = x[x['Standard_Food_Category'] == '7']
            print(x['FoodItem'])
        elif n == 8:
            x = x[x['Standard_Food_Category'] == '8']
            print(x['FoodItem'])
        else:
            break


def indhyperfood():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1. Sabzis, Dals & Curries, 2. Rice based Dishes, 3. Rotis & Parathas, 4. Sweets, 5. Idlis & Dosa, 6. Fast Foods, 7. Fish & Egg Products, 8. Meat & Poultry")
        n = int(input())
        x = df[(df['Sodium'] <= '50mg')]
        if n == 1:
            x = x[x['Standard_Food_Category'] == '1']
            print(x['FoodItem'])
        elif n == 2:
            x = x[x['Standard_Food_Category'] == '2']
            print(x['FoodItem'])
        elif n == 3:
            x = x[x['Standard_Food_Category'] == '3']
            print(x['FoodItem'])
        elif n == 4:
            x = x[x['Standard_Food_Category'] == '4']
            print(x['FoodItem'])
        elif n == 5:
            x = x[x['Standard_Food_Category'] == '5']
            print(x['FoodItem'])
        elif n == 6:
            x = x[x['Standard_Food_Category'] == '6']
            print(x['FoodItem'])
        elif n == 7:
            x = x[x['Standard_Food_Category'] == '7']
            print(x['FoodItem'])
        elif n == 8:
            x = x[x['Standard_Food_Category'] == '8']
            print(x['FoodItem'])
        else:
            break


def indheartfood():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1. Sabzis, Dals & Curries, 2. Rice based Dishes, 3. Rotis & Parathas, 4. Sweets, 5. Idlis & Dosa, 6. Fast Foods, 7. Fish & Egg Products, 8. Meat & Poultry")
        n = int(input())
        x = df[(df['Sodium'] <= '30mg') & (df['Monounsaturated'] <= '3.5mg') & (df['Polyunsaturated'] <= '3.5mg')]
        if n == 1:
            x = x[x['Standard_Food_Category'] == '1']
            print(x['FoodItem'])
        elif n == 2:
            x = x[x['Standard_Food_Category'] == '2']
            print(x['FoodItem'])
        elif n == 3:
            x = x[x['Standard_Food_Category'] == '3']
            print(x['FoodItem'])
        elif n == 4:
            x = x[x['Standard_Food_Category'] == '4']
            print(x['FoodItem'])
        elif n == 5:
            x = x[x['Standard_Food_Category'] == '5']
            print(x['FoodItem'])
        elif n == 6:
            x = x[x['Standard_Food_Category'] == '6']
            print(x['FoodItem'])
        elif n == 7:
            x = x[x['Standard_Food_Category'] == '7']
            print(x['FoodItem'])
        elif n == 8:
            x = x[x['Standard_Food_Category'] == '8']
            print(x['FoodItem'])
        else:
            break
