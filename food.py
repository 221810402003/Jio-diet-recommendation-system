import pandas as pd

df = pd.read_csv('USDA_Ingested.csv')
df.head()
del df['Unnamed: 0']
df['Standard_Food_Category'] = df['Standard_Food_Category'].replace({'Dairy Products':'1', 'Baby Foods':'2', 'Beverages & Health Drinks':'3', 'Dry Powders and Mixes':'4', 'Bakery Products':'5', 'Pizza & Pasta':'6', 'Fish & Egg Products':'7', 'Fast Foods':'8', 'Salads & Vegetables':'9', 'Soups & Sauces':'10', 'Meat & Poultry':'11', 'Rice based Dishes':'12', 'Pulses & Legumes':'13', 'Sabzis, Dals & Curries':'14', 'Spices & Herbs':'15', 'Nuts & Seeds':'16', 'Sweets':'17', 'Rotis & Parathas':'18', 'Chocolates & Energy Bars':'19', 'Maggie & Noodles':'20', 'Breakfast Cereals':'21', 'Mexican Dishes':'22', 'Fruits & Juices':'23', 'Jams, Syrups, Toppings':'24', 'Fats and Oils':'25'})


def obesity_food():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1.Dairy Products, 2.Baby Foods, 3.Beverages & Health Drinks, 4.Dry Powders and Mixes, 5.Bakery Products, 6.Pizza & Pasta, 7.Fish & Egg Products, 8.Fast Foods, 9.Salads & Vegetables, 10.Soups & Sauces, 11.Meat & Poultry, 12.Rice based Dishes, 13.Pulses & Legumes, 14.Sabzis, Dals & Curries, 15.Spices & Herbs, 16.Nuts & Seeds, 17.Sweets, 18.Rotis & Parathas, 19.Chocolates & Energy Bars, 20.Maggie & Noodles, 21.Breakfast Cereals, 23.Fruits & Juices, 24.Jams, Syrups and Toppings, 25.Fats and Oils")
        n = int(input())
        x = df[(df['Protein'] <= '10(kcal/24H)') & (df['Saturated'] <= '10.0(gm)')]
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
        elif n == 9:
            x = x[x['Standard_Food_Category'] == '9']
            print(x['FoodItem'])
        elif n == 10:
            x = x[x['Standard_Food_Category'] == '10']
            print(x['FoodItem'])
        elif n == 11:
            x = x[x['Standard_Food_Category'] == '11']
            print(x['FoodItem'])
        elif n == 12:
            x = x[x['Standard_Food_Category'] == '12']
            print(x['FoodItem'])
        elif n == 13:
            x = x[x['Standard_Food_Category'] == '13']
            print(x['FoodItem'])
        elif n == 14:
            x = x[x['Standard_Food_Category'] == '14']
            print(x['FoodItem'])
        elif n == 15:
            x = x[x['Standard_Food_Category'] == '15']
            print(x['FoodItem'])
        elif n == 16:
            x = x[x['Standard_Food_Category'] == '16']
            print(x['FoodItem'])
        elif n == 17:
            x = x[x['Standard_Food_Category'] == '17']
            print(x['FoodItem'])
        elif n == 18:
            x = x[x['Standard_Food_Category'] == '18']
            print(x['FoodItem'])
        elif n == 19:
            x = x[x['Standard_Food_Category'] == '19']
            print(x['FoodItem'])
        elif n == 20:
            x = x[x['Standard_Food_Category'] == '20']
            print(x['FoodItem'])
        elif n == 21:
            x = x[x['Standard_Food_Category'] == '21']
            print(x['FoodItem'])
        elif n == 23:
            x = x[x['Standard_Food_Category'] == '23']
            print(x['FoodItem'])
        elif n == 24:
            x = x[x['Standard_Food_Category'] == '24']
            print(x['FoodItem'])
        elif n == 25:
            x = x[x['Standard_Food_Category'] == '25']
            print(x['FoodItem'])
        else:
            break


def diafood():
    while True:
        print(
            "Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1.Dairy Products, 2.Baby Foods, 3.Beverages & Health Drinks, 4.Dry Powders and Mixes, 5.Bakery Products, 6.Pizza & Pasta, 7.Fish & Egg Products, 8.Fast Foods, 9.Salads & Vegetables, 10.Soups & Sauces, 11.Meat & Poultry, 12.Rice based Dishes, 13.Pulses & Legumes, 14.Sabzis, Dals & Curries, 15.Spices & Herbs, 16.Nuts & Seeds, 17.Sweets, 18.Rotis & Parathas, 19.Chocolates & Energy Bars, 20.Maggie & Noodles, 21.Breakfast Cereals, 22.Mexican Dishes, 23.Fruits & Juices, 24.Jams, Syrups and Toppings, 25.Fats and Oils")
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
        elif n == 9:
            x = x[x['Standard_Food_Category'] == '9']
            print(x['FoodItem'])
        elif n == 10:
            x = x[x['Standard_Food_Category'] == '10']
            print(x['FoodItem'])
        elif n == 11:
            x = x[x['Standard_Food_Category'] == '11']
            print(x['FoodItem'])
        elif n == 12:
            x = x[x['Standard_Food_Category'] == '12']
            print(x['FoodItem'])
        elif n == 13:
            x = x[x['Standard_Food_Category'] == '13']
            print(x['FoodItem'])
        elif n == 14:
            x = x[x['Standard_Food_Category'] == '14']
            print(x['FoodItem'])
        elif n == 15:
            x = x[x['Standard_Food_Category'] == '15']
            print(x['FoodItem'])
        elif n == 16:
            x = x[x['Standard_Food_Category'] == '16']
            print(x['FoodItem'])
        elif n == 17:
            x = x[x['Standard_Food_Category'] == '17']
            print(x['FoodItem'])
        elif n == 18:
            x = x[x['Standard_Food_Category'] == '18']
            print(x['FoodItem'])
        elif n == 19:
            x = x[x['Standard_Food_Category'] == '19']
            print(x['FoodItem'])
        elif n == 20:
            x = x[x['Standard_Food_Category'] == '20']
            print(x['FoodItem'])
        elif n == 21:
            x = x[x['Standard_Food_Category'] == '21']
            print(x['FoodItem'])
        elif n == 22:
            x = x[x['Standard_Food_Category'] == '22']
            print(x['FoodItem'])
        elif n == 23:
            x = x[x['Standard_Food_Category'] == '23']
            print(x['FoodItem'])
        elif n == 24:
            x = x[x['Standard_Food_Category'] == '24']
            print(x['FoodItem'])
        elif n == 25:
            x = x[x['Standard_Food_Category'] == '25']
            print(x['FoodItem'])
        else:
            break


def hyperfood():
    while True:
        print(
            "Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1.Dairy Products, 2.Baby Foods, 3.Beverages & Health Drinks, 4.Dry Powders and Mixes, 5.Bakery Products, 6.Pizza & Pasta, 7.Fish & Egg Products, 8.Fast Foods, 9.Salads & Vegetables, 10.Soups & Sauces, 11.Meat & Poultry, 12.Rice based Dishes, 13.Pulses & Legumes, 14.Sabzis, Dals & Curries, 15.Spices & Herbs, 16.Nuts & Seeds, 17.Sweets, 19.Chocolates & Energy Bars, 20.Maggie & Noodles, 21.Breakfast Cereals, 22.Mexican Dishes, 23.Fruits & Juices, 24.Jams, Syrups and Toppings, 25.Fats and Oils")
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
        elif n == 9:
            x = x[x['Standard_Food_Category'] == '9']
            print(x['FoodItem'])
        elif n == 10:
            x = x[x['Standard_Food_Category'] == '10']
            print(x['FoodItem'])
        elif n == 11:
            x = x[x['Standard_Food_Category'] == '11']
            print(x['FoodItem'])
        elif n == 12:
            x = x[x['Standard_Food_Category'] == '12']
            print(x['FoodItem'])
        elif n == 13:
            x = x[x['Standard_Food_Category'] == '13']
            print(x['FoodItem'])
        elif n == 14:
            x = x[x['Standard_Food_Category'] == '14']
            print(x['FoodItem'])
        elif n == 15:
            x = x[x['Standard_Food_Category'] == '15']
            print(x['FoodItem'])
        elif n == 16:
            x = x[x['Standard_Food_Category'] == '16']
            print(x['FoodItem'])
        elif n == 17:
            x = x[x['Standard_Food_Category'] == '17']
            print(x['FoodItem'])
        elif n == 19:
            x = x[x['Standard_Food_Category'] == '19']
            print(x['FoodItem'])
        elif n == 20:
            x = x[x['Standard_Food_Category'] == '20']
            print(x['FoodItem'])
        elif n == 21:
            x = x[x['Standard_Food_Category'] == '21']
            print(x['FoodItem'])
        elif n == 22:
            x = x[x['Standard_Food_Category'] == '22']
            print(x['FoodItem'])
        elif n == 23:
            x = x[x['Standard_Food_Category'] == '23']
            print(x['FoodItem'])
        elif n == 24:
            x = x[x['Standard_Food_Category'] == '24']
            print(x['FoodItem'])
        elif n == 25:
            x = x[x['Standard_Food_Category'] == '25']
            print(x['FoodItem'])
        else:
            break


def heartfood():
    while True:
        print("Select the catogories of the food from the list (weight = 100g)(press 0 to skip): 1.Dairy Products, 2.Baby Foods, 3.Beverages & Health Drinks, 4.Dry Powders and Mixes, 5.Bakery Products, 6.Pizza & Pasta, 7.Fish & Egg Products, 8.Fast Foods, 9.Salads & Vegetables, 10.Soups & Sauces, 11.Meat & Poultry, 12.Rice based Dishes, 13.Pulses & Legumes, 14.Sabzis, Dals & Curries, 15.Spices & Herbs, 16.Nuts & Seeds, 17.Sweets, 19.Chocolates & Energy Bars, 20.Maggie & Noodles, 21.Breakfast Cereals, 22.Mexican Dishes, 23.Fruits & Juices, 24.Jams, Syrups and Toppings, 25.Fats and Oils")
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
        elif n == 9:
            x = x[x['Standard_Food_Category'] == '9']
            print(x['FoodItem'])
        elif n == 10:
            x = x[x['Standard_Food_Category'] == '10']
            print(x['FoodItem'])
        elif n == 11:
            x = x[x['Standard_Food_Category'] == '11']
            print(x['FoodItem'])
        elif n == 12:
            x = x[x['Standard_Food_Category'] == '12']
            print(x['FoodItem'])
        elif n == 13:
            x = x[x['Standard_Food_Category'] == '13']
            print(x['FoodItem'])
        elif n == 14:
            x = x[x['Standard_Food_Category'] == '14']
            print(x['FoodItem'])
        elif n == 15:
            x = x[x['Standard_Food_Category'] == '15']
            print(x['FoodItem'])
        elif n == 16:
            x = x[x['Standard_Food_Category'] == '16']
            print(x['FoodItem'])
        elif n == 17:
            x = x[x['Standard_Food_Category'] == '17']
            print(x['FoodItem'])
        elif n == 19:
            x = x[x['Standard_Food_Category'] == '19']
            print(x['FoodItem'])
        elif n == 20:
            x = x[x['Standard_Food_Category'] == '20']
            print(x['FoodItem'])
        elif n == 21:
            x = x[x['Standard_Food_Category'] == '21']
            print(x['FoodItem'])
        elif n == 22:
            x = x[x['Standard_Food_Category'] == '22']
            print(x['FoodItem'])
        elif n == 23:
            x = x[x['Standard_Food_Category'] == '23']
            print(x['FoodItem'])
        elif n == 24:
            x = x[x['Standard_Food_Category'] == '24']
            print(x['FoodItem'])
        elif n == 25:
            x = x[x['Standard_Food_Category'] == '25']
            print(x['FoodItem'])
        else:
            break
