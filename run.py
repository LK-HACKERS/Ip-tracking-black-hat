import socket
import sys
import os


def print_banner():
    banner = """

 ██╗██████╗
 ██║██╔══██╗
 ██║██████╔╝
 ██║██╔═══╝
 ██║██║
 ╚═╝╚═╝

 ████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
    ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
    ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

    ---------------------------------------------
    [ TARGET: IP ADDRESS TRACKING LK-HACKERS BLACK HAT TOOL ]
    [ DEVELOPED BY: CYBER BLACK LION ]
    ---------------------------------------------
    """
    print("\033[1;31m" + banner + "\033[0m")

def get_ip():
    print("\033[1;33m[!] Ready to hunt IP address...\033[0m")


    target = input("\033[1;32mEnter Target Website (e.g., google.com): \033[0m").strip()


    if target.startswith("http://"):
        target = target.replace("http://", "")
    elif target.startswith("https://"):
        target = target.replace("https://", "")

    if target.endswith("/"):
        target = target[:-1]

    try:

        ip_address = socket.gethostbyname(target)
        print("\n" + "="*40)
        print(f"\033[1;36m TARGET: {target}\033[0m")
        print(f"\033[1;32m IP ADDRESS: {ip_address}\033[0m")
        print("="*40)
        print("\033[1;31m[+] Process Completed ip Tracking Successfully! \033[0m")

    except socket.gaierror:
        print("\n\033[1;31m ERROR: Invalid URL or Domain not found! 💀\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m CRITICAL ERROR: {str(e)}\033[0m")

if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')
    print_banner()
    get_ip()
