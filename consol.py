import cmd
import json

from models import storage
from models.base_model import BaseModel

'''The implementation of the console (CLI) for the AirBnB project'''


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """return empty line"""
        return ""

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        items = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        for item in items:
            if item != 'BaseModel':
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.__dict__['id'])

    def do_show(self, args):
        """show objects with an id and class name"""
        items = args.split()
        if len(items) < 1:
            print("** class name missing **")
        else:

            if len(items) < 2:
                print("** instance id missing **")
                return

            name, inst_id = items[0], items[1]
            name_id = name + '.' + inst_id
            if name != 'BaseModel':
                print("** class doesn't exist **")
                return
            try:
                with open('file.json', 'r', encoding='utf-8') as f:
                    my_obj = json.load(f)
                if name_id in my_obj:
                    print(my_obj[name_id])
                else:
                    print("** no instance found ** ")
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")

    def do_destory(self, args):
        """destory objects with an id and class name"""
        items = args.split()
        if len(items) < 1:
            print("** class name missing **")
        else:

            if len(items) < 2:
                print("** instance id missing **")
                return

            name, inst_id = items[0], items[1]
            name_id = name + '.' + inst_id
            if name != 'BaseModel':
                print("** class doesn't exist **")
                return
            try:
                my_obj = storage.all()
                if name_id in my_obj:
                    del my_obj[name_id]
                    storage.save()
                    return

                print("** no instance found **")
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")

    def do_all(self , args):
        items = args.split(' ')
        if len(items) < 1:
            print("** class doesn't exist **")



    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
