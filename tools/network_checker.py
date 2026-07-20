import socket
import platform
import urllib.request
import datetime

print("""
========================================
        IT HELPHUB NETWORK REPORT
========================================
""")

hostname = socket.gethostname()
current_time = datetime.datetime.now()
ip_address = socket.gethostbyname(hostname)

print("Computer Name     :", hostname)
print("Operating System  :", platform.system())
print("Local IP Address  :", ip_address)

try:

    urllib.request.urlopen("https://www.google.com", timeout=5)

    internet_status = True

    print("Internet Connection: Connected")


except:

    internet_status = False

    print("Internet Connection: Not Connected")



print("\nTroubleshooting Advice:")


if internet_status:

    print("- Your computer can access the internet.")
    print("- If a website is not working, the problem may be with that service.")


else:

    print("- Restart your router.")
    print("- Check your WiFi connection.")
    print("- Restart your computer.")


print("\nStatus:")

if internet_status:
    print("✓ Your network appears to be working normally.")
else:
    print("✗ A network issue was detected.")
    print("Try restarting your router or checking your WiFi.")

print("\n========================================")
print("Report generated:", current_time)
print("========================================")