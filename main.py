# Import Libraries
import os
import platform as pt
from pathlib import Path

# Get current working directory
current_os = pt.platform()
print(os.path.expanduser("~"))
pwd = os.getcwd()

# Make a folder called "100DaysOfCode"
Path(pwd + "/100DaysOfCode").mkdir(parents=True, exist_ok=True)
pwd += "/100DaysOfCode"
print(pwd)


def create_readme(default_path):
    """
    Creates a README.md file and adds basic info about 100DaysOfCode.
    """
    # Path for the readme file
    readme_path = Path(default_path + "/README.md")

    # Check if it already exists
    if readme_path.is_file():
        print("File already exists! Skipping this step.")
    else:
        # Create the file if it doesn't exist already
        readme_path.touch(mode=0o666, exist_ok=True)
        with open(readme_path, "a+") as readme_file:
            # Basic info about 100 Days Of Code
            readme_file.writelines(
                "# What is 100 Days of Code?\n\n"
                + "- It is just as the name suggests, you code for 100 days, everyday.\n\n"
                + "## The Rules\n\n"
                + "1. Code minimum an hour every day for the next 100 days.\n"
                + "2. Tweet your progress every day with the #100DaysOfCode hashtag.\n"
                + "3. Upload to Github\n\n"
                + "### Official Site for 100 Days Of Code for More Information\n\n"
                + "<https://www.100daysofcode.com/>\n\n"
                + "## My Progress\n\n"
            )
            for day_num in range(1, 101):
                readme_file.write(f"- [ ] Day_{day_num}\n")
        print(
            f"README file was created at {readme_path}! Edit it as you like :)"
        )


def create_gitignore(default_path):
    """
    Creates a .gitignore file and adds pre-made folders in it.
    """
    # Path for gitignore file
    gitignore_path = Path(default_path + "/.gitignore")
    if gitignore_path.is_file():
        print("File already exists! Skipping this step.")
    else:
        gitignore_path.touch(mode=0o666, exist_ok=True)
        with open(gitignore_path, "a+") as gitignore_file:
            for day_num in range(1, 101):
                gitignore_file.write(f"Day_{day_num}/\n")
            gitignore_file.writelines(
                "*/*.log\n" + "Day_*/__pycache__/\n" + ".vscode\n"
            )


def create_folders():
    """
    Creates 100 Folders with the pattern 'Day_<number>' with a README file to
    document the things that were learnt that day.
    """

    for day_num in range(1, 101):
        folder_path = Path(default_path + f"/Day_{day_num}")
        if folder_path.is_dir():
            print("Already Exists! Continuing")
        else:
            # make a new folder for each loop
            Path(default_path + f"/Day_{day_num}").mkdir(
                parents=True, exist_ok=True
            )

            # get the new folder path
            done = default_path + f"/Day_{day_num}"

            # Make required files and folder
            Path(done + "/README.md").touch(mode=0o666, exist_ok=True)

            # Write contents in README.md file
            readme_path = Path(done + "/README.md")
            with open(readme_path, "a+") as readme_file:
                readme_file.writelines(
                    f"# Day {day_num}\n\n" + "## Things I Learned\n\n"
                )


create_readme()
create_gitignore()
create_folders()
