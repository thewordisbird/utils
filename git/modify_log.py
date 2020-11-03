import sys
import subprocess
from os import path
import re
'''
Utility to modify the commit log using filter-remote --mailmap

Used to merge two git accounts, or upadate log if commits made from wrong
acct.

Usage:
Add the path to the git repository as an argument on run:
    python3 modify_log.py path/to/git path/to/mailmap

example path:
    /Users/justinbird/code/flask_snippets
'''
MAIL_MAP = '/Users/justinbird/desktop/mailmap'
GITHUB_BASE = 'https://github.com/'


def validate_git_path(path):
    if not path.exists(path + '/.git'):
        raise ValueError('Invalid Path')


def validate_mailmap_path(path):
    if not path.exists(path):
        raise ValueError('Invalid Path')


def display_warning(message):
    warning = input(f'WARNING: {messsage}. Continue (y/n)')
    if warning.lower() == 'n':
        return False
    return True


def display_prompt(message, input=false, binary=false, validator=None)
    '''Prompts user for input and returns the result as a string.'''
    if input and binary:
        prompt = f'{message}. (y/n)'
    elif input:
        prompt = message + ':'
    else:
        prompt = message
    
    resp = input(prompt')
    
    if validator:
        return validator(resp)
    return resp


def get_git_commit_log(project_path):
    ''' Returns the stdout from the subprocess as a string'''
    return subprocess.run(['git', 'log'], cwd=project_path, capture_output=True).stdout.decode("utf-8")


def update_commit_log(project_path, mailmap_path):
    '''Runs subprocess to update commit log with mailmap'''
    # TODO: Add validation and error handling
    subprocess.run(['git', 'filter-repo', '--mailmap', mailmap_path, '--force'], cwd=project_path)


def update_remote(project_path, remote_url):
    '''Runs subprocess to add remote to git repository'''
    # TODO: Add validation and error handling
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=project_path)


def push_to_remote(project_path):
    '''Runs subprocess to push git repository to remote'''
    # TODO: Add validation and error handling
    subprocess.run(['git', 'push', 'origin', '--all'], cwd=project_path)


if __name__ == "__main__":
    try:
        validate_git_path(argv[1])
        project_path = argv[1]
    except ValueError:
        print("The project path provided doesn't contain a git respository.")
        exit()

    try:
        validate_mailmap_path(argv[2])
        mailmap_path = argv[2]
    except ValueError:
        print("The mailmap path is invalid.")
        exit()    
    
    # Display's comment log
    get_git_commit_log(project_path)
    
    # Warn user of consequences
    if not display_warning('This script changes the commit log for the project'): 
        exit()
    update_commit_log()

    if display_prompt('Updating the commit log removes the remotes in the repository. Would you like to set new remotes for this project?', true, true):
        user_name =display_prompt('Enter github username', true, false)
        repo_name = display_prompt('Enter repository name', true, false)
        remote_url = f'{GITHUB_BASE}/{user_name}/{repo_name}.git'
        update_remote(project_path, remote_url)

    if display_prompt('Push changes to remote', true, true)
        push_to_remote(project_path)


    
        


    
    
    



