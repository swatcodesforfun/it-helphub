import platform

def get_system_info():
    operating_system = platform.system()
    computer_name = platform.node()
    processor = platform.processor()
    python_version = platform.python_version()

    system_info = {
        "Operating System": operating_system,
        "Computer Name": computer_name,
        "Processor": processor,
        "Python Version": python_version
    }

    return system_info

def display_report(system_info):
    print("=" * 40)
    print("       IT HELP HUB REPORT")
    print("=" * 40)

    for key, value in system_info.items():
        print(key + ":", value)
  

    
information = get_system_info()

display_report(information)