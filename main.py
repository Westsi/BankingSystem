"""
A banking system to integrate with my stock sim and SOLUS.
"""
# imports
import uuid
import json


def create_new_user(username):
    data = {'Username': username, 'UUID': str(uuid.uuid4()), 'Balance': 1000}
    print(data)
    user_list_write = open('user_list.txt', 'a')
    # if data['Username'] not in users:
    try:
        file_for_storage = 'users/' + data['Username'].lower() + '.json'
        with open(file_for_storage, 'x') as file:
            json.dump(data, file)
        user_list_write.write(username.lower() + '\n')
    except FileExistsError:
        print("Username already taken. Please think of a new one!")
        cli_new_user()

    user_list_write.close()


def cli_new_user():
    pref_username = input("Enter a username: \n")
    create_new_user(pref_username.lower())


# user list
user_list = open('user_list.txt', 'r')
users = user_list.readlines()
print(users)
user_list.close()

cli_new_user()