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

def init_github_repo():

  # Load env variables
  load_dotenv()
  github_token = os.getenv('GITHUB_TOKEN')

  if not github_token:
    print("GitHub token not found")
    return

  # Create GitHub object
  g = Github(github_token)

  # Get user
  user = g.get_user()

  # Set repo name
  repo_name = "basicGoldBot"

  # Create README
  with open("README.md", "w") as f:
    f.write("# "+repo_name)

  # Initialize Git repo
  run_command("git init")

  # Add and commit README
  run_command("git add README.md")
  run_command('git commit -m "first commit"')

  # Check if remote exists, if not, add it
  remotes = run_command("git remote").decode().split("\n")
  if "origin" not in remotes:
    run_command(f'git remote add origin https://github.com/{user.login}/{repo_name}.git')

  # Push to GitHub
  run_command("git push -u origin master")

if __name__ == "__main__":
  init_github_repo()
