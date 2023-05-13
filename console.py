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

        print()
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
            inst = eval(arg)()
            print(inst.id)
            inst.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """

        line = arg.split(' ')
        ob_dict = storage.all()
        if not arg:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            inst = f"{line[0]}.{line[1]}"
            if inst not in ob_dict:
                print("** no instance found **")
            else:
                obj = ob_dict[inst]
                print(obj)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """

        line = arg.split(' ')
        obj_dict = storage.all()
        if not arg:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            inst = f"{line[0]}.{line[1]}"
            if inst not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[inst]
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name.
            The printed result must be a list of strings
        """

        list_obj = []
        all_obj = storage.all()

        if not arg:
            for key in all_obj:
                obj = all_obj[key]
                list_obj.append(obj.__str__())
            print(list_obj)
        elif arg not in HBNBCommand.clss:
            print("** class doesn't exist **")
        else:
            for key, value in all_obj.items():
                if arg == value.__class__.__name__:
                    ob = all_obj[key]
                    list_obj.append(ob.__str__())
            print(list_obj)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file)
        """

        line = arg.split(' ')
        if not arg:
            print("** class name missing **")
            return
        elif line[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return

        inst = f"{line[0]}.{line[1]}"
        objt_dict = storage.all()
        if inst not in objt_dict:
            print("** no instance found **")
            return

        if len(line) == 2:
            print("** attribute name missing **")
            return
        elif len(line) == 3:
            print("** value missing **")
            return
        elif len(line) == 4:
            obj = objt_dict[inst]
            att_name = line[2]
            att_value = line[3]
            if hasattr(obj, att_name):
                att_type = type(getattr(obj, att_name))
                c_value = att_type(att_value)
                setattr(obj, att_name, c_value)
                obj.save()
            else:
                setattr(obj, att_name, att_value)
                storage.save()
            return

    def default(self, arg):
        """ Method called on an input line when the command prefix
            is not recognized.
            Retrieve all instances of a class by using: <class name>.all()
            Retrieve the number of instances of a class: <class name>.count()
        """

        obj = storage.all()
        line = arg.split('.')
        count = 0

        if line[1] == 'all()':
            self.do_all(line[0])
        elif line[1] == 'count()':
            for i in obj:
                key = i.split('.')
                if key[0] == line[0]:
                    count += 1
            print(count)
        elif line[1].startswith("show"):
            d_line = line[1].split('("')
            d_line[1] = d_line[1].replace('")', '')
            self.do_show(f"{line[0]} {d_line[1]}")
        elif line[1].startswith("destroy"):
            d_line = line[1].split('("')
            d_line[1] = d_line[1].replace('")', '')
            self.do_destroy(f"{line[0]} {d_line[1]}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
