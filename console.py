#!/usr/bin/python3
"""Command interpreter. Contains entry point for it."""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class. Contains entry point for it."""
    prompt = "(hbnb) "

    def do_EOF(self):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self):
        """Quit command to exit the program"""
        sys.exit(1)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        elif arg != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            creation = BaseModel()
            self.storage.new(creation)
            self.storage.save()
            print(creation.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            self.storage.reload()
            objects = self.storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            self.storage.reload()
            objects = self.storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                del objects[key]
                self.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = arg.split()
        self.storage.reload()
        objects = self.storage.all()
        if args and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        for key, obj in objects.items():
            if not args or args[0] == "BaseModel":
                print(str(obj))

    def update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)."""
        args = arg.split()
        static_attr = ["id", "created_at", "updated_at"]
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            self.storage.reload()
            objects = self.storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print("** no instance found **")
            if argss[2] in static_attr:
                return
            item = objects[key]
            try:
                attribute_type = type(getattr(item, args[2]))
                item.__dict__[args[2]] = attribute_type(args[3])
            except AttributeError:
                item.__dict__[args[2]] = args[3]
            self.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
