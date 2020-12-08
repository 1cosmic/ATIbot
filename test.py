import json

with open('city.json', 'r') as file:
    load_js = json.load(file)
    bad_keys = (' х ', 'МКАД', ' * ')
    good_city = []

    key1 = []
    key2 = []
    key3 = []


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

