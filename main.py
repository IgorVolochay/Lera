'''
Name: Lera
Version: v0.1-alpha
Description: Nothing yet
'''

class console():
    def __init__(self, user, user_id, version):
        self.user = user
        self.user_id = user_id
        self.version = version
        
        self.command()
        
    def command(self):
        while True:
            self.command_text = input()

            if extractOne(self.command_text, ["info", "information", ])[1] > 80:
                print(extractOne(self.command_text, ["info", "information"]))
                p_responses.__info__(self.version, self.user, self.user_id)
            elif self.command_text == "exit":
                break

try:
    print("> Start programm...")

    import prepared_responses as p_responses
    import user_options

    from import_moduls import install

    try:
        from fuzzywuzzy.process import extractOne
    except:
        print("! You don't have some modules downloaded !", "? Install them ?", sep="\n")
        if input("(n\y): ").lower() in ["y", "1", "yes", "да", "ok", "okay"]:
            install(["fuzzywuzzy"])
        else:
            exit()

    user_options.check_user()

    print("> Success start!")
    console(user_options.user_info()[0], user_options.user_info()[1], "v0.1-alpha" )
except:
    print("> Error!")