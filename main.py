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

def start():
    user = "user"
    version = "v0.1-alpha"

    console(user, version)

try:
    import prepared_responses as p_responses

    print("Success!")
    start()
except:
    print("Error!")