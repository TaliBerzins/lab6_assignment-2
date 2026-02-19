#Creating dictonary for username, pwd pairs
user_dict = {"guest": "guest", 'TAB': 'pwd', 'tberzins': 'ri74', 'gwalters': 'mango'}
user_username_input = input("Enter your username:")
#Checking if pwd's and usernames entered by user match
if user_username_input in user_dict.keys() and user_username_input == 'guest':
    user_pwd_input = input("Enter your password:")
    if user_pwd_input == user_dict[user_username_input]:
        print("You have guest acess")
    elif user_pwd_input != user_dict[user_username_input]:
         print("Wrong password")
#Creating case for if username is not guest username
elif user_username_input in user_dict.keys():
     user_pwd_input = input("Enter your password:")
     if user_pwd_input == user_dict[user_username_input]:
             print(f"Welcome {user_username_input}. You have level 1 access")
     elif user_pwd_input != user_dict[user_username_input]:
         print("Wrong password")

else:
     user_username_input = input("No such userName, enter again")
   




