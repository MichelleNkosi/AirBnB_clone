#!/usr/bin/python3
"""Module console.py: controles the interaction with the models"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class contains all custom CMD commands"""

    prompt = "(hbnb)"
    
    def do_quit(self, args):
        """This quits or exits the program"""
        return True    
    do_EOF = do_quit

    def do_create(self):
        """Create new BaseModel Obj"""
        pass

    def do_show(self):
        """Print string representation of instance based on class name and ID"""
        pass

    def do_destroy(self):
        """Deletes instance based on class name and id"""
        pass

    def do_all(self):
        """Prints string representation of all instances.
        Takes class name as argument"""
        pass

    def do_update(self):
        """Updates instance based on Class name and id(updates attributes)
        Usage: update <Class name>.<id> attribut value"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()