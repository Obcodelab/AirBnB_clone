#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exits the program"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Does not execute anything """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
