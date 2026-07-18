troubleshooting_database = {

    "wifi": {
        "category": "Networking",
        "description": "Problems connecting to WiFi or accessing the internet.",
        "solutions": [
            "Restart your router",
            "Restart your computer",
            "Forget the WiFi network and reconnect",
            "Check if other devices can access the internet"
        ]
    },


    "slow computer": {
        "category": "Performance",
        "description": "Computer running slowly or freezing.",
        "solutions": [
            "Close unnecessary programs",
            "Restart your computer",
            "Check available storage space",
            "Disable unnecessary startup applications"
        ]
    }

}

problem = input("Hello, what IT problem are you having?")

if problem in troubleshooting_database:

    issue = troubleshooting_database[problem]

    print("\nCategory:", issue["category"])

    print("\nDescription:")
    print(issue["description"])

    print("\nPossible solutions:")

    for solution in issue["solutions"]:
        print("-", solution)