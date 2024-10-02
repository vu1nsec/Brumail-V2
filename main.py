from colorama import *
from os import system
import os

banner = f"""
{Fore.YELLOW}__________                             .__.____     
\______   \_______ __ __  _____ _____  |__|    |    
 |    |  _/\_  __ \  |  \/     \\\__  \ |  |    |    
 |    |   \ |  | \/  |  /  Y Y  \/ __ \|  |    |___ 
 |______  / |__|  |____/|__|_|  (____  /__|_______ \\
        \/                    \/     \/           \/{Fore.WHITE}
"""

def generating(username, name, lastname, dob, zipcode, email):
    print(f"""
  {Fore.GREEN}+{Fore.WHITE} {username}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}{lastname}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}{name}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}{lastname}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}{name}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {dob}{name}@{email}
  {Fore.GREEN}+{Fore.WHITE} {dob}{lastname}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}{dob}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}{zipcode}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}.{lastname}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}.{name}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}-{lastname}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}-{name}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}{dob}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}{dob}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {dob}{lastname}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {dob}{name}{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}.{lastname}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}.{name}{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}_{lastname}@{email}
  {Fore.GREEN}+{Fore.WHITE} {lastname}_{name}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}_{dob}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}.{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {name}-{zipcode}@{email}
  {Fore.GREEN}+{Fore.WHITE} {username}-{zipcode}@{email}
""")
    


if __name__ == "__main__":
    system('cls')
    system('title BrumailV2')
    cmd = 'mode 110,30'
    os.system(cmd)
    print(banner)

    print("  ! - please type only the domain without the [@]")
    mail = input(f"  {Fore.YELLOW}?{Fore.WHITE} - What E-Mail ? : ")

    system('cls')
    print(banner)
    username = input(f"  {Fore.YELLOW}?{Fore.WHITE} - Username : ")
    name = input(f"  {Fore.YELLOW}?{Fore.WHITE} - Name     : ")
    lastname = input(f"  {Fore.YELLOW}?{Fore.WHITE} - Lastname : ")
    dob = input(f"  {Fore.YELLOW}?{Fore.WHITE} - Dob      : ")
    zipcode = input(f"  {Fore.YELLOW}?{Fore.WHITE} - Zipcode  : ")
    print(f"\n{Fore.GREEN}  !{Fore.WHITE} - Generating E-mails...")
    generating(username=username, name=name, lastname=lastname, dob=dob, zipcode=zipcode, email=mail)

    print(f"{Fore.YELLOW}  ?{Fore.WHITE} - To check if an E-mail is valid, go to : https://email-checker.net/check")
    print(f"{Fore.YELLOW}  ?{Fore.WHITE} - If you find a Valid E-mail, OSINT it using : https://epieos.com/")