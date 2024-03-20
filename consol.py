import cmd
import json

from models.base_model import  BaseModel

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
        print(type(items))
        if len(args) < 1 :
            print("class name missing")

        for item in items:
            if item != 'BaseModel':
                print("class doesn't exist")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.__dict__['id'])
    def do_show(self, args):
        items = args.split()
        if len(items) < 1:
            print("class name missing")
        name = items[0]
        inst_id = items[1]
        name_id = name + '.' + inst_id
        with open('file.json' , 'r', encoding='utf-8') as f:
            my_obj = json.load(f)
        print(my_obj[name_id])
        print(len(items))






    do_EOF =do_quit




if __name__ == '__main__':
    HBNBCommand().cmdloop()