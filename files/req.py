import requests
from bs4 import BeautifulSoup

url = "https://edu.donstu.ru/WebApp/#/Rasp/Group/50918'"  # Замените на URL вашего сайта
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    print(response.text)

else:
    print('Ошибка при загрузке страницы')


# soup = BeautifulSoup(html, 'html.parser')

# page = soup.find('div', class_="mt-2") 
# print(f'text: {page}')

# a = [1,2,3,4,5,6]
# for i in range(len(a)):
#     print(a[i])