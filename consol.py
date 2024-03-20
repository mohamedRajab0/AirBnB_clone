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
        if len(args) < 2:
            print("class name missing ")
        if args:
            args = args.split()
            for item in args:
                if item == "BaseModel":
                    newobj = BaseModel()
                    with open("file.json", 'w') as f:
                        json.dump(newobj, f)
                    print(newobj.id)
                else:
                    print("class doesn't exist")
    def do_show(self, args):
        pass





    do_EOF =do_quit




if __name__ == '__main__':
    HBNBCommand().cmdloop()