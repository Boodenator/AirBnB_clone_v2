#!/usr/bin/python3
"""
The entry point of the command interpreter
and the definition of console class
"""
from cmd import Cmd
from models import storage
from models.engine.error import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = storage.models


class HBNBCommand(Cmd):
    """
    The Console command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """quit the program"""
        return True

    def do_EOF(self, args):
        """Exit the programme at non-interactive mode"""
        return True

    def do_create(self, args):
        """Create an instance of BaseModel and save it
        to JSON given its name eg.$ create ModelName
        print out Error if ModelName missing or doesn't exist"""
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            # temp = classes[args[0]]()
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many arguments to be created **")
            pass

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id eg.$ show MyModel
        instance_id and prints out if class name missing or dont exist"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments to show **")
            pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id and
        save it to JSON file and then prints outt error if class name
        is missing or dont exist"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments to destroy **")
            pass

    def do_all(self, args):
        """ Prints all string representation of all instances based or
        not on the class name"""
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many arguments to all **")
            pass

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")

    def do_models(self, arg):
        """Print out registered Models"""
        print(*classes)

    def handle_class_methods(self, arg):
        """Handle Class Methods
        <cls>.all(), <cls>.show() etc
        """

        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for x in printable:
                if x in arg:
                    print(val)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass

    def default(self, arg):
        """ByPass default method to handle class methods"""
        if '.' in arg and arg.split('.')[0] in classes and arg[-1] == ')':
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """ByPass empty line and do nothing"""
        return


def parse(line: str):
    """spaces usage to split a line"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
