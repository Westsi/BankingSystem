"""
A banking system to integrate with my stock sim and SOLUS.
"""


def access_account(username):
    file = 'C:/Users/jamie/Desktop/SOLUS/USERS/' + username.lower() + '.json'

    with open(file, 'r') as user_file:
        user_info = user_file.readlines()
