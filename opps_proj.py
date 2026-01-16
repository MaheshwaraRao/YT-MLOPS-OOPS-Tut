class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(''' 
                           Welcome to ChatBook how would you like to proceed?
                           1. Login press 1
                           2. Sign Up press 2
                           3. Press 3 to write a post
                           4. Press 4 to messsage a friend
                           5. Press anyother key to exit
                           ''')
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print('Exiting ChatBook. Have a nice day!')
            exit()

obj = chatbook()



