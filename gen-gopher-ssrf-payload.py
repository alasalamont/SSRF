import os
import subprocess

def main_menu():
    print("""
- Option 1. gopher-get: access to a specific endpoint/file
- Option 2. gopher-post-url: send data to a specific endpoint/file via URL
- Option 3. gopher-post-json: send data to a specific endpoint/file, the data-sent is in json format
- Option 4. gopher-post-normal: send data to a specific endpoint/file, the data-sent is in www-form-urlencoded format

+ Please choose your option:
""")

def run_script(option):
    # Map the option numbers to their corresponding script filenames
    scripts = {
        1: "option-1-gopher-get.py",
        2: "option-2-gopher-post-url.py",
        3: "option-3-gopher-post-json.py",
        4: "option-4-gopher-post-basic.py",
    }
    script_name = scripts.get(option)
    script_path = f"./{script_name}"
    if os.path.exists(script_path):
        subprocess.run(["python3", script_path], check=True)
    else:
        print(f"Error: The script for option {option} does not exist.")

if __name__ == "__main__":
    main_menu()
    try:
        choice = int(input("Your choice (1-4): "))
        if choice in range(1, 5):
            run_script(choice)
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
    except ValueError:
        print("Please enter a numeric value.")
