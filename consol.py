import cmd
import json
import sys
from models import storage
from models.base_model import BaseModel
from  models.user import User
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
'''The implementation of the console (CLI) for the AirBnB project'''

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

class HBNBCommand(cmd.Cmd):

    my_classes = {'BaseModel': BaseModel(),'User': User(), 'State': State(), 'Review': Review(),
                    'Place': Place(), 'City': City(), 'Amenity': Amenity()}
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
            if item not in self.my_classes.keys():
                print("** class doesn't exist **")
            else:

                new_instance = self.my_classes[items[0]]
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
            if name not in self.my_classes.keys():
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
            if name not in self.my_classes.keys():
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
        """ Prints all string representation of all instances based or not on the class name"""
        items = args.split(' ')
        if len(args) < 1 or items[0] not in self.my_classes.keys():
            with open('file.json', 'r', encoding='utf-8') as f:
                my_obj = json.load(f)
                print(my_obj)
        else:
            print("** class doesn't exist **")
    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        items = args.split()
        if len(items) < 1:
            print("** class name missing **")
        else:

            if len(items) < 2:
                print("** instance id missing **")
                return

            name, inst_id = items[0], items[1]
            name_id = name + '.' + inst_id
            if name not in self.my_classes.keys():
                print("** class doesn't exist **")
                return



            try:
                my_object = storage.all()
                if name_id not  in my_object:
                    print("** no instance found ** ")
                    return
                if len(items) < 3:
                    print("** attribute name missing **")
                    return
                if len(items) < 4:
                    print("** value missing **")
                    return
                update_not = ['id', 'created_at', 'updated_at']
                if items[2] not in update_not:
                    my_object[name_id][items[2]] = items[3]
                    storage.save()
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")





    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
