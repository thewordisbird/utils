import sys
import subprocess
from os import path
import re
'''
Utility to modify the commit author. 

Used to merge two git accounts, or upadate log if commits made from wrong
acct.

Usage:
Add the path to the git repository as an argument on run:
    python3 modify_log.py path/to/git

example path:
    /Users/justinbird/code/flask_snippets
'''

MAIL_MAP = '/Users/justinbird/desktop/mailmap'
REMOTE = 'https://github.com/thewordisbird/'

project_path = sys.argv[1]

# validate path:
if not path.exists(project_path + '/.git'):
    print('There is not git repository in this path')
    exit()

git_path = project_path + '/git'

# Check remote
# result_remote = subprocess.run(['git', 'remote', '-v'], cwd=project_path, capture_output=True)
# result_remote = result_remote.stdout.decode("utf-8")
# print(result_remote)
# verify_remote = input('Do you want to modify the remote address? (y/n): ')
# if verify_remote.lower() == 'y':
#     new_remote = input('Enter the new remote: ')
#     subprocess.run(['git', 'remote', 'set-url', 'origin', new_remote], cwd=project_path)
#     print(f'The remote has been updated to: {new_remote}')

# Display log and confirm update with mailmap
result_log = subprocess.run(['git', 'log'], cwd=project_path, capture_output=True)
result_log = result_log.stdout.decode("utf-8")
print(result_log)
verify_author = input('Do you want to modify the remote author? (y/n)')
if verify_author.lower() == 'y':
    # path_mailmap = input('Enter path to mailmap file: ')
    # Validate mailmap exists
    # if not path.exists(path_mailmap):
    #     print('Invalid Path')
    #     exit()
    
    if input('WARNING: Continuing will rewite commit history. Continue? (y/n) :') == 'y':
        subprocess.run(['git', 'filter-repo', '--mailmap', MAIL_MAP, '--force'], cwd=project_path)
    

# Set new remote:
repo_name = input('Enter the repository name: ')
remote_url = REMOTE + repo_name +'.git'
subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=project_path)
print(f'The remote has been set to: {remote_url}')

# Push updates to remote
subprocess.run(['git', 'push', 'origin', '--all'], cwd=project_path)



