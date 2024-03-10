#!/usr/bin/python3
"""Module console.py: controles the interaction with the models"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Class contains all custom CMD commands"""

    prompt = "(hbnb)"
    model_list = ["BaseModel"]

    def do_quit(self, args):
        """This quits or exits the program"""
        return True
    do_EOF = do_quit

    def do_create(self, args):
        """Create new BaseModel Obj
        Usage: create BaseModel"""
        if not args:
            print("** class name missing **")
        elif args in self.model_list:
            class_obj = globals().get(args)
            new_obj = class_obj()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print string representation of instance based
        on class name and ID"""
        args_list = args.split()
        if self.check_args(args_list, 2) is True:
            storage.reload()
            all_objs = storage.all()
            class_id = args_list[0] + "." + args_list[1]
            if class_id in all_objs.keys():
                obj_dict = all_objs[class_id]
                obj_class = globals().get(args_list[0])
                obj = obj_class(**obj_dict)
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes instance base on class name and id"""
        args_list = args.split()
        if self.check_args(args_list, 2) is True:
                all_objs = storage.all()
                class_id = args_list[0] + "." + args_list[1]
                if class_id in all_objs.keys():
                    storage.delete(class_id)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """Prints string representation of all instances.
        Takes class name as argument"""
        storage.reload()
        args_list = args.split()
        if not args:
            all_objs = storage.all()
            for class_id, model in all_objs.items():
                class_key = class_id.split(".")
                class_name = class_key[0]
                if class_name in self.model_list:
                    class_obj = globals().get(class_name)
                    obj = class_obj(**model)
                    print(obj)

        elif args in self.model_list:
            all_objs = storage.all()
            for class_id, model in all_objs.items():
                class_key = class_id.split(".")
                class_name = class_key[0]
                if class_name == args:
                    class_obj = globals().get(class_name)
                    obj = class_obj(**model)
                    print(obj)

        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates instance based on Class name and id(updates attributes)
        Usage: update <Class name>.<id> attribut value"""
        args_list = shlex.split(args)
        storage.reload()
        if self.check_args(args_list, 4):
            all_objs = storage.all()
            arg_class_id = args_list[0] + "." + args_list[1]
            if arg_class_id not in all_objs.keys():
                print("** no instance found **")
            else:
                class_name = args_list[0]
                class_obj = globals().get(class_name)
                class_dict = all_objs[arg_class_id]
                storage.delete(arg_class_id)
                obj = class_obj(**class_dict)
                setattr(obj, args_list[2], args_list[3])
                storage.new(obj)
                obj.save()

    def check_args(self, args_list, arg_no):
        """Checks if the arguments are valid"""
        if len(args_list) < 1:
            print("** class name missing **")
            return False
        elif args_list[0] not in self.model_list:
            print("** class doesn't exist **")
            return False
        elif len(args_list) < 2:
            print("** instance id missing **")
            return False
        if arg_no >= 4:
            if len(args_list) < 3:
                print("** attribute  name missing **")
                return False
            if len(args_list) < 4:
                print("** value missing **")
                return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
