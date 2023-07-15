import os
from github import Github
from dotenv import load_dotenv
import subprocess

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error: {error}")
    return output

def update_github():
    # Load environment variables from .env file
    load_dotenv()

    # Check if the current directory is a Git repository
    if not os.path.exists('.git'):
        print("Git repository has not been initialized. Initializing now...")
        run_command('git init')

    # Get the GitHub token from the environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        print("GitHub token not found in .env file.")
        return

    # Prompt the user for the necessary information
    repo_name = input("Enter the name of the GitHub repository: ")
    commit_message = input("Enter a commit message: ")

    # Create a GitHub object using the provided token
    g = Github(github_token)

    # Get the user
    user = g.get_user()

    # Create a new repository if it doesn't exist
    if repo_name not in [repo.name for repo in user.get_repos()]:
        user.create_repo(repo_name)

    # Add all the files in the current directory to the staging area
    run_command('git add .')

    # Commit the changes
    run_command(f'git commit -m "{commit_message}"')

    # Push the changes to GitHub
    run_command(f'git remote add origin https://github.com/{user.login}/{repo_name}.git')
    run_command('git push -u origin master')

if __name__ == "__main__":
    update_github()
