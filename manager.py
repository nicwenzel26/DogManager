import dog
import datetime
import sqlite3

# Function for creating the table/SQLite DB
def create_db():
    # Establishing a connection to a database
    conn = sqlite3.connect("dog_database.db")
    curr = conn.cursor()

    # SQL command to create a table in the database
    create_table = """ CREATE TABLE DOG_DATA (
    name VARCHAR(50),
    age INT,
    sex VARCHAR(1),
    DOB TEXT,
    last_heat TEXT,
    next_heat TEXT
    );"""

    # Only create a table if it does not already exist
    try:
        curr.execute(create_table)
    except:
        pass
    finally:
        conn.commit()

# Function for decoposing a string into date time object
def decomp_date(date):
    date_lst = date.split('/')
    month = int(date_lst[0])
    day = int(date_lst[1])
    year = int(date_lst[2])

    return datetime.datetime(year, month, day)

# Function to add a dog to the system
def new_dog():
    # Getting the dogs information from the user
    last_heat_real = None
    next_heat = None
    name = input("Enter new dog name: ")
    sex = input("Enter the dogs sex (M/F): ")
    # Making sure the dog has a valid sex
    while sex != "M" and sex != "F":
        sex = input("Enter valid sex (M/F): ")
    # TODO make sure date is valid
    dob = input("Enter DOB (9/26/1998): ")
    dob_real = decomp_date(dob)

    today = datetime.date.today()

    age = today.year - dob_real.year - ((today.month, today.day) < (dob_real.month, dob_real.day))

    if sex == "F":
        last_heat = input("Enter last heat cycle date (5/2/1967): ")
        last_heat_real = decomp_date(last_heat)

    conn = sqlite3.connect("dog_database.db")
    curr = conn.cursor()

    add_dog = """INSERT INTO DOG_DATA VALUES('{name}', '{age}', '{sex}', '{dob}', '{last_heat}', '{next_heat}');""".format(name = name, age = age, sex = sex, dob = dob_real, last_heat = last_heat_real, next_heat = next_heat)

    try:
        curr.execute(add_dog)
        print("\n" + name + " added!\n")
    except:
        print("Failed to add dog to database.")
    finally:
        conn.commit()


# Function to show all the dogs info that is currently in the system
def show_all_dogs():
    conn = sqlite3.connect("dog_database.db")
    curr = conn.cursor()

    fetchdata = "SELECT * FROM DOG_DATA"
    curr.execute(fetchdata)
    res = curr.fetchall()

    for data in res:
        print(data)

def main():
    print("==========WELCOME TO DOG MANAGER V0.01============\n")

    create_db()

    x = 0;
    while x != "quit":
        print("\nOPTIONS:")
        print("1: Input New Dog")
        print("2: Show Dogs")
        print("3: Quit")
        x = input("Option: ")
        x = x.lower()

        if x == "1" or x == "input new dog":
            print("\n")
            new_dog()
        elif x == "2" or x == "show dogs":
            show_all_dogs()

main()
