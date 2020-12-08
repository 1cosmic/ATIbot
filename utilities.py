import json

# Очистка общего списка городов от лишних.
def filter_city():

    def proper_city():
        with open('city.json', 'r') as file:
            load_js = json.load(file)

            good_country = (1, 3, 7, 8, 9, 10, 14) # выборка необходимых городов
            bad_keys = (' * ', 'МКАД', ' х ')
            good_city = []

            for city in load_js: # пробегаемся проверкой по каждому городу в общ. списке
                if city['CountryId'] in good_country: # проверяем принадлежность к нужной стране
                    
                    for bad_key in bad_keys: # проверяем отсутствие лишних ключей в фразах
                        if bad_key in city['CityName']:
                            print('Пропущен город: {}'.format(city['CityName']))
            
                            continue

                    else:
                        # чистый город записываем в отд. список
                        good_city.append(city)

            else:
                print(f'\nВсего очищено: {len(load_js) - len(good_city)}')

        return good_city

        # {
        #     "CityId": 1,
        #     "CityName": "Санкт-Петербург",
        #     "CityNameEng": "St. Petersburg",
        #     "CitySize": 6,
        #     "CountryCodeName": "RUS",
        #     "CountryId": 1,
        #     "CountryName": "Россия",
        #     "CountryNameEng": "Russia",
        #     "FiasId": "c2deb16a-0330-4f05-821f-1d09c93331e6",
        #     "FullName": "Санкт-Петербург, Санкт-Петербург (регион), Россия",
        #     "FullNameEng": "St. Petersburg, Sankt-Peterburg (region), Russia",
        #     "Id2": "38331511-9812-e411-8e11-00259038ec34",
        #     "IsRegionalCenter": true,
        #     "Latitude": 59.937282,
        #     "Longitude": 30.310143,
        #     "RegionId": 153,
        #     "RegionName": "Санкт-Петербург (регион)",
        #     "RegionNameEng": "Sankt-Peterburg (region)",
        #     "ShortName": "Санкт-Петербург",
        #     "ShortNameEng": "St. Petersburg"
        # }

    with open('proper_cities.json', 'w') as file:
        json.dump(proper_city(), file, sort_keys=True,
                indent=4, ensure_ascii=False)

        print('Очистка успешна! Файл сохранён.')
# filter_city()

# Очистка списка 
def filter_counrty(id=1):
    pass