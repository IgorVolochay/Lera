import json

from time import strftime

def check_user():
    print("> Check user...")

    from os.path import exists

    if exists("user.json"):
        pass
    else:
        print("! User not found !", "? Want to create a user ?", sep="\n")
        answer = input("(n/y): ").lower()
        if answer == "y":
            create_user()
        else:
            return
    return

def create_user():
    user_name = input("* Enter your name: ")
    user_id = None
    user_registration_date = str(strftime("%d.%m.%Y %H:%M:%S"))

    with open("user.json", "w") as file:
        json.dump({"user": {"user_name": user_name, "user_id": user_id, "user_registration_date": user_registration_date}}, file, indent=2)
        file.close()

def user_info():
    with open("user.json", "r") as file:
        data = json.load(file)
        file.close()

    return [data["user"]["user_name"], data["user"]["user_id"], data["user"]["user_registration_date"]]