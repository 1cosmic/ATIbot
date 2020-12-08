# Made by 1cosmic.
# ATI-Bot = лучший хак для атишки. 
#
# Client ID: d66d3fca842845e7ab2e0e9eb2c8667e
# CRM: 1f1b1c7bfa114d0ab2ccfd8c80352666
# ATI Кабинет: 7c61a4904fc84c80add3c4a871134c9f
#
# С этим access_token вы можете вызывать методы API. 
# Передавайте его в заголовке Authorization: Bearer <токен>. Например:
# Authorization:Bearer 7c61a4904fc84c80add3c4a871134c9f
import requests
import json

class ATIBot:
   def __init__(self):   
      self.base_url = 'http://api.ati.su/'
      self.headers = {'Authorization': 'Bearer 7c61a4904fc84c80add3c4a871134c9f'}

   def setUrl(self, new_url):
      self.base_url = (self.base_url + new_url)

      return 'Установлен новый url: {}'.format(self.base_url)

   def getResponse(self):
      connect = requests.get(self.base_url, headers=self.headers)
      
      return connect

   # Получить все грузы и записать их в cargo.json
   def getCargo(self, id=0):
      connect = requests.get(self.base_url + f'loads?contactId={id}', headers=self.headers)
      self.all_cargo = connect.json()

      # создаём читаемый джейсон файл всех грузов.
      with open('cargo.json', 'w') as file: # записываем в файл

         #sort_keys и indent - преобразовывают джейсон в читаемый вид
         json.dump(self.all_cargo, file, sort_keys=True, indent=4)

      return self.all_cargo

   def addCargo(self, cargo=None):
      self.cargo = cargo

   def getCity(self):
      connect = requests.get(self.base_url + f"dictionaries/cities", headers=self.headers)
      self.city = connect.json()

      with open('city.json', 'w') as file:
         json.dump(self.city, file, sort_keys=True,
                   indent=4, ensure_ascii=False)
         print('Города успешно загружены.')

      return self.city
###
bot = ATIBot() # инициализируем бота

bot.getCargo() # получаем все грузы контакта (по деф. ContactID=0)
print('Грузы контакта успешно загружены.')

bot.getCity() # получаем всевозможные города в БД АТИ
