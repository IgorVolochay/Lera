import json

from time import strftime

def check_user():
    '''
    Checks the existence of the "user.json" file. If it does not exist, it offers to create it.
    '''
    print("> Check user...")

    from os.path import exists

    if exists("user.json"):
        pass
    else:
        print("! User not found !", "? Want to create a user ?", sep="\n")
        if input("(n/y): ").lower() in ["y", "1", "yes", "да", "ok", "okay"]:
            create_user()
        else:
            return
    return

def create_user():
    '''
    User creation:
    \nYou are required to enter a "user_name". In addition, "user_id" and "user_registration_date" information is written.
    '''
    print("> User creation...")
    user_name = input("* Enter your name: ")
    user_id = None
    user_registration_date = str(strftime("%d.%m.%Y %H:%M:%S"))

    with open("user.json", "w") as file:
        json.dump({"user": {"user_name": user_name, "user_id": user_id, "user_registration_date": user_registration_date}}, file, indent=2)
        file.close()

def user_info():
    '''
    Collects data about the user from the "user.json" file.
    '''
    with open("user.json", "r") as file:
        data = json.load(file)
        file.close()

    return [data["user"]["user_name"], data["user"]["user_id"], data["user"]["user_registration_date"]]