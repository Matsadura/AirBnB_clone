#!/usr/bin/python3
"""
    A module that contains the HBNBCommand class
"""
import cmd
import json
import re
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
# TO REMOVE COLORS LATER
from colorama import Fore, Style


classes = {"BaseModel": BaseModel, "User": User, "City": City,
           "State": State, "Amenity": Amenity, "Review": Review,
           "Place": Place
           }


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
        # classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            # new_inst = BaseModel()
            new_inst = classes[args[0]]()
            storage.new(new_inst)
            storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
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
                    instance = classes[args[0]](**data[key])
                    print(instance)

    def do_destroy(self, line):
        """Deletes an instance"""
        # classes = ['BaseModel']
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
        all_instances = []
        args = cmd.Cmd.parseline(self, line)
        with open('file.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        if args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] and args[0] in classes:
            for key in data.keys():
                instance = classes[args[0]](**data[key]).__str__()
                all_instances.append(instance)
            print(all_instances)
        else:
            for key in data.keys():
                name = data[key]['__class__']
                instance = classes[name](**data[key]).__str__()
                all_instances.append(instance)
            print(all_instances)

    def do_update(self, line):
        """Updates an instance"""
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
            print(f"PARA : {para}, LEN: {len(para)}")
            key = f'{args[0]}.{para[0]}'
            print(f"key: {key}")
            if key not in data:
                print("** no instance found **")
            elif key in data:

                if len(para) == 1:
                    print("** attribute name missing **")
                elif len(para) == 2:
                    print("** value missing **")
                elif len(para) > 2:
                    quoted_flag = False
                    if '"' in args[1]:
                        quoted_str = re.findall(r'"(.*?)"', args[1])
                        quoted_flag = True
                    if quoted_flag is True:
                        data[key].update({f"{para[1]}": str(quoted_str[0])})
                    else:
                        data[key].update({f"{para[1]}": eval(para[2])})
                        print(type(eval(para[2])))
                    with open("file.json", 'w', encoding="utf-8") as f:
                        json.dump(data, f)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
