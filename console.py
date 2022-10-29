#!/usr/bin/python3
"""
console containg command interprter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    simple commandline interpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """

        :param line: end of line
        :return: shows end of line
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
