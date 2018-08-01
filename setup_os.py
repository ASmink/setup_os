import os
import apt


class CommandExecutor:
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

    def system_packages_installed(self, package_names):
        if len(package_names) == 0:
            return True

        cache = apt.Cache()
        try:
            for package_name in package_names:
                cache[package_name].is_installed
        except:
            return False

        return True

    def install_python_package(self, package_name, legacy=False):
        print(f"Installing Python Package {package_name}. . .")
        if legacy:
            self._execute_command(False, f"pip install -U {package_name}")
        else:
            self._execute_command(False, f"pip3 install -U {package_name}")


if __name__ == "__main__":
    command_executor = CommandExecutor()
    command_executor.update_system()

    packages = {
        "system": [
            {
                "name": "python",
                "depends-on": []
            },
            {
                "name": "python-pip",
                "depends-on": []
            },
            {
                "name": "python3",
                "depends-on": []
            },
            {
                "name": "python3-pip",
                "depends-on": []
            },
            {
                "name": "vim",
                "depends-on": []
            },
            {
                "name": "git",
                "depends-on": []
            },
            {
                "name": "htop",
                "depends-on": []
            },
            {
                "name": "awscli",
                "depends-on": []
            },
            {
                "name": "whois",
                "depends-on": []
            },
        ],
        "python": [],
        "node": []
    }

    for package in packages.get("system"):
        if command_executor.system_packages_installed(package.get("depends-on")):
            command_executor.install_system_package(package.get("name"))

    if command_executor.system_packages_installed(["python", "python-pip"]):
        pass

    if command_executor.system_packages_installed(["python3", "python3-pip"]):
        pass
