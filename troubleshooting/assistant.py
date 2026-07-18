import datetime
from database import troubleshooting_database
from logger import save_log

def find_solution(user_problem):

    user_problem = user_problem.lower()

    for problem in troubleshooting_database:

        if problem in user_problem:
            return troubleshooting_database[problem]

    return None

def troubleshoot():

    problem = input("What IT problem are you having? ")

    solution = find_solution(problem)


    if solution:

        print("\nCategory:", solution["category"])

        print("Severity:", solution["severity"])

        print("\nDescription:")
        print(solution["description"])

        print("\nPossible solutions:")

        for item in solution["solutions"]:
            print("-", item)

        save_log(problem, solution)


    else:

        print("Sorry, I could not find a solution.")
        

while True:

    print("""
========================
       IT HELP HUB
========================

1. Troubleshoot a problem
2. View previous logs
3. Exit

========================
""")


    choice = input("Choose an option: ")


    if choice == "1":

        troubleshoot()


    elif choice == "2":

        print("\nPrevious Logs:\n")

        try:
            with open("logs.txt", "r") as file:
                print(file.read())
 
        except FileNotFoundError:
            print("No logs found yet.")


    elif choice == "3":

        print("Thank you for using IT HelpHub!")
        break


    else:

        print("Invalid option. Please choose 1, 2 or 3.")