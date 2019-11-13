import requests, random, sys

countryCode = ""
number = ""
countIterations = 0

for argumentIndex in range(len(sys.argv)):
    if (argumentIndex == 1):
        countryCode = sys.argv[argumentIndex]
    elif (argumentIndex == 2):
        number = sys.argv[argumentIndex]
    elif (argumentIndex == 3):
        countIterations = int(sys.argv[argumentIndex])
    

for i in range(countIterations):
    login = "John" + str(random.randint(0, 100000))
    data = {
        'userLogin': login,
        'userPassword': "123Hohn113",
        'userPassword2': "123Hohn113",
        'userEmail': 'john@gmail.com',
        'userName': "John Alderson",
        'countrycode': countryCode,
        'userPhone': number,
        'userPromo': ""
    }

    url = "https://www.smsfeedback.ru/users/registration/add.php"

    res = requests.post(url, data)
    
    if (res.status_code == 200):
        print("Everything is ok.")
        res.encoding = res.apparent_encoding
        print(res.text)