import employee
import pickle

# Global constant for the filename
FILENAME = 'employees.dat'

# The get_menu_choice function displays the menu and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee info')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

def load_employees():
    try:
        # Open the file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        emp_dct = pickle.load(input_file)

        # Close the file.
        input_file.close()
    except IOError:
        # Could not open the file, so create an empty dictionary.
        emp_dct = {}

    # Return the dictionary.
    return emp_dct

# main function
def main():
    # Load the existing dictionary and assign it to emp.
    emp = load_employees()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user wants to quit the program.
    while choice != 5:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == 1:
            look_up(emp)
        elif choice == 2:
            new_emp = getEmployee(emp)
            id_number = new_emp.getID()
            if id_number not in emp:
                emp[id_number] = new_emp
                print("The new employee has been added.")
            else:
                print("That ID number already exists.")
        elif choice == 3:
            change(emp)
        elif choice == 4:
            id_number = int(input("Enter an employee ID number: "))
            if id_number in emp:
                del emp[id_number]
                print("Employee information deleted.")
            else:
                print("The ID number was not found")
        elif choice == 5:
            # Save the emp dictionary to a file.
            save_employees(emp)
            print("Saving and quitting...")
        else:
            print("Invalid choice")



# The look_up function looks up an item in the specified dictionary.
def look_up(emp):
    # get emp id from user
    id = int(input("Enter an employee ID number: "))
    # verify if exists in dict
    if id in emp:
        print(emp[id])
    else:
        print("The specified ID number was not found")

# This function adds a new entry into the specified dictionary.
def getEmployee(emp):
    name = input("Enter employee name: ")
    id_number = int(input("Enter employee ID number: "))
    department = input("Enter employee department: ")
    job_title = input("Enter employee job title: ")
    
    entry = employee.Employee(name, id_number, department, job_title)
    
    return entry
    

# The change function changes an existing entry in the specified dictionary.
def change(emp):
    
    id_number = int(input("Enter an employee ID number: "))
    if id_number in emp:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        job_title = input("Enter the new job title: ")
        
        entry = employee.Employee(name, id_number, department, job_title)
        
        emp[id_number] = entry
        print("Employee information updated.")
    else:
        print("The specified ID number was not found")

# The funtion pickles the specified object and saves it to the file.
def save_employees(emp):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(emp, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
if __name__ == '__main__':
    main()

    
