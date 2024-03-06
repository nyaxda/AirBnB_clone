#!/usr/bin/python3
"""Command interpreter. Contains entry point for it."""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter class. Contains entry point for it."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit(1)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
