import os
from github import Github
from git import Repo

CommitMessage = 'This is my test commit through CreateRepo.py'
Username = '___'
Password = '___'

#Create a list of folders to create repos
path = "C:/Users/___/Desktop/Python/"
folders = os.listdir(path)

#Remove folders you don't want to create repos
folders.remove('Github')
print(folders)

for folder in folders:
  RepoName = folder
  URL = 'https://github.com/' + Username + '/' + RepoName

  #PyGithub
  #Create New Repo in GitHub if it doesn't exist
  g = Github(Username, Password)
  user = g.get_user()
  try:
    NewRepo = user.create_repo(RepoName)
  except:
    pass

  #GitPython
  #Create local repo at the path
  repo = Repo.init(os.path.join(path, RepoName))

  #Add all files in the directory and commit
  repo.git.add(A=True)
  try:
    repo.git.commit('-m', CommitMessage)
  except:
    pass

  #Push
  try:
    origin = repo.create_remote('origin', url=URL)
  except:
    origin = repo.remotes['origin']

  new_branch = 'MasterBranch'
  current = repo.create_head(new_branch)
  current.checkout()
  master = repo.heads.master
  repo.git.push('--set-upstream', 'origin', master)


