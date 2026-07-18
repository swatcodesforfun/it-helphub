import socket
import platform
import urllib.request

print("""

==========================
 IT HelpHub Network Checker
==========================
""")

hostname = socket.gethostname()


print("Computer Name:", hostname)

ip_address = socket.gethostbyname(hostname)

print("Local IP Address:", ip_address)

try:

    urllib.request.urlopen("https://www.google.com", timeout=5)

    internet_status = True

    print("Internet Connection: Available")


except:

    internet_status = False

    print("Internet Connection: Not Available")

    

print("\nTroubleshooting Advice:")


if internet_status:

    print("- Your computer can access the internet.")
    print("- If a website is not working, the problem may be with that service.")


else:

    print("- Restart your router.")
    print("- Check your WiFi connection.")
    print("- Restart your computer.")