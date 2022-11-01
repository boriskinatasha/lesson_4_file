def create_cook_book(file):
    cook_book = {}
    with open(file, "rt", encoding='utf8') as file_obj:
        for cook in file_obj:
            dish = cook.strip()
            ingridients = []
            count_ingr = int(file_obj.readline())
            for i in range(count_ingr):
                ingridient = file_obj.readline().split('|')
                ingridient_item = {}
                ingridient_item['ingridient_name'] = ingridient[0]
                ingridient_item['quantity'] = int(ingridient[1])
                ingridient_item['measure'] = ingridient[2]
                ingridients.append(ingridient_item)
                cook_book[dish] = ingridients
            file_obj.readline()
    return cook_book

def get_shop_list_by_dishes(dishes_name=None, dishes_count=None):
    if (dishes_name == None or dishes_count == None):
        return "Неправильно указаны параметры, введите наименование блюда и количество порций"
    ingredients_output = {}
    cook_book = create_cook_book('recipes.txt')
    for dish in dishes_name:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if ingridient['ingridient_name'] not in ingredients_output:
                    ingredients_output[ingridient['ingridient_name']] = (
                    {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * dishes_count})
                else:
                    ingredients_output[ingridient['ingridient_name']] = ({'measure': ingridient['measure'],'quantity': int(ingridient['quantity']) * dishes_count +ingredients_output[ingridient['ingridient_name']]['quantity']})
        else:
            ingredients_output = 'Указанное блюдо отсутствует в кулинарной книге'
    return (ingredients_output)

def union_files(*files):
    files_info={}
    files_text={}
    for file in files:
        with open(file, "r", encoding='utf8') as f:
            counter=0
            text=''
            for line in f:
                counter+=1
                text+=line
            files_text[file]=text
            files_info[file]=counter
        f.close()
    sorted_files=dict(sorted(files_info.items(), key=lambda item: item[1],reverse=True))
    with open('new_file.txt', 'a', encoding='utf8') as f:
        for file,count in sorted_files.items():
            f.write(f'{file}\n')
            f.write(f'{count}\n')
            f.write(f'{files_text[file]}\n')
    f.close()

# 1
print(create_cook_book('recipes.txt'))
# 2
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# 3
union_files('1.txt','2.txt','3.txt')
