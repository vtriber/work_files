from pprint import pprint

file_name = 'recipes.txt'

def cook_book(file_name: str) -> dict:
    with open(file_name, "r") as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            key = file.readline()
            ingredients = []
            for item in range(int(key)):
                ingredient = ((file.readline()).strip()).split('|')
                ingredient_dict = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                ingredients.append(ingredient_dict)
            cook_book[dish] = ingredients
            file.readline()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_dict = cook_book(file_name)
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book_dict[dish]:
            # print(ingredient)
            if ingredient['ingredient_name'] in shop_list.keys():
                s_l = shop_list.values()
                print(s_l)
                shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}})

            else:
                shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}})
    return shop_list






# pprint(cook_book(file_name))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
