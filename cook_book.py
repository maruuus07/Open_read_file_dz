from pprint import pprint
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        name_cook = line.strip()
        name_course = int(file.readline().strip())
        course = []
        for _ in range(name_course):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            course.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[name_cook] = course

pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish in dishes:
        for name, ingredient in cook_book.items():
            if dish == name:
                for i in ingredient:
                    ing = i.pop('ingredient_name')
                    ingredient_list[ing] = i
    for item, value in ingredient_list.items():
        value['quantity'] = int(value['quantity']) * int(person_count)
    for key, value in ingredient_list.items():
        print(key, value)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


