"""
A banking system to integrate with my stock sim and SOLUS.
"""
import absolute_url
import passlib.hash
import json


def access_account(username):
    file = absolute_url.absolute_url + username.lower() + '.json'
    try:
        with open(file, 'r') as user_file:
            user_info = json.load(user_file)
        return user_info
    except FileNotFoundError:
        return "Account does not exist!"


def cli_login():
    username = input("Enter your username:\n")
    password = input("Enter your password:\n")

    user_info = access_account(username)
    if type(user_info) == str:
        print(user_info)
        cli_login()
    else:
        print(user_info)
        print(type(user_info))
        if passlib.hash.sha512_crypt.verify(password, user_info['Pass']):
            print("Logged in as " + username)
        else:
            print("Incorrect password!")


cli_login()
