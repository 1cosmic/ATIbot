import json
from operator import attrgetter, itemgetter

# Очистка общего списка городов от лишних.
def filter_city():
    with open('city.json', 'r') as file:
        load_js = json.load(file)
        bad_keys = (' х ', 'МКАД', ' * ')
        good_city = []

        for city in load_js:  # пробегаемся проверкой по каждому городу в общ. списке
            #if city['CountryId'] in good_country: # проверяем принадлежность к нужной стране

            for bad_key in bad_keys:  # проверяем отсутствие лишних ключей в фразах
                if bad_key in city['CityName']:
                    print('Пропущен город: {}'.format(city['CityName']))
                    break

            else:
                # чистый город записываем в отд. список
                good_city.append(city)

        else:
            print(f'\nВсего очищено: {len(load_js) - len(good_city)}')
            print(len(load_js), len(good_city))

    with open('proper_cities.json', 'w') as file:
        json.dump(good_city, file, sort_keys=True,
                indent=4, ensure_ascii=False)

        print('Очистка успешна! Файл сохранён.')
filter_city() # вызываем ф-цию

# Сортировка списка по убыванию: сначала размер, затем страна
def filter_country():
    with open('proper_cities.json', 'r') as file:
        js = json.load(file)
        print(js[1])
    sorted(js, key=itemgetter('CitySize', 'CountryId'), reverse=True)

    with open('corted_cities.json', 'w') as file:
        json.dump(js, file, sort_keys=True,
                  indent=4, ensure_ascii=False)
# ilter_country()
