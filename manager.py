import dog
import datetime

# Function to add a dog to the system
def new_dog():
    # Getting the dogs information from the user
    name = input("Enter new dog name: ")
    age = input("Enter dog age in years: ")
    sex = input("Enter dog sex (M/F): ")

    # Writing the infomration to text file. Should probably be database in the future
    with open("dogs.txt", "a") as dog_file:
        dog_file.write(name + " " + age + " " + sex + "\n")

    print("Successfully added: {name}, Age: {age}, Sex: {sex}".format(name = name, age = age, sex = sex))

# Function to show all the dogs info that is currently in the system
def show_all_dogs():
    print("Name:\tAge:\tSex:")
    with open("dogs.txt") as dog_file:
        lines = dog_file.readlines()
        for line in lines:
            spl = line.split(" ")
            print(spl[0] + "\t" + spl[1] + "\t" + spl[2])

def main():
    print("==========WELCOME TO DOG MANAGER V0.01============\n")
    x = 0;
    while x != "quit":
        print("OPTIONS:")
        print("1: Input New Dog")
        print("2: Show Dogs")
        print("Quit")
        x = input("Option: ")
        x = x.lower()

        if x == "1" or x == "input new dog":
            new_dog()
        elif x == "2" or x == "show dogs":
            show_all_dogs()

main()
