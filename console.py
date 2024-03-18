#!/usr/bin/python3
"""
    A module that contains the HBNBCommand class
"""
import cmd
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# TO REMOVE COLORS LATER
from colorama import Fore, Style


class HBNBCommand(cmd.Cmd):
    """
    """
    # TO REMOVE COLORS LATER
    prompt = f"{Fore.GREEN}(hbnb){Style.RESET_ALL} "

    def do_quit(self, line):
        """Exits the program"""
        exit(0)

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Does nothing if emptyline is entered"""
        return cmd.Cmd.emptyline(self)

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to JSON"""
        classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            storage.new(new_inst)
            storage.save()
            print(new_inst.id)

    @staticmethod
    def kwargs_class_str(name, **keys):
        """A static mothod that returns the instance based on **Kwargs"""
        classes = {
                'BaseModel': BaseModel(**keys).__str__()
                }
        return classes.get(name)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] in classes and args[1] == '':
            print("** instance id missing **")
        else:
            with open("file.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
                key = f'{args[0]}.{args[1]}'
                if key not in data:
                    print("** no instance found **")
                else:
                    # instance = BaseModel(**data[key]).__str__()
                    instance = self.kwargs_class_str(args[0], **data[key])
                    print(instance)

    def do_destroy(self, line):
        """Deletes an instance"""
        classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] in classes and args[1] == '':
            print("** instance id missing **")
        else:
            with open("file.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
            key = f'{args[0]}.{args[1]}'
            if key not in data:
                print("** no instance found **")
            else:
                data.pop(key)
                with open("file.json", 'w', encoding="utf-8") as f:
                    json.dump(data, f)

    def do_all(self, line):
        """Prints all string representation of all instances"""
        classes = ['BaseModel']
        all_instances = []
        args = cmd.Cmd.parseline(self, line)
        with open('file.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        if args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] and args[0] in classes:
            for key in data.keys():
                instance = self.kwargs_class_str(args[0], **data[key])
                all_instances.append(instance)
            print(all_instances)
        else:
            for key in data.keys():
                name = data[key]['__class__']
                instance = self.kwargs_class_str(name, **data[key])
                all_instances.append(instance)
            print(all_instances)

    def do_update(self, line):
        """Updates an instance"""
        classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        with open("file.json", 'r', encoding="utf-8") as f:
            data = json.load(f)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] in classes and args[1] == '':
            print("** instance id missing **")
        elif args[0] and args[1] is not None and args[1] != '':
            para = args[1].split(' ')
            key = f'{args[0]}.{para[0]}'
            if key not in data:
                print("** no instance found **")
            elif key in data:
                if len(para) == 1:
                    print("** attribute name missing **")
                elif len(para) == 2 and para[1] not in data[key][para[1]]:
                    print("** value missing **")
        else:
            



if __name__ == "__main__":
    HBNBCommand().cmdloop()
