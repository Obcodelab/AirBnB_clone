#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '
    clss = ('BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review')

    def do_EOF(self, arg):
        """exits the program"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Does not execute anything """

        pass

    def do_create(self, arg):
        """ Creates a new instance, saves it and prints the id"""

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.clss:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
