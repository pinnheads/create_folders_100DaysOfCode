import os
from handle_creation import HandleCreation

# Get the default dir
default_dir = os.path.expanduser("~") + "/Code"

print("-" * 100)
# Ask user for the desired path
user_dir = input(f"Enter a directory of your choice(default: {default_dir}):\n")

print("\n\n")

# If no dir is passed
if user_dir == "":
    fd = HandleCreation(default_dir)
else:
    fd = HandleCreation(user_dir)

# Create main folder
fd.create_main_folder()

# Create README at root level
fd.create_readme()

# Create .gitignore at root level
fd.create_gitignore()

# Create Folders
fd.create_folders()

print("\nDone")
print("-" * 100)
