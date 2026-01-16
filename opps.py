# initiste a class

class employee:
    def __init__(self):
        self.id = 1
        self.salary = 5000
        self.designation = 'SDE'
        print('The sttributes have been initialised')

    def travel(self, destination):
        print("Employee is not travelling to destination")
        print(f"The destination is {destination}")

# Create an instace of class
sam = employee()

print(sam)