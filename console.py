import cmd
import json
import sys

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

'''The implementation of the console (CLI) for the AirBnB project'''


class HBNBCommand(cmd.Cmd):

    my_classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'Review': Review,
                  'Place': Place, 'City': City, 'Amenity': Amenity}
    prompt = "(hbnb) "

    supported_commands = ['quit', 'create', 'show', 'destory', 'all', 'update']

    # TODO:
    # def precmd(self, line: str) -> str:
    # vaildate = line.split(' ')
    # print(vaildate)
    # if vaildate[0] in self.supported_commands:
    #     print("iam actually here")
    #     print(line)
    #     return line
    # # <class name> functionName ("" , " " , " ")
    # # <class name> functionName ("" , {" " , " " , " "})
    # new_command = line.split('.')
    # class_name = new_command[0]
    # fun_name_with_args = new_command[1]
    # # print(class_name)
    # # print(fun_name_with_args)
    # return self.parse(fun_name_with_args) + ' ' +class_name

    # #TODO:
    # def parse(self, fun_with_args) -> list:
    #     command_args = []
    #     command = fun_with_args.split('(')
    #     command_args.append(command[0])
    #     args = command[1].split(',')
    #     command_args.append(args)
    #     command_args[-1][-1].replace(")" , "")
    #     # print(command_args)

    #     return command[0]

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
                obj = new_instance()
                obj.save()
                print(obj.id)

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
        items = args.split(' ')
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

    def do_all(self, args):
        """ Prints all string representation of all instances based or not on the class name"""
        items = args.split()
        objects = []
        num_of_instances = 0
        # len(items) => 0,1   class => not found
        if len(items) <= 1 or items[0] in self.my_classes.keys():
            for instance in storage.all().values():
                if len(items) != 0 and instance.__class__.__name__ == items[0]:
                    objects.append(instance.__str__())
                elif len(items) == 0:
                    objects.append(instance.__str__())
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        items = args.split()
        for item in items:
            print(item)
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
                if name_id not in my_object:
                    print("** no instance found ** ")
                    return
                if len(items) < 3:
                    print("** attribute name missing **")
                    return
                if len(items) < 4:
                    print("** value missing **")
                    return
                # <atrr> value <attr> value
                #         0                 1                       2    3      4          5
                # update User f7a9c035-8d67-4867-ab57-cf77277411c3 name ypuss my_number 219191
                for i in range(2, len(items) - 1, 2):
                    setattr(my_object[name_id], items[i],  items[i+1])
                storage.save()
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")

    def do_count(self, args):
        items = args.split()
        if items[0] not in self.my_classes.keys():
            print("** class doesn't exist **")
            return
        obj_conuting = 0
        for instance in storage.all().values():
            if instance.__class__.__name__ == items[0]:
                obj_conuting += 1
        print(obj_conuting)

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()



#TODO:
    # <class name>.Function( {})   => Function + <class name> + ()
    # "asojj oisajdf" => " "

    # User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89}) 
    # update User 38f22813-2753-4d42-b37c-57a17f1e4f88 first_name Jhon age 89
    # User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
    # update User 38f22813-2753-4d42-b37c-57a17f1e4f88 first_name Jhon