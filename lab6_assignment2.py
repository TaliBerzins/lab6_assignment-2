user_dict = {"guest": "guest", 'TAB': 'pwd', 'tberzins': 'ri74', 'gwalters': 'mango'}
user_username_input = input("Enter your username:")
if user_username_input in user_dict.keys():
    print(user_username_input)
    user_pwd_input = input("Enter your password:")
    if user_pwd_input == user_dict[user_username_input]:
        print("You printed correct pwd")


