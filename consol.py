#!/usr/bin/python3
'''The implementation of the console (CLI) for the AirBnB project'''

commands = ["quit", "create", "update", "all", "--help"]

description = {
    "quit": "quits the program",
    "--help": "lists the vaild commands in consol",
    "create": "creates a new user",
    "update": "updates a user that has been aready created"
    " if not found nothing happen",
    "all": "i dont know yet"
}

# if __name__ == '__main__':
while True:
    print("(hbnb) ", end="")
    command = input("")

    if command == "--help":
        print("Usage: (command) [OPTION...] [SECTION] PAGE...")
        for vaild_command in commands:
            print(f"(command) {vaild_command} : {description[vaild_command]}")

    elif command == "quit":
        exit()

    else:
        print("Try '--help' for more information")
        continue
