'''
Name: Lera
Version: v0.1-alpha
Description: Nothing yet
'''

class console():
    def __init__(self, user, version):
        self.user = user
        self.version = version

        self.command()
        
    def command(self):
        while True:
            self.command_text = input()

            if self.command_text == "info":
                p_responses.__info__(self.version, self.user)
            elif self.command_text == "exit":
                break

try:
    print("> Start programm...")

    import prepared_responses as p_responses
    import user_options

    user_options.check_user()
    user = user_options.user_info()[0]
    version = "v0.1-alpha"    

    print("> Success start!")
    console(user, version)
except:
    print("> Error!")