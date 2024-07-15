import sys
import os
from pathlib import Path
from colorama import init, Fore

# Initialize colorama for color support in terminal
init(autoreset=True)

def show_directory_structure(path, indent_level=0):
    try:
        # Iterate over each item in the directory
        for item in path.iterdir():
            # Define paddings for formatting (4 spaces per level)
            indent = ' ' * 4 * indent_level
            if item.is_dir():
                # Print the directory name in blue
                print(Fore.BLUE + f"{indent}{item.name}/")
                # Recursively call the function for nested directories
                show_directory_structure(item, indent_level + 1)
            else:
                # Print the file name in green
                print(Fore.GREEN + f"{indent}{item.name}")
    except PermissionError:
        # Print a message if there is a permission error
        print(Fore.RED + f"{indent}Permission denied: {item}")

def visualize_directory_structure(path):
    path = Path(path)
    if not path.exists():
        print(Fore.RED + f"Error: The path {path} does not exist.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Error: The path {path} is not a directory.")
        return

    show_directory_structure(path)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task_03.py <path_to_directory>")
    else:
        # Get the directory path from the command line arguments
        directory_path = sys.argv[1]
        # Call the function to visualize the directory structure
        visualize_directory_structure(directory_path)
