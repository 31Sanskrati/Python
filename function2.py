#Defining a function to store age
def get_age():
    age = int(input("Enter your age :"))
    return age

# Defining a function to get name
def get_name():
    name = input("Enter your name : ")
    return name

#Defining main function
def Main():
    print("Starting ....")
    age = get_age()
    Myname = get_name()
    print("My name is ", Myname, "and I am ", age, "years old")
    print("The End ^_^ ")

#telling python about main function existance
if __name__ == "__main__":
    Main()

