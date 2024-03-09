#!/usr/bin/python3
"""Module console.py: controles the interaction with the models"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """Class contains all custom CMD commands"""

    prompt = "(hbnb)"
    
    def do_quit(self, args):
        """This quits or exits the program"""
        return True    
    do_EOF = do_quit

    def do_create(self, args):
        """Create new BaseModel Obj
        Usage: create BaseModel"""
        if args == "":
            print("** class name missing **")
        elif args == "BaseModel":            
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print string representation of instance based on class name and ID"""
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")            
        elif args_list[0] == "BaseModel":
            if len(args_list) < 2:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                class_id = args_list[0] + "." + args_list[1]
                if class_id in all_objs.keys():
                    print(all_objs[class_id])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")            

    def do_destroy(self, args):
        """Deletes instance base on class name and id"""
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")            
        elif args_list[0] == "BaseModel":
            if len(args_list) < 2:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                class_id = args_list[0] + "." + args_list[1]
                if class_id in all_objs.keys():
                    print(all_objs[class_id])
                else:
                    print("** no instance found **")

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