"""
A banking system to integrate with my stock sim and SOLUS.
"""
import absolute_url


def access_account(username):
    file = absolute_url.absolute_url + username.lower() + '.json'

    with open(file, 'r') as user_file:
        user_info = user_file.readlines()
