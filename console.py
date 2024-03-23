import cmd
import json
import re

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

    my_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                  'Review': Review, 'Place': Place, 'City': City,
                  'Amenity': Amenity}
    prompt = "(hbnb) "

    splitted = False

    items = []
    supported_commands = ['quit', 'create', 'show', 'destory', 'all', 'update']

    def precmd(self, line: str) -> str:
        self.splitted = False
        self.items = []
        check = line.split()

        if check[0] in self.supported_commands:
            return line

        try:
            function_name, args = self.fetch_parts(line)
            class_name, command = function_name.split('.')
            args = args.split(',', 1)
            final_command = f'{command}'
            self.items.append(class_name)
            arguments = ""

            for arg in args:
                arg = self.parse_str(arg.strip())
                arguments += (arg + ' ')

            arguments = arguments[:len(arguments)-1]

            real_args = self.parse_string_to_list(arguments)

            self.splitted = True

            for arg in real_args:
                self.items.append(arg)

            return final_command
        except Exception:
            return line

    def parse_string_to_list(self, input_string):
        # Use regular expression to find all matches of quoted strings, numbers
        matches = re.findall(r'"([^"]+)"|(\d+)', input_string)
        # Flatten the list of tuples and filter out None values
        result = [item for sublist in matches for item in sublist if item]
        return result

    def fetch_parts(self, input):
        match = re.match(r'(\w+\.\w+)\((.*)\)', input)
        if not match:
            raise ValueError("Invalid function call format")

        function_name = match.group(1)
        arguments = match.group(2)

        return function_name, arguments

    def parse_str(self, mystr):
        my_dict = {"{": 1, "}": 2,
                   ")": 3, "(": 4, ",": 5, ":": 6}
        new_str = ""
        for i in mystr:
            if i in my_dict.keys():
                continue
            if i == '\'':
                i = '"'
            new_str += f"{i}"
        return new_str

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """return empty line"""
        return ""

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not self.splitted:
            self.items = args.split()
        if len(self.items) < 1:
            print("** class name missing **")
            return

        for item in self.items:
            if item not in self.my_classes.keys():
                print("** class doesn't exist **")
            else:

                new_instance = self.my_classes[self.items[0]]
                obj = new_instance()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """show objects with an id and class name"""
        if not self.splitted:
            self.items = args.split()
        if len(self.items) < 1:
            print("** class name missing **")
        else:

            name = self.items[0]
            if name not in self.my_classes.keys():
                print("** class doesn't exist **")
                return

            if len(self.items) < 2:
                print("** instance id missing **")
                return
            inst_id = self.items[1]
            name_id = name + '.' + inst_id
            try:
                my_obj = storage.all()
                if name_id in my_obj:
                    print(my_obj[name_id].__str__())
                else:
                    print("** no instance found ** ")
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")

    def do_destroy(self, args):
        """destroy objects with an id and class name"""
        if not self.splitted:
            self.items = args.split()
        if len(self.items) < 1:
            print("** class name missing **")
        else:

            name = self.items[0]
            if name not in self.my_classes.keys():
                print("** class doesn't exist **")
                return
            if len(self.items) < 2:
                print("** instance id missing **")
                return
            inst_id = self.items[1]
            name_id = name + '.' + inst_id
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
        """
        Prints all string representation
        of all instances based or not on the class name
        """
        if not self.splitted:
            self.items = args.split()
        objects = []
        # print(len(items)) # => 0,1   class => not found
        if len(self.items) <= 1 or self.items[0] in self.my_classes.keys():
            for instance in storage.all().values():
                if (len(self.items) != 0 and
                        instance.__class__.__name__ == self.items[0]):
                    objects.append(instance.__str__())
                elif len(self.items) == 0:
                    objects.append(instance.__str__())
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        if not self.splitted:
            self.items = args.split()
        if len(self.items) < 1:
            print("** class name missing **")
        else:
            name = self.items[0]
            if name not in self.my_classes.keys():
                print("** class doesn't exist **")
                return
            if len(self.items) < 2:
                print("** instance id missing **")
                return

            inst_id = self.items[1]
            name_id = name + '.' + inst_id
            try:
                my_object = storage.all()
                if name_id not in my_object:
                    print("** no instance found ** ")
                    return
                if len(self.items) < 3:
                    print("** attribute name missing **")
                    return
                if len(self.items) < 4:
                    print("** value missing **")
                    return

                for i in range(2, len(self.items) - 1, 2):
                    setattr(my_object[name_id],
                            self.items[i],  self.items[i+1])

                storage.save()
            except FileNotFoundError:
                print("File not found error occurred")
            except json.JSONDecodeError:
                print("JSON decoding error occurred")

    def do_count(self, args):
        if self.items[0] not in self.my_classes.keys():
            print("** class doesn't exist **")
            return
        obj_conuting = 0
        for instance in storage.all().values():
            if instance.__class__.__name__ == self.items[0]:
                obj_conuting += 1
        print(obj_conuting)

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
