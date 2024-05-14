import subprocess
import os
from MenuItem import MenuItem  # Assuming MenuItem is defined in MenuItem.py

class CommandExecutor:
    """
    The CommandExecutor class in python_menus/smart_menu/CommandExecutor.py is designed to execute commands associated with menu items. It has a single static method called execute_command that takes a menu_item object as input.

    The purpose of this code is to provide a way to run commands or actions specified by menu items. These menu items could be part of a graphical user interface (GUI) or a command-line interface (CLI) application. The execute_command method checks if the input menu_item is an instance of the MenuItem class. If not, it raises a ValueError exception.

    If the menu_item is valid, the method first saves the current working directory of the program using os.getcwd(). It then checks if the menu_item has a working_directory attribute set. If it does, the method changes the current working directory to the specified directory using os.chdir().

    Next, the method checks if the menu_item has an open_in_subprocess attribute set. If it's True, the method uses the subprocess.run() function to execute the command specified in the menu_item.action attribute. The shell=True argument tells the subprocess to execute the command through the system's shell, and check=True raises an exception if the command returns a non-zero exit code.

    If open_in_subprocess is False, the method uses the os.system() function to execute the command directly in the current process. This is a placeholder, and in reality, more direct execution methods might be used depending on the command.

    If an exception occurs during the execution of the command, the method prints an error message with the command and the exception details.

    Finally, regardless of whether an exception occurred or not, the method restores the original working directory using os.chdir(original_dir).

    The code does not produce any output directly, but it executes commands or actions specified by the menu_item object. The output of the executed command, if any, will be displayed in the console or the appropriate output stream.
    """
    @staticmethod
    def execute_command(menu_item):
        """Executes the command associated with a given MenuItem."""
        if not isinstance(menu_item, MenuItem):
            raise ValueError("menu_item must be an instance of MenuItem")

        original_dir = os.getcwd()  # Save the original directory
        try:
            # Change the working directory if specified
            if menu_item.working_directory:
                os.chdir(menu_item.working_directory)
            
            # Execute command in a subprocess or current process
            if menu_item.open_in_subprocess:
                subprocess.run(menu_item.action, shell=True, check=True)
            else:
                # This is a placeholder for executing the command without opening a new subprocess.
                # In reality, this might involve more direct execution methods depending on the command.
                os.system(menu_item.action)
        except Exception as e:
            print(f"Error executing command {menu_item.action}: {e}")
        finally:
            os.chdir(original_dir)  # Restore the original directory
