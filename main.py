# Import Libraries
import os
from handle_creation import HandleCreation


default_dir = os.path.expanduser("~") + "/Code"
user_dir = input(f"Enter a directory of your choice(default: {default_dir})")

if user_dir == "":
    fd = HandleCreation(default_dir)
else:
    fd = HandleCreation(user_dir)

fd.create_main_folder()
fd.create_readme()
fd.create_gitignore()
fd.create_folders()
