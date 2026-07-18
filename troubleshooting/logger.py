import datetime

def save_log(problem, solution):
    with open("logs.txt", "a") as file:

        file.write("--------------------------------\n")
        file.write("IT HelpHub Log\n\n")
        file.write("Time: ")
        file.write(str(datetime.datetime.now()))
        file.write("\n\n")

        file.write("Problem:\n")
        file.write(problem + "\n\n")

        file.write("Category: ")
        file.write(solution["category"] + "\n")

        file.write("Severity: ")
        file.write(solution["severity"] + "\n\n")

        file.write("Solution Provided:\n")

        for item in solution["solutions"]:
            file.write("- " + item + "\n")

        file.write("--------------------------------\n\n")
