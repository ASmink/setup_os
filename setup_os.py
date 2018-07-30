import os
import apt

class CommandExecuter:
    def __init__(self):
        pass

    def _execute_command(self, root, command):
        execution_string = ""

        if root:
            execution_string += "sudo "
        
        execution_string += command
        
        try:
            os.system(execution_string)
        except:
            print(f"Failed to run command: {execution_string}")

    def update_system(self):
        print("Updating Repositories and Upgrading Packages . . .")
        self._execute_command(True, f"apt update -y")
        self._execute_command(True, f"apt upgrade -y")
    
    def install_system_package(self, package_name):
        print(f"Installing System Package {package_name}. . .")
        self._execute_command(True, f"apt install {package_name} -y")

    def system_package_installed(self, package_name):
        cache = apt.Cache()
        try:
            return cache[package_name].is_installed
        except:
            return False

    def install_python_package(self, package_name, legacy=False):
        print(f"Installing Python Package {package_name}. . .")
        if legacy:
            self._execute_command(False, f"pip install -U {package_name}")
        else:
            self._execute_command(False, f"pip3 install -U {package_name}")


if __name__ == "__main__":
    command_executer = CommandExecuter()
    command_executer.update_system()

    system_packages = [
            "python", 
            "python-pip", 
            "python3",
            "python3-pip",
            "vim",
            "git",
            "htop",
            "awscli",
            "whois"
            ]
    
    for package in system_packages:
        command_executer.install_system_package(package)

    if command_executer.system_package_installed("python") and command_executer.system_package_installed("python-pip"):
        pass

    if command_executer.system_package_installed("python3") and command_executer.system_package_installed("python3-pip"):
        pass
