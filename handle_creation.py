import os
import platform as pt
from pathlib import Path


class HandleCreation:
    def __init__(self, user_path):
        self.os = pt.platform()
        self.home_directory = os.path.expanduser("~")
        self.main_dir = "100DaysOfCode"
        self.default_dir = (
            f"{self.home_directory}/{self.main_dir}"
            if user_path == ""
            else f"{user_path}/{self.main_dir}"
        )
        print(self.default_dir)
        self.readme_path = f"{self.default_dir}/README.md"
        self.gitignore_path = f"{self.default_dir}/.gitignore"

    def create_main_folder(self):
        """
        Creates the main folder
        """
        self.main_dir = Path(self.default_dir).mkdir(
            parents=True, exist_ok=True
        )

    def create_readme(self):
        """
        Creates a README.md file and adds basic info about 100DaysOfCode.
        """
        # Path for the readme file
        readme_path = Path(self.readme_path)

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

    def create_gitignore(self):
        """
        Creates a .gitignore file and adds pre-made folders in it.
        """
        # Path for gitignore file
        gitignore_path = Path(self.gitignore_path)
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

    def create_folders(self):
        """
        Creates 100 Folders with the pattern 'Day_<number>' with a README file to
        document the things that were learnt that day.
        """

        for day_num in range(1, 101):
            folder_path = Path(self.default_dir + f"/Day_{day_num}")
            if folder_path.is_dir():
                print("Already Exists! Continuing")
            else:
                # make a new folder for each loop
                Path(self.default_dir + f"/Day_{day_num}").mkdir(
                    parents=True, exist_ok=True
                )

                # get the new folder path
                done = self.default_dir + f"/Day_{day_num}"

                # Make required files and folder
                Path(done + "/README.md").touch(mode=0o666, exist_ok=True)

                # Write contents in README.md file
                readme_path = Path(done + "/README.md")
                with open(readme_path, "a+") as readme_file:
                    readme_file.writelines(
                        f"# Day {day_num}\n\n" + "## Things I Learned\n\n"
                    )
