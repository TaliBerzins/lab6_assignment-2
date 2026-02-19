#Creating dictonary for username, pwd pairs
user_dict = {"guest": "guest", 'TAB': 'pwd', 'tberzins': 'ri74', 'gwalters': 'mango'}
user_username_input = input("Enter your username:")
#Checking if pwd's and usernames entered by user match
if user_username_input in user_dict.keys() and user_username_input == 'guest':
    user_pwd_input = input("Enter your password:")
    user_attemps : int = 1
#Creating while loop for user to attempt password 3 times
    while(user_attemps<3):
        if user_pwd_input == user_dict[user_username_input]:
         print("You have guest acess")
         break
        elif user_pwd_input != user_dict[user_username_input]:
             print("Wrong password")
             user_attemps += 1
             user_pwd_input = input("Enter your password:")
if user_attemps>=3:
     print("MAXIMUM NUMBER OF ATTEMPTS")
#Creating case for if username is not guest username
elif user_username_input in user_dict.keys():
     user_pwd_input = input("Enter your password:")
     if user_pwd_input == user_dict[user_username_input]:
             print(f"Welcome {user_username_input}. You have level 1 access")
     elif user_pwd_input != user_dict[user_username_input]:
         print("Wrong password")

else:
     user_username_input = input("No such userName, enter again")
   




