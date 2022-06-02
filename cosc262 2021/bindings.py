""" Installs and updates modules for the current user.
    Updates pip if needed.
    Overwrites any rubbish currently installed for each module.
"""
import sys
import subprocess

MODULES_TO_INSTALL = ['graphviz', 'numpy', 'matplotlib']
PATH = sys.executable

def update_pip():
    """ Tries to ensure pip is installed and updated for the current user """
    print('Upgrading pip to latest version... \n')
    subprocess.run([PATH] + '-m pip install --user --upgrade pip'.split(), check=True)
    
    
def install_module_for_user(module):
    """ 
    Installs module if needed.
    Updates module if already installed.
    Forces install/update over top of any rubbish that's already there
    """
    print(f'Installing {module} for the current user... \n')
    subprocess.run([PATH] + f'-m pip install --user {module} --upgrade --ignore-installed'.split(), check=True)
    

def main():
    """ Feel free to add other modules to the list of things to install """
    print('Python executable at: {}\n'.format(PATH))
    update_pip()
    for module in MODULES_TO_INSTALL:    
        install_module_for_user(module)


if __name__ == "__main__":
    main()