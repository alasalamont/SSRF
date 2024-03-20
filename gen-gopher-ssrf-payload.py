#!/usr/bin/python3

#Note
#This file will give the option for user to choose. It will call 4 files as follow:
#1. option-1-gopher-get.py
#2. option-2-gopher-post-url.py
#3. option-3-gopher-post-json
#4. option-4-gopher-post-basic`
#→ Need to put the above 4 files together with this file

from colorama import Fore, Back, Style, init
init(autoreset=True)  # Auto reset color for each print
import os
import subprocess

def main_menu():
    print(f"""
{Style.BRIGHT}[+] Option-1. {Fore.GREEN}gopher-get{Style.RESET_ALL}{Style.BRIGHT}: access to a specific endpoint/file
{Style.BRIGHT}[+] Option-2. {Fore.GREEN}gopher-post-url{Style.RESET_ALL}{Style.BRIGHT}: send data to a specific endpoint/file via {Fore.GREEN}URL{Style.RESET_ALL}{Style.BRIGHT}
{Style.BRIGHT}[+] Option-3. {Fore.GREEN}gopher-post-json{Style.RESET_ALL}{Style.BRIGHT}: send data to a specific endpoint/file, the data-sent is in {Fore.GREEN}json format{Style.RESET_ALL}{Style.BRIGHT}
{Style.BRIGHT}[+] Option-4. {Fore.GREEN}gopher-post-normal{Style.RESET_ALL}{Style.BRIGHT}: send data to a specific endpoint/file, the data-sent is in {Fore.GREEN}www-form-urlencoded format{Style.RESET_ALL}{Style.BRIGHT}

{Style.BRIGHT}+ Please choose your option:""")


def run_script(option):
    script_path = f"./option{option}.py"
    if os.path.exists(script_path):
        subprocess.run(["python3", script_path], check=True)
    else:
        print(f"Error: The script for option {option} does not exist.")

if __name__ == "__main__":
    main_menu()
    try:
        choice = int(input(f"{Style.BRIGHT}→ Your choice (1-4): "))
        if choice in range(1, 5):
            run_script(choice)
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
    except ValueError:
        print("Please enter a numeric value.")

