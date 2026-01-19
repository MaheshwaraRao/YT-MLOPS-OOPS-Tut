class ChatBook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        while True:
            user_input = input(''' 
Welcome to ChatBook! How would you like to proceed?
1. Login
2. Sign Up
3. Write a post
4. Message a friend
5. Exit
Enter your choice: ''')

            if user_input == '1':
                self.signin()
            elif user_input == '2':
                self.signup()
            elif user_input == '3':
                self.write_post()
            elif user_input == '4':
                self.send_message()
            else:
                print('Exiting ChatBook. Have a nice day!')
                break

    def signup(self):
        email = input('Enter your email: ')
        pwd = input('Enter your password: ')
        self.username = email
        self.password = pwd
        print('Sign up successful! You can now log in.\n')

    def signin(self):
        if not self.username or not self.password:
            print("No user found, please sign up first.\n")
            return

        email = input('Enter your email: ')
        pwd = input('Enter your password: ')

        if email == self.username and pwd == self.password:
            self.loggedin = True
            print('Login successful! Welcome back.\n')
        else:
            print('Login failed! Incorrect email or password.\n')

    def write_post(self):
        if self.loggedin:
            txt = input('Write your post here: ')
            print('Your post has been published!\n')
        else:
            print('Please log in to write a post.\n')

    def send_message(self):
        if self.loggedin:
            txt = input('Enter your message here: ')
            frnd = input('Enter whom to send: ')
            print(f'Message sent to {frnd}!\n')
        else:
            print('Please log in to send messages.\n')


obj = ChatBook()
