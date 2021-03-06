import random
from datetime import datetime, timedelta


def random_str():
    strs = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(random.randint(1, 5), random.randint(6, 10)):
        result += random.choice(strs)
    return result


def random_phone():
    result = '09'
    for i in range(9):
        result += str(random.randint(0, 9))
    return result


def random_email():
    result = random_str()
    result += '@'
    result += random_str()
    result += '.'
    result += random_str()
    return result


def random_date():
    return str(datetime.now() + timedelta(days=random.randint(-9, 9)))


def random_bool():
    return random.choice([False, True])


def main():
    users = {"model": "post.customuser"}
    file_name = './d2.json'
    file = open(file_name, 'w')
    file.write('[')
    for i in range(1000, 3000):
        users['pk'] = i
        users['fields'] = {
            "password": random_str(),
            "last_login": random_date(),
            "is_superuser":random_bool(),
            "username": random_str()+str(i),
            "first_name": random_str(),
            "last_name": random_str(),
            "is_staff": random_bool(),
            "is_active": random_bool(),
            "date_joined": random_date(),
            "email": random_email(),
            "phone": random_phone(),
            "adres": random_str(),
            "bio": random_str(),
            "avatar": random_str(),
            "date_sent": random_date(),
            "groups": [],
            "user_permissions": []
        }
        file.write(str(users))
        file.write(',')
    file.write(']')
    file.close()
    file = open(file_name, 'r')
    str1 = file.read().replace("'", '"')
    str1 = str1.replace('False', 'false')
    str1 = str1.replace('True', 'true')
    file = open(file_name, 'w')
    file.write(str1)
    file.close()
    #end users

    


    print('ok')


if __name__ == "__main__":
    main()
